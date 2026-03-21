# Generate synthetic data: y = 3x + 7 + noise. Build feature matrix X with bias column. Solve for weights using NumPy's normal equation w = (XᵀX)⁻¹Xᵀy. Predict on test data, compute MSE. Compare with np.linalg.solve().



import numpy as np

X1=np.array([1,2,3,4,5])
noise=np.random.randn(5)
y= (3*X1) + 7 + noise
print(f"actual: {y}")

#hstack	Flattens into one row
# column_stack	Creates columns (2D matrix)
#-----------------
#building a matrix
#-----------------
x=np.column_stack((np.ones(5),X1))
print(x)
#-----------------
#solving weight
#-----------------
w= np.linalg.inv(x.T @ x) @x.T@y
print(f"weight: {w}")
#-----------------------
#prediction on test data
#-----------------------
y_pred= x@w
print(y_pred)
#-----------------
#computing MSE
#-----------------
# MSE = mean((y - y_pred)²)  #mean square error(how long our predictions are)
mse=np.mean((y-y_pred)**2)
print(f"Mean squared error: {mse}")
#------------------------------
#comparing with linalg.solve()
#------------------------------
A=x.T@x
B=x.T@y
w2=np.linalg.solve(A,B)
print(w2)


#Eventually, both (w and w2) gives same result, the 2nd method is preferred.