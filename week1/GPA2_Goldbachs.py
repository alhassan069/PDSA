import math

def isPrime(num):
    if num <2:
        return False
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def Goldbach(n):
    ans = []
    upper_limit = n
    i = 0
    while i< upper_limit:
        if isPrime(i) and isPrime(n-i):
            ans.append((i, n-i))
            upper_limit = n-i
        i += 1
    return ans
                
n=int(input())
print(sorted(Goldbach(n)))