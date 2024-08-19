# Question in the sortInRange.png
# Test cases in the ppa_2-not graded.zip
from runTestCases import runTestCases
def sortInRange(L,r):
    dict = {}
    for i in range(r):
        dict[i] = 0
    for element in L:
        dict[element] = dict[element] + 1
    left = 0
    right = 0
    for i in range(r):
        right = right + dict[i]
        L[left:right] = [i]*dict[i]
        left = right



li = [2, 0, 1, 1, 2, 3, 0, 2, 1, 0, 2, 3, 1, 2,]
nu = 4
sortInRange(li,nu)
print(li)