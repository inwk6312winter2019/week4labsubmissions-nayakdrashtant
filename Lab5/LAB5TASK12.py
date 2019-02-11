from netaddr import *
import pprint
import socket
class IP_Address():
    def __init__(self,ipadd=socket.gethostbyname(socket.gethostname())):
        self.ipadd = ipadd

    def __repr__(self):
        ip = IPNetwork(self.ipadd)
        print("============== Network Information ==============")
        print("Network:    " +  str(ip.network) +  "     " +  str(ip.network.bits()))
        print("BroadCast:  " + str(ip.broadcast) + "   " + str(ip.broadcast.bits()))
        print("First Host: " + str(ip[0]) + "     Last Host: " + str(ip[-1]))
        print("Total Host: " + str(len(ip)))

i = input("Enter IP address with netmask:")
myobj = IP_Address(i)    
myobj.__repr__()
