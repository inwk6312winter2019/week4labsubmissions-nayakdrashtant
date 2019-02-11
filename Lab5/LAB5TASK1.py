class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self):
        return int(self.x) - int(self.y)

x= input("Enter value for x:")
y =input("Enter value for y:")
myobj = Point(x,y)
print("Distance: ",myobj.distance())
