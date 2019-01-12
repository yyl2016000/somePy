import os

libs = ["pandas"]#列表项即为待安装库

for i in libs:
	try:
		os.system("pip install "+i)
		print(i+" Successful Install")
	except:
		print(i+"Failed Install")