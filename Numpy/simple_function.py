import numpy as np
a=np.arange(1,11,2)
print(a)
print("\n")

b=np.arange(1,11).reshape(5,2)
print(b)
print("\n")

c=np.arange(1,13).reshape(3,4)
print(c)
print("\n")

# np.ones and np.zeros
d=np.ones((3,4))
print(d)
print("\n")

e=np.zeros((2,3))
print(e)
print("\n")

f=np.random.random((3,4))
print(f)
print("\n")

g=np.linspace(-10,10,10)#Lower range , Upper Range , Number of Items
print(g)
print("\n")# The difference between the elements in this array is same.

h=np.identity(3)# Creates an Identity Matrix
print(h)
print("\n")