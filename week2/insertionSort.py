def insertionSort(L):
    n = len(L)
    if n<=1: # if there is only one element or none then just return the list as it is
        return L
    for i in range(n): # loop the list
        j = i   
        while (j>0 and L[j-1]>L[j]): # if the element right of i is lesser than itself, swap and continue till j>0
            (L[j],L[j-1]) = (L[j-1], L[j])
            j = j - 1
    return L


def main():
    arr = [1,-66,3,654,33,4,2,62,754,51,0,9]
    print(insertionSort(arr))

main()