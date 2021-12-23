import random
from names import names
from phonenumbers import PhoneNum
from Stopwatch import stopwatch
from LinkedList import linkedList
sizes = [10000]
numbers =[]
def main():
    for N in sizes:
        Animal = stopwatch()  
        Animal.start()
        sample = []
        genpopLlist  = linkedList()
        genpoplist = []
        genpopdict = {}
        for x in range(N):
            name = names()
            num = PhoneNum()
            pair = (name,num)
            genpopLlist.append(pair)
            genpoplist.append(pair)
            genpopdict[name] = num
            if x % 20 == 0:
                sample.append(name)
            if x % 50 == 0:
                Falsename = names()
                sample.append(Falsename)
        y = random.sample(sample,len(sample))
        time = Animal.stop()
        print(time)
        lookupdict(y, genpopdict, N)
        lookupLlist(y, genpopLlist, N)
        lookuplist(y, genpoplist, N)

        

def lookupdict(sample, dicts, N):
    C = stopwatch()
    C.start()
    for x in sample:
        numbers.append(dicts.get(x))
    c = C.stop()
    print("for a sample size of {} and dictionary size of {} it took {}".format(len(sample), N, c))
            
def lookupLlist(sample, Llist, N):
    A = stopwatch()
    A.start()
    for x in sample:
        for y in Llist:
            if x == y[0]:
                numbers.append(y[1])
                break
    a = A.stop()
    print("for a sample size of {} and linkedlist size of {} it took {}".format(len(sample), N, a))

def lookuplist(sample, lists, N):
    B = stopwatch()
    B.start()
    for x in sample:
        for y in lists:
            if x == y[0]:
                numbers.append(y[1])
                break
    b = B.stop()
    print("for a sample size of {} and list size of {} it took {}".format(len(sample), N, b))
    print(" ")


    




