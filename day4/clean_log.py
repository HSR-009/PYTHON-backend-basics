import subprocess
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
        with open('security(1).log','a') as f:
                f.write(f"========= Security Scan Report =========\nScan Time : {log_time}\n\n\nUsername : {user}\nActive IPs:\n{ip}\n\n\nFailed ssh attempts :{count}\nSecurity Status :{status}\n========================================\n\n")
try:
	user=get_current_user()
	ip=get_network_info()
	count=count_failed_ssh_attempts()
	status=get_security_status(count)
	write_log(log_time, user, ip, count, status)
except Exception as e:
        print (e)
