import numpy as np
# print(np.__version__)  just to check if its working or not

# -------------------------
# Creating a basic array
# -------------------------

arrays= np.array([2,4,6,8])
print(f"Original array: {arrays}")
arrays*=2
print(f"after multiplying: {arrays}")

# -------------------------
# Practice 1 - another array
# -------------------------

array2 =np.array([10,20,30,40])
array2+=5
print(f"Addition: {array2}")

# -------------------------
# Practice 2 - another array
# -------------------------

array3=np.array([2,4,5,6])
print(type(array3))


# -------------------------
# Practice 3 - adding 2 arrays
# -------------------------

array_1=np.array([2,4,6,8])
array_2=np.array([1,3,5,7])
print(f"adding two arrays: {array_1+array_2}")


# -------------------------
# Practice 4 - * and + 2 arrays
# -------------------------

a1=np.array([5,3,2,4])
a1=(a1*2)+3   #multipulication and addition
print(a1)