from time import gmtime, strftime

def print_time():
    print("Current Time is:",strftime("%H:%M:%S", gmtime()))

print_time()    

