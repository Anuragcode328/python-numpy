import numpy as np
a1=np.arange(10)
a2=np.arange(12,dtype=float).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)

#ndim - Dimension of an array
a=a1.ndim
print(a)
print("\n")
b=a2.ndim
print(b)
print("\n")
c=a3.ndim
print(c)
print("\n")

#shape
d=a1.shape
print(d)
print('\n')
e=a2.shape
print(e)
print("\n")
f=a3.shape
print(f)
print("\n")

#size
g=a1.size
print(g)
print("\n")
h=a2.size
print(h)
print("\n")
i=a3.size
print(i)
print("\n")

#itemsize - integer here as 64 bit as 8 byte
j=a1.itemsize
print(j)
print("\n")
k=a2.itemsize
print(k)
print("\n")
l=a3.itemsize
print(l)
print("\n")

#dtype - datatype
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

# Changing Datatype - astype
m=a3.astype(np.int32)
print(m)
print(a3.dtype)
print(m.dtype)