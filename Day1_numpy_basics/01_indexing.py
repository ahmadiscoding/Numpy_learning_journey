import numpy as np

#[layer , row , column]

# ---------------
#  Chain Indexing
# ---------------

arrays= np.array([
    [['A','B','C'],['D','E','F'], ['G','H','I']],
    [['J','K','L'],['M','N','O'], ['P','Q','R']],
    [['S','T','U'],['V','W','X'], ['Y','Z','_']]
    ])

print(f"Chain indexing: {arrays[1][1][1]}")


# -------------------------
#  Multidimension Indexing 
# -------------------------

arrays= np.array([
    [['A','B','C'],['D','E','F'], ['G','H','I']],
    [['J','K','L'],['M','N','O'], ['P','Q','R']],
    [['S','T','U'],['V','W','X'], ['Y','Z','_']]
    ])

print(f"Multi-dimension indexing: {arrays[1,1,1]}")

# ---------------
# Indexing  Pract
# ---------------

arrays= np.array([
    [['A','B','C'],['D','E','F'], ['G','H','I']],
    [['J','K','L'],['M','N','O'], ['P','Q','R']],
    [['S','T','U'],['V','W','X'], ['Y','Z','_']]
    ])

#going to form a word using concatenation

word1=arrays[1,1,0]+ arrays[2,0,2]+ arrays[0,2,1]+ arrays[0,0,0]+arrays[1,1,0]+ arrays[1,1,0]+ arrays[0,0,0]+ arrays[0,1,0]
word2= arrays[0,0,0]+ arrays[0,2,1]+ arrays[1,1,0]+ arrays[0,0,0] + arrays[0,1,0]
print(word1+' '+word2)