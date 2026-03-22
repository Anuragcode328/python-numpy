import numpy as np
a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)
print(a1)
print("\n")
print(a2)

#Scalar operations 
b1=a1*2
print(b1)
print("\n")
b2=a2+2
print(b2)
print("\n")
print(a1**2)
print(a1>5)
print(a1+a2)