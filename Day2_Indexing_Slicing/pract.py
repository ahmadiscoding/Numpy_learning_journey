import numpy as np

arr = np.array([3, 7, 2, 9, 12, 5, 8])
mask=arr>6
print(arr[mask])

print("x-----------------x")

arr = np.array([3, 7, 2, 9, 12, 5, 8])
even=arr%2==0
print(arr[even])

print("x-----------------x")

odd=arr%2!=0
print(arr[odd])

print("x-----------------x")

#replacing number less than 5 with zero
arr[arr<5]=0
print(arr)

print("x-----------------x")
# Print all values greater than 30.
arr = np.array([
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
])
a=arr>30
print(arr[a])

print("x-----------------x")
# Using the same array, print rows where the first column is greater than 20.

#[rows, column]
result= arr[:,0]>20
print(arr[result])
print("x-----------------x")


arr = np.array([5, 10, 15, 20, 25, 30])
result= (arr>10) & (arr<25)
print(arr[result])

print("x-----------------x")
# Replace all negative numbers with 0.
arr = np.array([-4, 7, -2, 9, -1, 3])
arr[arr<0]=0
print(arr)

print("x-----------------x")

arr = np.array([
    [5, 12, 7],
    [18, 3, 21],
    [9, 14, 6]
])


result= arr[arr%3 == 0]
print(result)

print("x-----------------x")
#slicing
arr = np.array([10,20,30,40,50,60])

print(arr[1:4])

print(arr[:3])

print(arr[-3:])

print("x-----------------x")
arr = np.array([1,2,3,4,5,6,7,8])


print(arr[::2])

print("x-----------------x")

arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
#1st row
result= arr[0,:]
print(result)

#2nd column
result_2=arr[:,1]
print(result_2)

result_3=arr[0:2,:]
print(result_3)

result_4=arr[1:,1:]
print(result_4)


# Print middle column but only from row 1 onward.
result_5=arr[1:,1]
print(result_5)