if __name__ == "__main__":
	import subprocess
	uptime=subprocess.run(['uptime'],capture_output=True,text=True)
	with open('/home/kali/python_backend/day5/demo.log','a') as d:
		d.write(f"Uptime : {uptime.stdout}\n")
