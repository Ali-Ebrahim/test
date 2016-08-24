from datetime import datetime
import time
import socket
import whois
import sys
import random

Target =raw_input("\t entre le site (like :www.google.com ): \t")
if "://" in Target :
    Host = Target.replace('http://','')
    Host = Target.replace('https://','')
#socket

ip_host= socket.gethostbyname(Host)

print ("\tIP -------------------------> {}\t".format(ip_host))
#اسم الجهاز
Srv_name = socket.gethostname()
print ("\thostname -------------------------> {}\t".format(Srv_Name))
#whois
Who_site = whois.whois(Target)
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
         res=sock.connect_ex(Target , port)
         if res==0:
           print ("\t port open  \t" , port ,"\t---\t" ,Target)
           sys.exit()
except :
           print ("\tsorry we have problem with your site\t")
T2=  datetime.now()
total=T2-T1
print("\tscaning complete in \t" , total)





































