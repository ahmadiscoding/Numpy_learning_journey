import numpy as np

# # ---------------
# #  zero dimension
# # ---------------

arrays=np.array('A')
print(f"Zero dimension: {arrays}")
print(arrays.ndim)
print(arrays.shape)

# # ---------------
# #  One dimension
# # ---------------

arrays= np.array(['A', 'B', 'C'])
print(f"One dimension: {arrays}")
print(arrays.ndim)
print(arrays.shape)

# # ---------------
# #  Two dimension
# # ---------------

arrays= np.array([
                ['A','B','C'],
                ['D','E','F']
                  ])
print(f"Two dimension: {arrays}")
print(arrays.ndim)
print(arrays.shape)

# # ---------------
# #  Three dimension
# # ---------------

arrays= np.array([
                [[2,4,5],[1,2,3],[6,7,8]]
                ])
print(f"Three dimension: {arrays}")
print(arrays.ndim)
print(arrays.shape)

# Another one:

arrays= np.array([
    [['A','B','C'],['D','E','F'], ['G','H','I']],
    [['J','K','L'],['M','N','O'], ['P','Q','R']],
    [['S','T','U'],['V','W','X'], ['Y','Z','_']]
    ])

print(f"Three dimension: {arrays}")
print(arrays.ndim)
print(arrays.shape)