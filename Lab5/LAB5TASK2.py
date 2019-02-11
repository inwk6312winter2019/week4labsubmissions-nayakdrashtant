class Point():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

class Rectangle():
    corner = Point()
    x = corner.x
    y = corner.y
    def __init__(self,width=100,height=200,x=0,y=0):
     #   print(corner)
  #      corner = Point()
        self.width = width
        self.height = height
        self.x = x
        self.y = y

def find_center(Rectangle):
    myobj = Rectangle()
    centerCoord = (myobj.x+(myobj.width/2), myobj.y+(myobj.height/2))
    print("Center of circle:",centerCoord)

def move_rectangle(Argument,dx,dy):
    myobj = Argument()
    myobj.x = int(dx)
    myobj.y = int(dy)
    centerCoord = (myobj.x+(myobj.width/2), myobj.y+(myobj.height/2))
    print("Center of Rectangle after moving is:",centerCoord)

def new_rectangle(Argument,width,height):
    myobj = Argument()
    myobj.width = int(width)
    myobj.height = int(height)
    centerCoord = (myobj.x+(myobj.width/2), myobj.y+(myobj.height/2))
    print("Center of New Rectangle :",centerCoord)

find_center(Rectangle)
x = input("Enter X coordinates to move circle:")
y = input("Enter Y coordinates to move circle:")
w = input("Enter Width for new Rectangle:")
h = input("Enter Heigh for new Rectangle:")

move_rectangle(Rectangle,x,y)
new_rectangle(Rectangle,w,h)
