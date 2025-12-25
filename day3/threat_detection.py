import subprocess
result = subprocess.run(
['journalctl','-u','ssh'], capture_output=True, text=True )
if result.returncode!=0:
        print('Process Failed')
lines=result.stdout.splitlines()
count=0
for line in lines:
        if 'Failed'in line  or 'failed' in line:
                count+=1
if count<5:
	print ('Normal')
elif 10 >count>=5:
	print('Warning')
else :
	print ('Alert')
