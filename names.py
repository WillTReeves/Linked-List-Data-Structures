import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'


# A name is the join of some random choices of alphabetic 
# letters, of length k, where k is itself a choice of a 
# number between parameters min and max, then capitalized.
class names:
    def __init__(self):
        self.first = self.name(3,8) 
        self.lastname = self.name(5,10)
    
    def name(self, min, max):
        return ( ''.join (
                    random.choices( alphabet, 
                                    k = random.randrange(min,max) ))
                ).capitalize()\
    
    def __str__(self):
        nam = self.first + " " + self.lastname
        return nam
    
    def __repr__(self):
        return self.__str__()


