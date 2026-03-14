import numpy as np

# aggregate functions basically summarize the data and return a single value

arr= np.array([[1,2,3,4,5], 
               [6,7,8,9,10]])

#to sum everything:
print(np.sum(arr))
#to find the mean or averaga:
print(np.mean(arr))
#to find the min or max value:
print(np.min(arr))
print(np.max(arr))
#to find the location of the min or max value:
print(np.argmin(arr))
print(np.argmax(arr))
#to find the standard deviation:
print(np.std(arr))
#to find the variance:
print(np.var(arr))


#to sum arr elements in columns and rows:
print(np.sum(arr, axis=0)) ## for column
print(np.sum(arr, axis=1)) ## for rows


#-----------
# np.where()
#-----------


# if condition true → first value
# else → second value
# .where(condition, x, y)

arr= np.array([[[50,85,66,70,99],
               [26,77,89,46,100]],
               [[66, 55, 42, 43, 77],
                [88,99,77,100,96]]])

a= np.where(arr>65, "pass", "fail")
print(a)


#-----------
# np.clip()
#-----------
# Restricts values within a range.

arr= np.array([[50,85,66,70,99],
               [26,77,89,46,100]])

#.clip(array, values<, value>)

# values < 50 → become 50
# values > 85 → become 85
b=np.clip(arr, 50, 85)
print(b)



#-------------------------
# round(), ceil(), floor()
#-------------------------


arr= np.array([50.2, 0.85, 66.7, 70.9, 99.1])
print(f'{np.round(arr)}\n')
print(f'{np.ceil(arr)}\n')
print(f'{np.floor(arr)}\n')

