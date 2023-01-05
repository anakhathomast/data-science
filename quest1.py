import numpy as np
a= np.array([[2,3,4],[7,8,9],[1,4,5]])
b= np.array([[1,2,3],[4,5,6],[7,8,9]])
print("matrix A:\n",a)
print("matrix B:\n",b)
c= np.transpose(a)
print("transpose of A:\n",c)
d= np.multiply(a,c)
print("multiply of A:\n",d)
k= np.transpose(b)
print("transpose of B:\n",k)
m= 2*b
print("2B:\n",m)
g=np.multiply(m,k)
print("2*b*transpose of B:\n",g)
e=d-g
print("Transpose Matrix:\n")
print(e)
