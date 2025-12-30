import subprocess
import json
from datetime import datetime
log_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
def get_current_user():
        user=subprocess.run(['whoami'],capture_output=True,text=True)
        return user.stdout.strip()
def get_network_info():
        ip=subprocess.run(['ip','a'],capture_output=True,text=True)
        return ip.stdout
def count_failed_ssh_attempts():
        result=subprocess.run(['journalctl','-u','ssh'],capture_output=True,text=True)
        lines=result.stdout.splitlines()
        count=0
        for line in lines:
                if 'Failed' in line or 'failed' in line:
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
        with open('/home/kali/python_backend/day5/security.log','a') as f:
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
try:
	user=get_current_user()
	ip=get_network_info()
	count=count_failed_ssh_attempts()
	status=get_security_status(count)
	scan_result = {
	"timestamp": log_time,
	"user": user,
	"failed_ssh_attempts": count,
	"security_status": status
	}
	print(scan_result)
	write_log(log_time, user, ip, count, status)
	write_json_log(scan_result)
except Exception as e:
        print (e)
