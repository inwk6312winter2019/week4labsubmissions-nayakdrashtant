class Point():
    def __init__(self,x=10,y=11):
        self.x = x
        self.y = y
    def add(self):
        if isinstance(self.y,type):
            mynew = self.y(40,10)
            myold = Point()
            x = mynew.x + myold.x
            y = mynew.y + myold.y
            print("Class: Point new value are X:"+ str(x) + " Y:" + str(y))
        elif isinstance(self.y,tuple):
            check = self.y
            print("Tuple: Point new value are X:"+ str(check[0]) + " Y:" + str(check[1]))
        else:
            print("d",type(self.y))

myobj = Point(1,2)
newobj = Point(myobj,Point)
newobj.add()
s = 2,1,3
newob = Point(2, s)
newob.add()
