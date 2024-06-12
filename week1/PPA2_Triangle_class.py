class Triangle:
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
        
    def Is_valid(self):
        if (self.a+self.b) > self.c and (self.a + self.c) > self.b and (self.b + self.c )> self.a:
            return 'Valid'
        else:
            return 'Invalid'
    
    def Side_Classification(self):
        if self.Is_valid() == 'Invalid':
            return 'Invalid'
        elif self.a == self.b == self.c :
            return 'Equilateral'
        elif (self.a == self.b) or (self.a == self.c) or (self.b == self.c):
            return 'Isosceles'
        else:
            return 'Scalene'
    
    def Angle_Classification(self):
        if self.Is_valid() == 'Invalid':
            return 'Invalid'
        sortedArray = sorted([self.a,self.b,self.c])
        (a,b,c) = (sortedArray[0],sortedArray[1], sortedArray[2])
        
        if (a**2) + (b**2) > (c**2):
            return 'Acute'
        elif (a**2) + (b**2) == (c**2):
            return 'Right'
        elif (a**2) + (b**2) < (c**2):
            return 'Obtuse'
    
    def Area(self):
        if self.Is_valid() == 'Invalid':
            return 'Invalid'
        (a,b,c) = (self.a, self.b, self.c)
        s = (self.a + self.b + self.c)
        calculation1 = s * (s - a) * (s - b) * (s - c)
        ans = calculation1 ** .5
        return ans
    
        
        
        
            
    



a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())