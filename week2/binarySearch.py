def binarySearch(arr,target):
    left, right = 0, len(arr) - 1
    ans = -1
    while left <= right:
        middle_index = (left + right) // 2
        if arr[middle_index] == target:
            ans = middle_index
            break
        elif arr[middle_index] > target:
            right = middle_index - 1
        else:
            left = middle_index + 1
    return ans

lis = [-1, 2, 4, 5, 7,8, 10,100, 154]
print(binarySearch(lis,100))