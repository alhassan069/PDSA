def gcd(m,n):
    # greatest_common_factor = 1
    for i in range(1, min(m,n)+ 1):
        if(m%i) == 0 and (n%i) == 0:
            greatest_common_factor = i
    return(greatest_common_factor)

print(gcd(420, 1024))