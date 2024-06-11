# L = [[10.5], '10.5', 10.5, (10.5)]

# i = 0

# while i < 4:
#     try:
#         item = int(L[i])
#         print('No Error')
#     except TypeError:
#         print('Error1')
#     except ValueError:
#         print('Error2')
#     i += 1

# print(int((10.5)))

def sq(n):
    return (n** .5) == int(n) ** .5

print(sq(5))
print(5.0 == 5)