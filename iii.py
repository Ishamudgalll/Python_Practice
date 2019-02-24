import matplotlib.pyplot as plt
import random
y=[]
x=[]
for i in range(0,10):
	a=random.randint(-10,10)
	x.append(a)
for i in range(len(x)):
	b=4*x[i]*x[i]
	y.append(b)

x.sort()
y.sort()	

	




plt.plot(x,y)
plt.show()