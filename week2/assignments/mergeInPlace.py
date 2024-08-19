    # A = [1, 2, 3, 4, 13, 15]
    # B = [5, 6, 9, 10]
def mergeInPlace(A, B):
    
    m = len(A)
    n = len(B)
    
    for i in range(m):
        if A[i]> B[0]:
            # swap A[i] with B[0]
            temp = A[i]
            A[i]=B[0]
            B[0]=temp
            
            j = 0
            while(j < n-1 and B[j]>B[j+1]):
                temp = B[j]
                B[j] = B[j+1]
                B[j+1] = temp
                j += 1
                
    return (A,B)           

            
            
    
    
def main():
    A = [2, 4, 6, 9, 13, 15]
    B = [1, 3, 5, 10]
    mergeInPlace(A,B)
    print(A,B)
    
main()
