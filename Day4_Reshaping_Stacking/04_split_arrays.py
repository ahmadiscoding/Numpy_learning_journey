import numpy as np


# ----------
# np.split()
# ----------
arr= np.arange(1,9)
print(np.split(arr,4))


# -----------
# np.vsplit()
# -----------

arr_1= np.arange(0,8).reshape(2,4)
print(arr_1)
print(np.vsplit(arr_1,2))

# -----------
# np.hsplit()
# -----------

arr_2= np.arange(0,8).reshape(4,2)
print(arr_2)
print(np.vsplit(arr_2,4))

