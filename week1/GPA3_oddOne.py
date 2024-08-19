def odd_one(L):
    data_types = {
        'int' : 0,
        'float': 0,
        'str': 0,
        'bool': 0 
    }
    for i in L:
        data_types[str(type(i).__name__)] += 1
    
    for j in data_types.keys():
        if data_types[j] == 1:
            return j
        
print(odd_one([2,13,16,4.5]))

# print(str(type(3).__name__))