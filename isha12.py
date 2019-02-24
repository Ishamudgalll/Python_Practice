a=["harsh","gog","harsh","rajat","tom","rajat","rajat","tom","gog","harsh"]
f=[]
print(a)
a.sort()
print(a)
b=sorted(a)
print(b)
for i in range(len(b)):
	c=b.count(b[i])
	f.append(c)
	print(b[i],"=",c)

e=max(f)
print(e)
print(f)
a
