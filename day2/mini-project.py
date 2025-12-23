import subprocess
from datetime import datetime
stime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Scan Time: {stime}\n")
result=subprocess.run(
['ip','a'],capture_output=True,text=True
)

if result.returncode!=0:
	print("Unable to return results, Please verify again !!!")
print("ACTIVE NETWORK INTERFACES:\n")
lines=result.stdout.splitlines()
flag=0
for line in lines:
	if "inet" in line and "127.0.0.1" not in line:
		print(line)
		flag+=1
if flag==0:
	print("Sorry, no active network interfaces are present.")
