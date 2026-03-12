
import numpy as np

# Create a 4 × 4 matrix of zeros.
# Then print:
# the matrix
# its shape
# its size
arrays=np.zeros((4,4))
# [[2,4,5,1], [6,7,2,8], [9,10,4,8], [5,1,4,0]]
print(arrays)
print(arrays.shape)
print(arrays.ndim)
print(arrays.size)


print("x----------------x")
# Create a 3 × 5 matrix of ones.
# Then print:
# .ndim
# .dtype
arrays=np.ones((3,5))
print(arrays)
print(arrays.ndim)
print(arrays.dtype)

print("x----------------x")
# Create a 5 × 5 identity matrix.
arrays= np.eye(5)
print(arrays)

print("x----------------x")
# Create an array from 10 → 50 with step 5
arrays=np.arange(10,50,5)
print(arrays)
print(arrays.shape)
print(arrays.size)

print("x----------------x")
# Generate 6 numbers between 0 and 1
arrays= np.linspace(0,1,6)
print(arrays)

print("x----------------x")
#typecasting

arrays=np.array([2,4,5,7])
print(arrays.astype(float))

print("x----------------x")
arrays=np.array([[0,128,255]], dtype=np.uint8)
print(arrays)
print(arrays.dtype)
print(arrays.size)

print("x----------------x")
arrays= np.array([1.5,2.8, 3.3, 4.9])
print(arrays.astype(int))

print("x----------------x")

arrays=np.ones((3,3))
arrays*=5
print(arrays)