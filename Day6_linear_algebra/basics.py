import numpy as np

# ======================
# Matrix Multipulication
# ======================
# row of A × column of B
# we can use both @ or np.dot
A= np.array([[1,2],[3,4]])
B= np.array([[5,6],[7,8]])

print(F"Matrix multipulication: {A@B}")  #Matrix multipulication


C=np.array([1,2,3])
# print(A@C)  #will show Error
# #(m × n) @ (n × p)   Inner dimensions must match


# ============================
# Element-wise Multipulication
# ============================
# [[1*5, 2*6],    = [[5, 12],
# [3*7, 4*8]]       [21, 32]] 

A= np.array([[1,2],[3,4]])
B= np.array([[5,6],[7,8]])
print(F"Element wise: {A*B}")


# =========
# Transpose
# =========
#it flips rows into columns

arr=np.array([[1,2,3,4], 
              [5,6,7,8]])

print(f"simple:{arr}")
print(f"arr.T: {arr.T}")
print("Original shape:", arr.shape)
print("Transpose shape:", arr.T.shape)


