# Create a 2D array of 10 students × 5 subject scores. Use boolean indexing to find students with average > 70, use slicing to extract specific subject columns, replace failing scores (<40) with 40.


import numpy as np
scores = np.array([
    [85, 90, 78, 88, 92],   
    [45, 52, 60, 48, 55],   
    [90, 92, 88, 91, 87],   
    [65, 70, 72, 68, 74],   
    [88, 84, 79, 85, 90],   
    [35, 40, 38, 45, 42],   
    [72, 75, 70, 68, 74],   
    [55, 60, 58, 62, 57],   
    [77, 79, 39, 26, 78],   
    [94, 96, 62, 75, 97]    
])


avg= np.mean(scores, axis=1)
mask=scores[avg>70]
print(f'student with average > 70 : {mask}')


slic_score=scores[:, 1:3]
print(f'Extracted Specific columns: {slic_score}')

scores[scores<40]=40
print(f'Changing marks which are less than 40: {scores}')