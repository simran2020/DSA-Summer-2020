from graphics import *

win=GraphWin('Rectangles',800,800)
win.setCoords(0,0,100,100)
a = win.getMouse()
a1 = a.getX()
a2 = a.getY()
p1= Point(a1,a2)
#print(a)
b = win.getMouse() 
b1 = b.getX()
b2 = b.getY()
p2= Point(b1,b2)
#print(b)
def drawRect():
        if a1<b1 and a2<b2:
            bL = a
            tR = b
            print(bL)
            print(tR)
            rec=Rectangle(bL,tR)
            rec.draw(win)
            return
        elif a1<b1 and a2>b2:
            tR = b
            bL = a
            print(bL)
            print(tR)
            rec=Rectangle(tR,bL)
            rec.draw(win) 
        else:
            pass
    
drawRect()

def Area():
        length = abs(a1-b1)
        breadth = abs(a2-b2)
        area = length*breadth
        print("The area of this rectangle is",round(area),"units squared")
Area()

def Perimeter():
        length = abs(a1-b1)
        breadth = abs(a2-b2)
        perimeter=(2*length)+(2*breadth)
        print("The perimeter of the rectangle is",round(perimeter), "units")
Perimeter()


