import subprocess
import json
import os
from datetime import datetime
def get_current_user():
        user=subprocess.run(['whoami'],capture_output=True,text=True,check=False)
        return user.stdout.strip()
def get_network_info():
        ip=subprocess.run(['ip','a'],capture_output=True,text=True,check=False)
        return ip.stdout
def count_failed_ssh_attempts():
        result=subprocess.run(['journalctl','-u','ssh'],capture_output=True,text=True,check=False)
        lines=result.stdout.splitlines()
        count=0
        for line in lines:
                if 'failed' in line.lower():
                        count+=1
        return count
def get_security_status(count):
        if count<5:
                status="Normal"
        elif 10>count>=5:
                status="Warning"
        else :
                status="Alert"
        return status
def write_log(log_time, user, ip, count, status):
        with open('security.log','a') as f:
                f.write(
                "========= Security Scan Report =========\n"
                f"Scan Time : {log_time}\n\n"
                f"Username : {user}\n"
                f"Active IPs:\n{ip}\n"
                f"Failed SSH Attempts : {count}\n"
                f"Security Status : {status}\n"
                "========================================\n\n")
def write_json_log(scan_result):
    with open('security.json', 'a') as jf:
        jf.write(json.dumps(scan_result) + "\n")

def read_logs():
        logs=[]
        if not os.path.exists("security.json"):
                return logs
        with open("security.json","r") as j:
                for line in j:
                        try:
                                logs.append(json.loads(line))
                        except json.JSONDecodeError:
                                continue
                return logs

def compute_baseline(logs):
        if not logs:
                return 0
        total=0
        for l in logs:
                total+=l.get("failed_ssh_attempts",0)
        return total/len(logs)

def calculate_risk_score(current,baseline):
        if baseline == 0:
                return 30
        ratio =(current/baseline)
        if ratio <=1:
                return 20
        elif ratio <=2:
                return 50
        elif ratio <=3:
                return 80
        else :
                return 100

def ai_decision(risk_score):
    if risk_score < 30:
        return "Normal Behavior"
    elif risk_score < 70:
        return "Suspicious Activity"
    else:
        return "Potential Attack"

def log_error(log_time,err_msg):
        with open('error.log','a') as er:
                er.write(f"[{log_time}] Error: {err_msg}\n") 

def run_security_scan():
        log_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
                user=get_current_user()
                ip=get_network_info()
                count=count_failed_ssh_attempts()
                status=get_security_status(count)
                logs=read_logs()
                baseline=compute_baseline(logs)
                risk_score=calculate_risk_score(count,baseline)
                ai_result = ai_decision(risk_score)
                scan_result = {
                "timestamp": log_time,
                "user": user,
                "failed_ssh_attempts": count,
                "security_status": status,
                "baseline": round(baseline, 2),
                "risk_score": risk_score,
                "ai_decision": ai_result
                }
                print(scan_result)
                print("Baseline logs :",baseline)
                print("Risk Score: ",risk_score)
                print("AI Decision:", ai_result)
                write_log(log_time, user, ip, count, status)
                write_json_log(scan_result)
                return scan_result

        except Exception as e:
                log_error(log_time,str(e))
                return {"error": "Scan Failed"}
