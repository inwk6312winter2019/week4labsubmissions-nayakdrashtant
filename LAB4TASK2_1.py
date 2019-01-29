import string
def stringoperation():
    myfile = open("58782-0.txt","r")
    punct = string.punctuation
    for my in myfile:
        my = my.strip()
        my = my.replace(" ","\n")
        for c in punct:
           my = my.replace(c,"")
        my = my.lower()
        print(my)
stringoperation()
