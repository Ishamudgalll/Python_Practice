import random
import matplotlib.pyplot as plt
mean=20
standard=34
a=0
b=0
c=[]
y=[]
for i in range(5000):
	a=random.randint(-4,4)
	b=mean+a*standard
	c.append(b)
	y.append(5)




c.sort()
y.sort()



plt.bar(c,10)
plt.show()