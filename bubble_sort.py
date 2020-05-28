import random
import time
x=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
y=0
c=0
b=0


for i in range(10):
	data=[]
	for j in range(i):
		c=random.randint(1,500)
		data.append(c)
		


print(data)
t1=time.time()
def bubbleSort(x):
    for passnum in range(len(data)-1,0,-1):
        for i in range(passnum):
            if data[i]>data[i+1]:
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp

bubbleSort(data)
print(data)


t2=time.time()


print(t1-t2)
