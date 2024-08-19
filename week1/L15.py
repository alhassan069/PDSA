# simplifying the gcd 
# if d divides m and n, then d also divides (m-n)
# using recursion
# time complexity O(max(m,n))

def gcd(m,n):
    (a,b) = (max(m,n), min(m,n))
    if a%b == 0:
        return b
    else:
        return (gcd(b,a-b))
    
# Euclid's algorithm
# suppose n doesnot divide m
# then m = qn + r #quotient and reminer
# suppose d divides both m and n
# then m = ad, n = bd
# m = qn + r  -> ad = q(bd) + r
# r must be in the form of cd
# 
# EUCLID'S ALGORITHM
# if n divides m, gcd(m,n) = n
# otherwise compute gcd(n,m mod n) 

def gcd_optimized(m,n):
    (a,b) = (max(m,n), min(m,n))
    if a%b == 0:
        return b
    else:
        return gcd_optimized(b, a%b)




ans = int((405448323 * 435638250) / 3)
print(ans)