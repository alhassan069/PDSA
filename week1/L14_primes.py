# checking for a prime number
# Approach 1

def factors(n):
    fl = [] #factor list
    for i in range(1, n+1):
        if (n%i) == 0 :
            fl.append(i)
    return (fl)

def prime(n):
    return (factors(n) == [1,n])


# approach 2

def prime2(n):
    result = True
    for i in range(2,n):
        if(n%i) == 0:
            result = False
            break
    return result

# approach 3 same but using while loop

def prime3(n):
    (result,i) = (True,2)
    while(result and (i<n)):
        if (n%i) == 0:
            result = False
        i = i + 1
    return result

# approach 4 using sqrt

import math

def prime4(n):
    (result,i) = (True, 2)
    while (result and (i<math.sqrt(n))):
        if(n%i) == 0:
            result = False
        i = i + 1
    return result


# list all primes upto m

def primesupto(m):
    pl = [] # prime list
    for i in range(1, m+1):
        if prime(i):
            pl.append(i)
    return pl


# list the first m primes

def firstprimes(m):
    (count, i, pl) = (0,1,[]) #multiple assignments (pl is prime list)
    while(count<m):
        if prime(i):
            (count,pl) = (count + 1,pl+[i]) # pl+[i] is same as pl.append(i)
        i = i + 1
    return (pl)




def primediffs(n):
    lastprime = 2
    pd = {} # dictionary for prime differences
    for i in range(3, n+1):
        if prime4(i):
            d = i - lastprime
            lastprime = i
            if d in pd.keys():
                pd[d] = pd[d] + 1
            else:
                pd[d] = 1
    return (pd)

print(primediffs(420))