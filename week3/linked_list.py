class Node:
    def __init__(self, v = None):
        self.value = v
        self.next = None
        return
    
    def isEmpty(self):
        if self.value == None:
            return True
        else:
            return False
    
    def appendR(self, v):
        # Recursive
        if self.isEmpty():
            self.value = v
        elif self.next == None:
            self.next = Node(v)
        else:
            self.next.append(v)
        return
    
    def append(self, v):
        # iterative
        if self.isEmpty():
            self.value = v
            return
        
        temp = self
        while temp.next != None:
            temp = temp.next
        
        temp.next = Node(v)
        return
    
    def insert(self, v):
        if self.isEmpty():
            self.value = v
            return
        newNode = Node(v)
        # swap the values
        self.value, newNode.value = newNode.value, self.value
        # switch links
        self.next, newNode.next = newNode, self.next
        return
    
    def deleteR(self, v):
        # Recursive
        if self.isEmpty():
            return
        
        if self.value == v:
            self.value = None

            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if self.next != None:
                self.next.delete(v)
                if self.next.value == None:
                    self.next = None
        return 
    
    def delete(self, v):
        if self.isEmpty():
            return
        temp = self
        while temp.next != None:
            if temp.value == v:
                temp.value = temp.next.value
                temp.next = temp.next.next
                break
            else:
                temp = temp.next
        

    