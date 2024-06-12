import math

def isPrime(num):
    if num <2:
        return False
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def Twin_Primes(n,m):
    ans = []
    lastPrime = 2
    for i in range(n,m+1):
        if isPrime(i) == True:
            if (i - lastPrime) == 2:
                ans.append((lastPrime,i))
            lastPrime = i
    return ans
    
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))