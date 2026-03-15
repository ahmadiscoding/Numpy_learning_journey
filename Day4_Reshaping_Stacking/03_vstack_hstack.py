import numpy as np

# vstack → vertical stacking ( adds rows)
# hstack → horizontal stacking (adds columns)

# ------
# arrays
# ------

a= np.array([1,2,3])
b= np.array([4,5,6])



# --------------
# Vertical Stack
# --------------

v=np.vstack((a,b))
print(f"Vertical stack: {v}")



# ----------------
# Horizontal Stack
# ----------------

h=np.hstack((a,b))
print(f"Horizontal stack: {h}")

# --------
# 2D Array
# --------

arr_1=np.array([[1,2,3],[4,5,6]])
arr_2=np.array([[7,8,9],[10,11,12]])

vv= np.vstack((arr_1,arr_2))
hh=np.hstack((arr_1, arr_2))
print(f"Vertical stack: {vv}")
print(f"Horizontal stack: {hh}")



# -------------
# Concatenation
# -------------
##This function joins arrays together along a specific axis.

arr1=np.array([[1,2,3],[4,5,6]])
arr2=np.array([[7,8,9],[10,11,12]])

# ----------------------------
# Concatenate axis = 0
# ----------------------------
# rows added:
print(np.concatenate((arr1,arr2), axis=0))


# ----------------------------
# Concatenate axis = 1
# ----------------------------
# columns added:
print(np.concatenate((arr1,arr2), axis=1))



# concatenate() is the general function.
# vstack() and hstack() are just convenient shortcuts.