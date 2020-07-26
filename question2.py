import random
from time import *


def binarySearch(arr, target):
    
    high = (len(arr) - 1)
    low = 0
    while low <= high and target >= arr[low] and target <= arr[high]:

        pos = int((low + high)/ 2)
        
        if arr[pos] == target:
            print("value found", pos)
        if arr[pos] < target:
            low = pos + 1;
        else:
            high = pos - 1;
    return "Your request is not in this sequence"

def interpolationSearch(arr, target):
    Low = 0
    High = (len(arr) - 1)
    while Low <= High and target >= arr[Low] and target <= arr[High]:
        POS = Low + int(((( arr[High] - arr[Low])) * ( target - arr[Low]))/float(High - Low))

        if arr[POS] == target:
            print("value found", POS)
        if arr[POS] < target:
            Low = POS + 1;
        else:
            High = POS - 1;            
    return "Your request is not in this sequence"

def compare():
    target = eval(input("what value are you searching for? "))

     
   # 100 values
    arr=[]
    for i in range(100):
        val = random.randint(1,32767)
        arr.append(val)
    arr.sort()
    #print (arr)

    import time
    startBS = int(round(time.time() ))
    binarySearch(arr, target)
    endBS = int(round(time.time()))
    print( "The time taken by the Binary Search was:", endBS-startBS)

    startIS =  int(round(time.time()))
    interpolationSearch(arr, target)
    endIS =  int(round(time.time() ))
    print ("The time taken by the Interpolation Search was:", endIS-startIS)

# 1000 values
    arr=[]
    for i in range(1000):
        val = random.randint(1,32767)
        arr.append(val)
    arr.sort()
    print (arr)


    import time
    startBS = int(round(time.time() ))
    binarySearch(arr, target)
    endBS = int(round(time.time() ))
    print( "The time taken by the Binary Search was:", endBS-startBS)

    startIS =  int(round(time.time()))
    interpolationSearch(arr, target)
    endIS =  int(round(time.time() ))
    print ("The time taken by the Interpolation Search was:", endIS-startIS)

# 5000 values
    arr=[]
    for i in range(5000):
        val = random.randint(1,32767)
        arr.append(val)
    arr.sort()
    print (arr)

    import time
    startBS = int(round(time.time() ))
    binarySearch(arr, target)
    endBS = int(round(time.time() ))
    print( "The time taken by the Binary Search was:", endBS-startBS)

    startIS =  int(round(time.time() ))
    interpolationSearch(arr, target)
    endIS =  int(round(time.time() ))
    print ("The time taken by the Interpolation Search was:", endIS-startIS)



compare()
