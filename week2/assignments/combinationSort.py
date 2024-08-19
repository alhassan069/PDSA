# Question in the combinationSort.png file
# Test cases in the grpa_1.zip file
import string
def combinationSort(L):
    Dict = {s:[] for s in string.ascii_lowercase}
    
    
    for i in range(len(L)):
       char = L[i][0]
       Dict[char].append(L[i])
    
    L = []
    for key in Dict.keys():
        for s in Dict[key]:
            L.append(s)

    L1 = L.copy()

    
    i = 1
    # As there can be no more than 100 strings with same initial character.
    # Using insertion sort within group.
    while i<len(L):
        right = i
        while(right>0 and L[right][0] == L[right-1][0] and int(L[right-1][1:])<int(L[right][1:])):
            (L[right], L[right-1]) = (L[right-1], L[right])
            right -= 1
        i += 1
  
    return (L1, L)






def main():
    inputList = ["d34", "g54", "d12", "b87", "g1", "c65", "g40", "g5", "d77"]
    print(combinationSort(inputList))

main()