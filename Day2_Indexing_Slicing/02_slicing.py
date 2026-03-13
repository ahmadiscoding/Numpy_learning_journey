import numpy as np

# ----------
# 2D slicing
# ----------

arrays= np.array([[1,2,4,5,6,8],
                  [2,4,6,8,10,12], 
                  [0,1,2,3,4,6]
                  ])
a=arrays[0:2,1:3]
print(a)


