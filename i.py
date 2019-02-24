a=[]
d=[]
c=[]
b=[int(a) for a in input().split()]
for i in range(len(b)):
	if (b[i]%3==0):
		c.append(b[i])
	else:
		d.append(b[i])

for x in d:
    print(x, end=" ")
		
		

