class Kangaroo():
    def __init__(self):
        self.pouch_contents = []
 
    def put_in_pouch(self,ob):
        self.pouch_contents.append(ob)

    def __str__(self):
        string = ""
        for i in self.pouch_contents:
            string += str(i)
        return string


kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch(roo)
print(kanga)
