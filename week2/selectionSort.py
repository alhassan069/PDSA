def SelectionSort(L):
    n = len(L)
    if n <= 1: # if there is only one element or no element
        return L
    for i in range(n):  # loop through the list
        minimum_position = i # let the current position be the minimum position
        for j in range(i+1, n): # then loop from i to end of the list (n)
            if L[j] < L[minimum_position]: # if the element at j is less than element at minimum position
                minimum_position = j            #  change the minimum position to j
        (L[i], L[minimum_position]) = (L[minimum_position], L[i]) # swap the two elements
    return L

def main():
    arr = [1,-66,3,654,33,4,2,62,754,51,0,9]
    print(SelectionSort(arr))

main()