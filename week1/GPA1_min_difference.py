def find_Min_Difference(L,P):
    n  = len(L)
    L = sorted(L)
    left = 0
    right = P - 1
    minimum_difference = 2**29
    
    while(right<n):
        difference = L[right] - L[left]
        if difference < minimum_difference:
            minimum_difference = difference
        left += 1
        right += 1
    
    return minimum_difference
        
    

# L=eval(input().strip())
# P=int(input())
L = [1,2,3,-4,3,2,1,5,-6,7,8,9,10]
P = 6
print(find_Min_Difference(L,P))

