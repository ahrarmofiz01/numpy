import numpy as np
x=[1,2,3]
y=[4,5,6]
z=np.array([x,y])
print(z)
x=[1,2,3]
y=[4,5,6]
a=[7,8,9]
z=np.array([[x,y,a]])
print(z)
print(z.ndim)
x=[1,2,3]
y=[4,5,6]
a=[7,8,9]
b=[10,11,12]
z=np.array([[[x,y,a,b]]])
print(z)
print(z.ndim)