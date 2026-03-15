import numpy as np


# ---------------
# Basic transpose
# ---------------
arr= np.arange(0,6).reshape(2,-1)
print(f"Simple: {arr}")
print(f"Transpose: {arr.T}")

# -------------
# Square matrix
# -------------

arr_1= np.arange(0,9).reshape(3,3)
print(f"Square matrix: {arr_1}")
print(f"Transpose matrix: {arr_1.T}")


# ------------------------
# Transpose using function
# ------------------------

arr_2=np.arange(0,6).reshape(3,2)
print(f"Simple: {arr_2}")
print(f"Transpose: {np.transpose(arr_2)}")