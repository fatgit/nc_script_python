import subprocess



qq = 'grep 333 /home/fat/11.conf'

process = subprocess.Popen(qq, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output,stderr = process.communicate()
status = process.poll()

print(output)

if output == '':
    print ('not found')
else:
    print('found')
