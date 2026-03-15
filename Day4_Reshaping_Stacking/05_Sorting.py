import numpy as np

arr = np.array([45, 12, 78, 34, 23])

print("Original array:", arr)

# np.sort() → returns a new sorted array
sorted_arr = np.sort(arr)

print("Sorted using np.sort():", sorted_arr)

# arr.sort() → sorts the original array
arr.sort()

print("Sorted using arr.sort():", arr)


#-----------
# Along axis
#-----------
arr = np.array([[30,10,20],
                [90,50,70]])
print("\nSort axis=1 (row-wise):")
print(np.sort(arr, axis=1))

print("\nSort axis=0 (column-wise):")
print(np.sort(arr, axis=0))