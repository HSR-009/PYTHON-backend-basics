import subprocess
result=subprocess.run(
	['whoami'],
	capture_output=True,
	text=True
)
name=result.stdout.strip()
print(name)
