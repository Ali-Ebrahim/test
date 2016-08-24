#coding utf-8
#-----------------------------------------------------------------------------
from datetime import datetime
import time
import socket
import whois
import sys
import random
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def sahlaoui():
    print (""" \t
                     |---------------------------------------------------------------|
                     |              pirimipirimi[@]gmail[dot]com                     |
                     |               08/2016      zipscan v0.0                       |
                     |                  فلسطين ليست للبيع                            |
                     |---------------------------------------------------------------- \t""" )
sahlaoui1= sahlaoui()

TARGET =input("\t entre le site (like :www.google.com ): \t")
b="."
e="www"
if b and e in TARGET:
                print ("\t****************information de site *******************\t")
                time.sleep(2)
                print ("\tsite ---------------------->\t" , TARGET)
else:
                print ("""\tdon't make me crazy \t""")
                TARGET.close()
                
#socket

#جلب إبي
c = socket.gethostbyname(TARGET)
print ("\tIP -------------------------> {}\t".format(c))
#اسم الجهاز
d = socket.gethostname()
print ("\thostname -------------------------> {}\t".format(d))
#whois
e = whois.whois(TARGET)
print ("\temails --------------------------> {}\t".format(e.get("\temails\t")))
print ("\t name ----------------------------> {}\t".format(e.get("\tname\t")))
print ("\t domain_name ---------------------> {}\t".format(e.get("\tdomain_name\t")))
print ("\t address -------------------------> {}\t".format(e.get("\taddress\t")))
print ("\t country -------------------------> {}\t".format(e.get("\tcountry\t")))
print ("\t zipcode -------------------------> {}\t".format(e.get("\tzipcode\t")))
print ("\t referral_url --------------------> {}\t".format(e.get("\treferral_url\t")))
print ("\t city ----------------------------> {}\t".format(e.get("\tcity\t")))
print ("\t****************information de site **********************\t")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#scan port
print ("""\t--------------------------------------------------------------------------------------------------------------
            --------------------------------------------------------------------------------------------------------------
            ----------------------------- SCANING YOUR PORT --------------------------------------------------------------
            ----------------------------------------------------------------------SCANING YOUR PORT-----------------------
            --------------------SCANING YOUR PORT-------------------------------------------------------------------------
            --------------------------------------------------------------------------------------------------------------\t""")
PORT_FER=input("\t Entre the START port number : \t")
PORT_SEG=input("\t Entre the LAST port number :\t")
T1=  datetime.now()
try:
    for port in range(PORT_FER,PORT_SEG):
         sock=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
         res=sock.connect_ex(TARGET , port)
         if res==0:
           print ("\t port open  \t" , port ,"\t---\t" ,TARGET)
           sys.exit()
except :
           print ("\tsorry we have problem with your site\t")
T2=  datetime.now()
total=T2-T1
print("\tscaning complete in \t" , total)





































