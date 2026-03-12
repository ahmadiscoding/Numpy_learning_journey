# Create a Python script that builds a 'zoo' of arrays — 1D, 2D, 3D — and prints a formatted report showing name, shape, ndim, size, and dtype for each.

import numpy as np

array1=np.array([1,2,3,4])
array2=np.array([[1,3,5,7], [2,4,6,8]])
array3=np.array([[[1,2,3,4], [5,6,7,8], [9,10,11,12]]])


def report(name,arr):
    print(f"Array's Name: {name}")
    print(f"Shape: {arr.shape}")
    print(f"dimension: {arr.ndim}")
    print(f"size: {arr.size}")
    print(f"type: {arr.dtype}")

report("Array_1",array1)
report("Array_2", array2)
report("Array_3", array3)
