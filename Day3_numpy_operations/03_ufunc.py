import numpy as np

## this include all the universal functions which are used in numpy.

arr= np.array([1,2,4,8,16,32,64])

print(f'{np.sqrt(arr)}\n')
print(f'{np.exp(arr)}\n')
print(f'{np.abs(arr)}\n')
print(f'{np.log10(arr)}\n')

print("x----------------x")


#-----------------
# Trigno functions
#-----------------

angles= np.array([0, np.pi/2, np.pi/4])

print(f'Sin theta: {np.sin(angles)}\n')
print(f'cos theta: {np.cos(angles)}\n')
print(f'tan theta: {np.tan(angles)}\n')


print("x----------------x")


#-------------------
# operation operator
#-------------------

arr_1=np.array([1,2,3,4])
arr_2= np.array([5,6,7,8])

print(np.maximum(arr_1,arr_2))
print(np.minimum(arr_1,arr_2))


print("x----------------x")



