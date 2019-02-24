a=(input())
b=int(a)
c=0
d="NO"
r=[]
t=[]
while(b>0):
	c=c+1
	r.append(b%10)
	b=int(b/10)									
																	
    

for i in range(len(r)):
	if(r.count(r[i])==1):
		d="YES"





print(d)		


