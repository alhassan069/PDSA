def merge(A,B):
    (m,n) = (len(A),len(B))
    (C,i,j,k) = ([],0,0,0)
    while (k<m+n):
        if i==m:        # if A is empty
            C.extend(B[j:])     #add rest of B to c
            k = k + (n-j)       # change the index of k to 
        elif j==n:
            C.extend(A[i:])
            k = k + (m - i)
        elif A[i] < B[j]:
            C.append(A[i])
            i = i + 1
            k = k + 1
        else:
            C.append(B[j])
            j = j + 1
            k = k + 1
    return C

def mergeSort(L):
    n = len(L)
    if n <= 1:
        return L
    left = mergeSort(L[:n//2])
    right = mergeSort(L[n//2:])
    
    merged_and_sorted = merge(left,right)
    return merged_and_sorted

def main():
    arr = [1,-66,3,654,33,4,2,62,754,51,0,9]
    print(mergeSort(arr))

main()