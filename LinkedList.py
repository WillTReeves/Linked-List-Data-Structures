class Node:
    def __init__(self,value):
        self.item = value
        self.next = None
    
    def __str__(self):
        return str(self.item)
    
    def __repr(self):
        return self.__str__()
    
    def set_value(self,new_value):
        self.item = new_value
    
    def count(self):
        if self.next is None:
            return 1 
        else:
            return 1 + self.next.count()

class linkedList:
    def __init__(self):
        self.head = None
        self.size = 0 

    def __repr__(self):
        return self.__str__()

    def __str__ (self):
        description = '['
        current = self.head
        if current is not None:
            while current.next is not None:
                description += str(current.item) + ", "
                current= current.next
            description += str(current.item)
        return description + "]"   

    def __iter__(self):
      return iterate(self)

    def isEmpty(self):
        return self.head == None    
    
    def chop(self):
        if self.isEmpty():
            pass
        else:
            self.head = self.head.next   

    def index(self,index):
        count = 0 
        current = self.head
        if current.next is not None:
            while count != index:
                current = current.next
                count += 1 
        return current

    def append(self,value):
        if self.head == None:
            self.head = Node(value)
        else :
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)
    
    def copy(self):
        current = self.head
        b = linkedList()
        b.append(current.item)
        if self.getsize() != 0:
            while current.next is not None:
                current = current.next
                b.append(current.item)
        return b 
    
    def copyconvert(self):
        current = self.head
        copy = []
        copy.append(current.item)
        if self.getsize() != 0:
            while current.next is not None:
                current = current.next
                copy.append(current.item)
        return copy
    
    def pop(self):
        current = self.head
        if self.getsize() != 0:
            while (current.next).next is not None:
                current = current.next
            item = current.next 
            current.next = None
            return item

    def popp(self,index):
        current = self.index(index-1)
        nextone = self.index(index)
        item = nextone
        current.next = nextone.next
        return item

    def insert(self,value,index):
        current = self.index(index-1)
        after = self.index(index)
        item = Node(value)
        current.next = item
        item.next = after
        
    def indexassingment(self, index, assignment):
        current = self.index(index)
        current.set_value(assignment)        

    def getsize(self):
        if self.head is None:
            return 0
        else:
            return self.head.count()

    def reverse(self):
        b = self.copy()
        c = linkedList()
        current = self.head
        while current is not None: 
            item = b.pop()
            c.append(item)
        return c 



    

class iterate:
    def __init__(self,windowlist):
        self.windowlist = windowlist
        self.current = windowlist.head

    def __next__(self):
        if self.current is not None:
            temp = self.current.item
            self.current = self.current.next
            return temp
        else:
            raise StopIteration


