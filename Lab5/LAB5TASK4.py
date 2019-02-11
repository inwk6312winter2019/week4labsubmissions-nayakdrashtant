from time import gmtime, strftime
from datetime import datetime,timedelta
# print("Current Time is:",strftime("%H:%M:%S", gmtime()))

class Time():
    def __init__(self,t1,t2):
         self.t1 = t1
         self.t2 = t2

    def is_after(self):
         return self.t1 < self.t2

y = datetime.now() - timedelta(days=1)
z = datetime.now()
print(y)
print(z)
myobj = Time(z,y)
print(myobj.is_after())
