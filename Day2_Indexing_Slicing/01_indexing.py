import numpy as np

# -----------------------------
# positive and negative Indexing 
# -----------------------------

arrays=np.array([10,20,40,50])
print(arrays[3]) #positive
print(arrays[-1]) #negative

#positive indexing [0,1,2,3]
#negative indexing [-4,-3,-2,-1]

# -------
# Slicing
# -------

#[start : stop : step]

arrays= np.array([1,2,0,3,6,7,9]) #its counting starting from 1
print(arrays[3:5:2])
#reverse slicing
arrays=np.array([2,4,6,8,9,10])
print(arrays[::-1]) #wil reverse the whole array
print(arrays[-4]) #should print 6

# -------------
# View and copy
# -------------
arrays= np.array([2,4,5,1,3,6])
view_slic= arrays[1:4] #4,5,1

view_slic[0]=22 # would change 4 into 22
print(view_slic)

#all we have to do here is to store our slicing in a variable.


copy_arr= arrays.copy()
copy_arr[4]=100 #will replace 3 into 100
print(copy_arr)


# -------------
# Broadcasting
# -------------
#assigning single value to multiple element
arrays=np.array([1,2,4,6,9,1,0,1])
arrays[2:5]=99 #change 4,6,9 to 99
print(arrays)


# ----------------
# boolean indexing
# ----------------

arr=np.array([2,3,5,7,9,11])
mask=arr>7
print(arr[mask])


# ----------------
# fancy indexing
# ----------------

arr = np.array([
    [10,20],
    [30,40],
    [50,60],
    [70,80],
    [90,100],
    [200,0],
    [4.0,10]
])

result=arr[[5,6]]
print(result)

# -------------------
# & and | combination
# -------------------

arr= np.array([0,1,2,4,4,5,6,7,8,9])

a=arr[(arr>2)& (arr<8)]
print(a)

a= arr[(arr%2==0) & (arr<7)]
print(a)