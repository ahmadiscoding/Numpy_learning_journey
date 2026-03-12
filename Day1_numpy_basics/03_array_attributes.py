import numpy as np

# ------------
#  zero Arrays
# ------------

arrays=np.zeros((3,3))

print(f"3x3 zero matrix: {arrays}")

## Another one

a=np.zeros((2,3))
print(f"2x3 zero matrix: {a}")

# ------------
#  one Arrays
# ------------

arrays= np.ones((3,3))
print(f"3x3 ones matrix: {arrays}")

# --------------
#  empty Arrays
# --------------

arrays= np.empty((2,3))

print(f"Printing garbage values: {arrays}")


# ------------
#  eye Arrays
# ------------

arrays=np.eye(3,3)
print(f"Diagonal matrix: {arrays}")



# ------------
#  arange Arrays
# ------------


#its like a range() which used in python

arrays= np.arange(0,10,2)  #[start, stop , step]
print(arrays)


# ------------
#  linspace Arrays
# ------------

arrays= np.linspace(0, 10, 5)   
#[start, stop, evenly_spaced_number_of_values]
print(arrays)



# -------------------------
#  common attributes Arrays
# -------------------------

arrays= np.array([[2,3,4],
                  [5,2,5]])
print(f"Number of rows and columns: {arrays.shape}")
print(f"data types: {arrays.dtype}")
print(f"dimension: {arrays.ndim}")
print(f"element in arrays: {arrays.size}")

# -------------------
#  Changing data_type
# -------------------
arrays=np.array([[0,128,255]], dtype=np.uint8)
print(arrays)

# --------------------
#  type_Casting Arrays
# --------------------

arrays=np.array([0.5, 1.7, 4.9 ])
print(arrays.astype(int))

