import numpy as np


# ===========
# Determinant
# ===========
#np.linalg.det()




# determinant = 0 → ❌ not invertible
# determinant ≠ 0 → ✅ invertible
# sign (+/-) doesn’t matter for invertibility


A=np.array([[1,2],
            [3,4]])

print(np.linalg.det(A))  #Determinant
print("X-------------------X")

A=np.array([[1,2],
            [2,4]])
print(np.linalg.det(A))

print("X-------------------X")

A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])
print(np.linalg.det(A))


A=np.array([[2,5],[5,9]])

print(np.linalg.det(A))

print("X-------------------X")
# ===========
# inverse
# ===========


A=np.array([[1,2],[3,4]])
print(np.linalg.inv(A))
print(A@np.linalg.inv(A))


print("X-------------------X")

# ================
# Solving Equation
# ================
#Solving equations = multiplying by inverse matrix
# A × X = B
# A = coefficients  
# X = variables  
# B = results

A=np.array([[1,2],[3,4]])
B=np.array([[5,6],[7,8]])
print(np.linalg.solve(A,B))   #X = A⁻¹ × B

print("X-------------------X")
# ========================
# Eigen values and vectors
# ========================

A = np.array([[2, 0],
              [0, 3]])

values, vectors= np.linalg.eig(A)

print(values)   # scaling
print(vectors)


print("X-------------------X")
# ====
# Norm
# ====

A=np.array([3,4])
print(np.linalg.norm(A))


print("X-------------------X")
# =================
# Linear Regression
# =================

X=np.array([[1,1],
            [1,2],
            [1,3]])
Y=np.array([2,3,4])
# FORMULA FOR LINEAR REGRESSION:
# W=(X.T @ X) @ X.T @ Y

W=np.linalg.inv(X.T @ X) @ X.T @ Y
print(W)
