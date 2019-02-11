class Point():
    def __init__(self,x=1,y=2):
        self.x = x
        self.y = y
    def __str__(self):
        return "str method:" + str(self.x) + " " + str(self.y)

    def add(self):
        print("Addtion is:" + str(int(self.x) + int(self.y)))

myobj = Point(1,2)
print(myobj)
myobj.add()
