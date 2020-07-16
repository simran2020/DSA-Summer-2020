import random as rd

def DotProduct(N):
    ListA = []
    ListB = []
    for i in range (N):
        valA = rd.randint(1,1000)
        ListA.append(valA)
        valB = rd.randint(1,1000)
        ListB.append(valB)
    print(ListA)
    print(ListB)
    ans =sum([x*y for x,y in zip(ListA,ListB)])
 
    print("the dot product for these two lists is", ans)
    return 

DotProduct(10)
DotProduct(100)
