import numpy as np


# Compare shapes from right to left:
#broadcasting is valid only if:
# both dimensions are same 
# OR
#any of the dimension is 1



#Valid broadcasting example
arr1= np.array([[1,2,3,4,5,6,7,8,9,10]])
arr2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(arr1.shape)
print(arr2.shape)

print(arr1 * arr2)

#InValid broadcasting example
array_1= np.array([[1,2,3,4],[5,6,7,8]])
array_2=np.array([[1],[2],[3],[4]])

print(array_1.shape)
print(array_2.shape)
# here (2,4) and (4,1) means 1 vs 4 and 2 vs 4 here one condition is true but in 2nd one 2 vs 4 its not correct so its invalid and will give an ERROR. ---> ValueError: operands could not be broadcast together with shapes (2,4) (4,1)
# print(array_1 * array_2)



#---------------------
# Scalar Broadcasting
#---------------------

array=np.array([1,2,3,4])

print(array * 3)
print(array + 100)