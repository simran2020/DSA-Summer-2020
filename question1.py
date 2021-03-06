import array as arr
import random as rd
# Circular array implementation using probabilistic insertion and removal
#by Jason Christopher Apaw Nkansah

class Deque:
    
    def __init__(self):
        self.deque = arr.array('i',[])
        self.ft = 0
        self.rr = 0
        self.itemCount = 0

#This function fills up the array by half
    def fillHalf(self):
        for i in range(10):
            num=rd.randint(1,100)
            self.deque.append(num)
            self.itemCount +=1 

    def dequeSize(self):
        return "The size of the Deque is",  self.itemCount

    def dequeCapacity(self):
        if Deque.isEmpty(self):
            return "The Deque is empty"
        elif self.itemCount == 20:
            return "The Deque is full"
        else:
            return "There are values in the deque"
        
    def isEmpty(self):
         if self.itemCount == 0:
            return "The deque is empty"
         else:
            return "there are values in the deque"
        
    def displayDeque(self):
        return self.deque
    
    def addTofront(self):
        if self.itemCount == 20:
            return "Cannot add value: Deque is full"
        else:
            self.deque.insert(self.ft, rd.randint(1,100))
            self.itemCount +=1
            self.ft = 0
            print( "value added to the frontend successfully")
            return Deque.displayDeque(self)
#a limit of twenty was given to the arrays. after 20, no more values can be added
#you cannot remove from an empty array either
    def addToback(self):
        if self.itemCount == 20:
            return "Cannot add value: Deque is full"
        else:
            self.deque.insert(self.itemCount, rd.randint(1,100))
            self.itemCount +=1
            print("value added to the backend successfully")
            return Deque.displayDeque(self)

    def removeFront(self):
        if self.itemCount == 0:
            return "Cannot remove value: The deque is empty"
        else:
            self.deque.pop(0)
            self.itemCount -=1
            print("value removed from the frontend successfully")
            return Deque.displayDeque(self)
        
    def removeBack(self):
        if self.itemCount == 0:
            return "Cannot remove value: The deque is empty"
        else:
            self.deque.pop(-1)
            self.itemCount -=1
            self.rr -=1
            print("value removed from the backend successfully")
            return Deque.displayDeque(self)
        
    #this function creates a new array when the class begins      
    def getDeque(self):
        Deque.fillHalf(self)
        return self.deque
        return Deque.displayDeque(self)

    #This fucntion represents the first set of probailities 
    def probA(self):
        p = round(rd.random(),2)
        print(p)
        
        if 0<p and p<=0.1:
            print( Deque.addTofront(self))
            return Deque.dequeSize(self)
        
        elif 0.1<p and p<=0.3:
            print( Deque.removeFront(self))
            print(Deque.isEmpty(self))
            return Deque.dequeSize(self)
        
        elif 0.3<p and p<=0.4:
            print( Deque.addToback(self))
            return Deque.dequeSize(self)
        
        elif 0.4<p and p<=1.0:
            print( Deque.removeBack(self))
            print(Deque.isEmpty(self))
            return Deque.dequeSize(self)
        else:
            pass
       
    #This fucntion represents the second set of probailities   
    def probB(self):
        p = round(rd.random(),2)
        print(p)
        if 0<p and p<=0.1:
            print( Deque.addTofront(self))
            return Deque.dequeSize(self)
        elif 0.1<p and p<=0.7:
            print( Deque.removeFront(self))
            print(Deque.isEmpty(self))
            return Deque.dequeSize(self)
        elif 0.7<p and p<=0.8:
            print( Deque.addToback(self))
            return Deque.dequeSize(self)
        elif 0.8<p and p<=1.0:
            print( Deque.removeBack(self))
            print(Deque.isEmpty(self))
            return Deque.dequeSize(self)
        else:
            pass


myDeque = Deque()
print(myDeque.getDeque())
        
print("testing using first probability set")
print("")

myDeque.probA()
myDeque.probA()
myDeque.probA()
myDeque.probA()
myDeque.probA()
print("testing using second probability set")
print("")
myDeque.probB()
myDeque.probB()
myDeque.probB()
myDeque.probB()
myDeque.probB()

