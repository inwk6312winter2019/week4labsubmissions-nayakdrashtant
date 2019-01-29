import string
def stringoperation():
    myfile = open("58782-0.txt","r")
    punct = string.punctuation
    histo = dict()
    counter = 0
    listofwords = []
    for my in myfile:
        my = my.strip()
        for c in punct:
           my = my.replace(c,"")
        my = my.lower()
        lis = my.split()
        for li in lis:
            listofwords.append(li)
    for lists in listofwords:
        if lists not in histo:
            histo[lists] = 1
        else:
            histo[lists] += 1
    print("Words usage:",histo)
    print("Total no of words:",len(listofwords))

stringoperation()
