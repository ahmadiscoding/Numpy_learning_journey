import numpy as np
inp= np.array(list(map(int, input("Enter you marks WITH SPACE:").split())))
print(inp)
print(np.percentile(inp, 50))


# EXPLANATION:
# input()
# Takes input as one string.

# .split()
# Splits the string by spaces.

# map(int, ...)
# map() applies a function to every element.
# Here it converts each string → integer.

# list(...)
# Converts the map object into a list.

# Then NumPy converts it to array


# take numbers from user → convert to integers → store in list