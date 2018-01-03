import subprocess

# the getoutput() function capture the comands of bash shell
ret = subprocess.getoutput('date')
print(ret)

ret = subprocess.getoutput('date -u')
print(ret)

# wc can compute the data -u have 1 line, 
# 6 words and 43 characters
ret = subprocess.getoutput('date -u | wc')
print(ret)


# the function of check_output() don't use the bash shell
ret = subprocess.check_output(['date', '-u'])
print(ret)

# getstatusoutput() can return the exitst status and output the tuple
ret = subprocess.getstatusoutput('date')
print(ret)

# if just want to the exist status, using the call()
ret = subprocess.call('date')
print(ret)

# shell = True express that the program will be executed by shell
ret = subprocess.call('date -u', shell = True)
print(ret)

# the program will be executed by no shell
ret = subprocess.call(['date', '-u'])
print(ret)


