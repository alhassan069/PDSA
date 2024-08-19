# Question is at sortedAndRotated.png file
# Test cases is at grpa_2.zip
# https://neetcode.io/problems/find-target-in-rotated-sorted-array

from runTestCases import runTestCases

def findLargest(L):
    n = len(L)
    left = 0
    right = n-1
    curr_largest = float("-inf")
    
    if n == 1 or L[left]<L[right]:
        return [L[right]]

    
    while left<=right:
        if L[left] < L[right]:
            curr_largest = max(curr_largest,L[right])
            break
        
        mid = (left + right) // 2
        curr_largest = max(curr_largest, L[mid])
        
        if L[mid] > L[left]:
            left = mid + 1
        else:
            right = mid - 1
                 
    return [curr_largest]
    
    
            
    
    

runTestCases(findLargest,"grpa_2.zip")