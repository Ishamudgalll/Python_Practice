a=input()
b=str(a)
c=str()
if(b.count('0')==1):
	c="YES"
else:	
	if(b.count('1')==1):
		c='YES'
	else:
		c="NO"

print(c)
