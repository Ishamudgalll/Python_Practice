a=input()
b=str(a)
c="NO"
d=len(b)
for i in range(d):
  if(b[i].count('1')==1):
    c="YES"
  else:
  	if(b[i].count('0')==1):
  		c="YES"
  	else:
  		c="NO"

    
print(c)    
