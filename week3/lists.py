# zerolist = [0,0,0]

# zeromatrix = [zerolist,zerolist,zerolist]

# zeromatrix[1][1] = 1

# print(zeromatrix) #  [[0, 1, 0], [0, 1, 0], [0, 1, 0]] 


# zeromatrix = [ [0 for i in range(3) ] for j in range(3) ] #list comprehension

# zeromatrix[1][1] = 1

# print(zeromatrix) # [[0, 0, 0], [0, 1, 0], [0, 0, 0]]


import numpy as np

zeromatrix = np.zeros(shape=(3,3))
newarr = np.array([[0,1],[1,0]])

row2 = np.arange(5)



print(row2)
