import subprocess
result=subprocess.run(
	['ip','a'],
	capture_output=True,
	text=True
)
if result.returncode != 0:
	print("Command Failed")
lines=result.stdout.splitlines()
for line in lines:
	if "inet" in line:
		print(line)
