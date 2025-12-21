import subprocess
from datetime import datetime

log_file="system.log"

try:
    user=subprocess.getoutput('whoami')
    uptime=subprocess.getoutput('uptime')
    ip=subprocess.getoutput('ip a')

    current_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("system.log","a") as file:
        file.write(f"\n--- Log Time: {current_time} ---\n")
        file.write(f"User: {user}\n")
        file.write(f"Uptime: {uptime}\n")
        file.write(f"IP Info:\n{ip}\n")

    print("System info saved successfully")

except Exception as error:
    print("Something went wrong:", error)

