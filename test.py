H = []
W = []

n = int(input())

for i in range(n):
	H.append(tuple(map(int,input().split())))

for i in range(n):
	W.append(tuple(map(int,input().split())))
	
tlen = max(H[-1][-1],W[-1][-1])
timelen = [0]*tlen

for s,e in H:
	for i in range(s,e):
		timelen[i]+=1

for s,e in W:
	for i in range(s,e):
		timelen[i]+=1

print(timelen.count(2))