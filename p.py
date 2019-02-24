
import numpy as np
arr=np.array([[1,2,3],[1,2,3],[1,2,3]])
print(arr.shape)
print(arr.size)

print(arr.dtype)
#2^row+column-1
print(arr.ndim)
print(type(arr))
print(arr.flatten)
print(np.log(arr))
print(np.exp(arr))

a=np.random.randn(4,6)
print([a])
c=np.zeros((5))#algorithm fail
d=np.zeros((5,1))
print(c.shape)
print(d.shape)
fd=c.reshape(5,1)
print(fd.shape)
print(d.T)


#a=np.array(5,6)
#print(a)


A=np.random.randn(1,4)*0.01
print([A])
B=np.random.randn(4,150)
print([B])
z=np.dot(A,B)
o=np.exp(z)
e=1+np.exp(z)
y=o/e
print(z)
print(y)

