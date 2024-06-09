## ABSTRACT DATATYPE
# - stores some information
# - designated functions to manipulate the information
# - for instance, stack: last in, first- out, push(), pop()
# 
## Seperate the (private) implementation from the (public) specification
# 
## CLASS
# - template for a data type
# - how data is stored
# - how public functions manipulate data
# 
## OBJECT 
# - concrete instance of template

## SPECIAL FUNCTIONS
# __init(self) -> initializes internal values
# __str__() -> converts object to string and invoked by print()
# __add__() -> adds two points and invoked by +
# __mult__() -> invoked by *
# __lt__() -> invoked by <
# __ge__() -> invoked by >=



# EXAMPLE -> 2D Points

class Point:
    def __init__(self, a=0,b=0):  # this function initializes internal values the first parameter is always self
        self.x = a
        self.y = b
    
    def translate(self, deltaX, deltaY):
        self.x += deltaX
        self.y += deltaY
    
    def odistance(self):
        import math         
        return math.sqrt( (self.x * self.x) + (self.y * self.y) )
    
    def __str__(self):  # converts object to string and invoked by print()
        return (
            '(' + str(self.x) + ',' + str(self.y) + ')'
        )
    
    def __add__(self, p): # adds two points and invoked by +
        return (Point(self.x + p.x, self.y + p.y))
        
oldp = Point(5,5)    
newp = Point(3,5)

print(newp)
print(newp.odistance())
newp.translate(1,1)

print(newp)

latestp = newp.__add__(oldp)

anotherp = newp + oldp

print(latestp)
print(anotherp)


