import ipaddr
class IP4Address():
    def __init__(self,hoctet,mask):
        self.hoctet = hoctet
        self.mask = mask

    def getNetwork(self):
        network = self.hoctet
        return network
    
    def getMask(self):
        ipaddress = ""
        for ip in self.hoctet: 
            ipaddress += "." + str(ip)
        ipwithmask = ipaddress[1:] + "/" + str(self.mask)
        mask = ipaddr.IPv4Network(ipwithmask)
        return mask.netmask
   
    def getAddress(self):
        ipaddress = ""
        for ip in self.hoctet:
            ipaddress += "." + str(ip)
        ipaddress = ipaddress[1:]
        return ipaddress   
   
    def __str__(self):
        mask = self.getMask()
        return ("Network Portion: " + str(self.getNetwork()) + "\nMask:" + str(self.getMask()) + "\nIP Address: " + self.getAddress())

myobj = IP4Address([10,0,1,7],24)
print(myobj)

