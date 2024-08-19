# Question in the binarySearchIndexAndComparisons.png file
# Test cases in the ppa_1-not graded.zip file
# using while loop and two pointers
def binarySearchIndexAndComparisons(L,k):
    n = len(L)
    left = 0
    right = n-1
    elementsCompared = 0
    found = False
    while (left<=right):
        mid = (left + right)//2
        
        if L[mid]==k:
            # print("eq")
            elementsCompared = elementsCompared + 1
            found = True
            break
        elif k < L[mid]:
            # print("lt",mid)
            elementsCompared = elementsCompared + 1
            right = mid - 1
        else:
            # print("gt",{"left":left,"mid":mid,"right":right})
            elementsCompared = elementsCompared + 1
            left = mid + 1
    
    return (found,elementsCompared)
    
def binarySearchIndexAndComparisonsRecursion(L,k):
    if L == []:
        return False
    m = len(L)//2
    if k == L[m]:
        return True
    if k<L[m]:
        return binarySearchIndexAndComparisonsRecursion(L[:m],k)
    else:
        return binarySearchIndexAndComparisonsRecursion(L[m:],k)

def main():
    L = [2, 6, 8, 11, 17, 23, 33, 44, 46, 50, 65]
    karr = [23,100,11]
    for i in range(len(karr)):
        print(binarySearchIndexAndComparisons(L,karr[i]))
        
main()