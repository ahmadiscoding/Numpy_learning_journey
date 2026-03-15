import numpy as np

# X----------------------------------X
# .reshape(2,3,2)
# for three dimension
# (2 , 3 , 2)
#  ↑   ↑   ↑
#  |   |   |
#  |   |   └── columns
#  |   └────── rows
#  └────────── layers (matrices)
# X---------------------------------X

# ------------
#  .reshape()
# ------------
#changes the dimension of the array

arr=np.arange(0,6).reshape(2,3) #2D array
print(f"Reshape: {arr}")

arr_1=np.arange(0,6).reshape(-1,2)
print(f"auto rows: {arr_1}")
arr_1=np.arange(0,6).reshape(2,-1)  
## "-1" will calc automatically the rows/columns
print(f"auto columns: {arr_1}")



print("x----------------------x")

# ------------
#  .ravel()
# ------------
#.ravel(): If you modify its → original array also changes

arr=np.arange(1,7).reshape(2,3)
r=arr.ravel()
# arr[0]=999 #it will change the first row
#arr[0,0]=999 ##it will change only one element
r[0]= 999
print(f"Before change: {arr}") 
print(f"After change: {r}")
print("x----------------------x")

# ------------
#  .flatten()
# ------------
#.flatten(): If you modify it → original array stays same, it creates a new array.
arr1=np.arange(0,6).reshape(2,3)
c=arr1.flatten()
c[0]=555
print(f"Before change: {arr1}") 
print(f"After change: {c}")




