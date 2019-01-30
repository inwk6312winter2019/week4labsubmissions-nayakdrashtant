import string
import math
from collections import Counter
import matplotlib.pyplot as pyplot

def findlog(param):
    return int(math.log(int(param)))

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    mydict=dict()
    for a in aux:
        key = a[1]
        value = a[0]
        mydict[key] = value
    return mydict

def rankdict(dicto):
    mydict = sortFreqDict(dicto)
    noofitems = len(mydict) 
#    for keys in mydict:
    #    mydict["A"].append(keys)
    return mydict

def plots(scale,xvalue,yvalue):
    pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title("title string")
    pyplot.xlabel("label string")
    pyplot.ylabel("label, string")
    pyplot.plot(xvalue, yvalue)
    pyplot.show()

def stringoperation():
    myfile = open("listofwords.txt","r")
    punct = string.punctuation
    histo = dict()
    counter = 0
    listofwords = []
    newlist = []
    newwords = []
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

    print(histo)
  #  l = sorted(histo.items(), key=lambda item: item[1],reverse=True)
  #  noofitems = len(l)
 #   for key, value in l:
 #       r = noofitems
#        noofitems -= 1
#        l[r].append(key)
  #  print(l)
   # counts = Counter([list(d.keys())[0] for keys, d in histo])
#    data_sorted = sorted(histo,key=lambda item: counts[list(item.keys())[0]], # function to lookup freq from counts
 #   reverse=True # descending order
  #  )
   # print(counts)

    sort = rankdict(histo)
    plots(10,120,10)
#    print(sort)

stringoperation()


