# def fun(s):
#     p = 0
#     s = s.lower()
#     for i in range(len(s)):
#         print(s[i], s[:i])
#         if s[i] not in s[:i]:
#             print("+1")
#             p += 1
#     return p

# strin = 'abcabc'
# prin(fun(strin))

# # print(strin[:3])

# def f(n):
#     print("*************************************")
#     s = 0
#     for i in range(2,n):
#         print(i,"-")
#         if n % i == 0 and i % 2 == 1:
#             s = s + 1
#             print(i, "-----")
#     return(s)

# print(f(60) - f(59))

# x = 1
# while True:
#     if x % 5 == 0:
#         break
#     print(x, end = ' ')
#     x += 1

# class Person:
#     def __init__(self,name):
#         self.name = name
#     def say_hi(self):
#         print('Hello, ', self.name)

# p = Person('Good morning')
# p.say_hi()

# a = [1,2,3]
# try:
#     print("Second elelment = %d" %(a[1]))
#     print("Fourth elelment = %d" %(a[3]))
# except:
#     print('An error occured')

def special3Bad(L):
    try:
        if L[0] % L[1] == 0 and L[1] !=0:
            if L[0] / (L[1] ** 2 - L[2]) == 0:
                return True
        return False
    except ZeroDivisionError:
        
        print('ZeroDivisonError', 'for', L)
    except:
        print('Some other exception occurred')
    else:
        print('No exception occurred')




def isSymmetricBad(L: list):
    initia = str(L)
    try:
        while len(L)> 0:
            if L.pop(0) != L.pop(-1):
                return False
        return True
    except IndexError:
        print('IndexError', initia)
    except:
        print('Some other exception occurred')
    else:
        print('No exception occurred')


arrays = [
   [1, 2, 3, 4, 3, 2, 1],
    [2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1],
    [8],
    [2, 4, 6]
]
# for i in range(len(arrays)):
#     print(isSymmetricBad(arrays[i]))
# print(isSymmetricBad([2,4,6]))

def gcd(m,n):
    print(m,n)
    (a,b) = (max(m,n), min(m,n))
    if a % b == 0:
        return (b)
    else:
        return (gcd(b,a % b))
# print(gcd(24,130))

class Enrollment:
    count = 0
    
    def __init__(self,n,c):
        self.name = n
        self.course = c
        Enrollment.count += 1
    
    def display(self):
        print(self.name)
        print(self.course)
        
myarr = []

myarr.append((2,3))
myarr.append((1,3))
myarr.append((3,3))
# print(myarr)

# print(2 == 2 == 2)
print(sorted([11,10,1, 2, 3, 4, 3, 2, 1]))
