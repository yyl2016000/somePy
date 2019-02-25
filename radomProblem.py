import random
import time
problems_num = 25#题目的个数
numRange = 30#数的范围

#out_file = open("D:\题目"+str(time.strftime('%Y-%m-%d',time.localtime(time.time())))+".txt",'a')
out_file = open("D:\题目2.txt",'w')

for i in range(problems_num):
    a = random.randint(1,numRange)
    flag = random.randint(0, 1)
    if flag == 0:
        b = str((random.randint(1, numRange)))
        out_file.write(str(a)+"+"+b+"="+"\n")
    else:
        b = str(random.randint(1, a))
        out_file.write(str(a)+"-"+b+"="+"\n")
out_file.close()