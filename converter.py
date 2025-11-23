import math
msg = input()
ascii = [ord(i) for i in msg]
#print(ascii)
sq = list(map(math.sqrt, ascii))
#print(sq)
m1 = list(map(int,sq))
rem = []
for i in range(len(m1)):
	rem.append(ascii[i]-m1[i]**2)
#print(m1, rem)
m2 = m1[:]
for i in range(len(rem)):
	m2[i] += rem[i]//m1[i]
	rem[i] = rem[i]%m1[i]
	#if m2[i]//2<rem[i]:
	#	m2[i] += 1
	#	rem[i] -= m2[i]//2
#print(m1,m2,rem)
c1 = list(map(lambda x:">"+("+"*x), m1))
c1[0] = c1[0][1:]
c2 = list(map(lambda x:"+"*x, m2))
c3 = list(map(lambda x:">"+("+"*x+"."), rem))
#print(c1, c2, c3)

c2 = list(map(lambda x: "[>"+x+"<-]", c2))
#print(c1, c2, c3)
res = []
for i in range(len(c1)):
	res.append(c1[i]+c2[i]+c3[i])
res = '\n'.join(res)
print(res)
