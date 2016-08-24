#!python#
import socket
import time
host = raw_input('enter url site : ')
if ('http://') in host:
	host = host.replace('http://','')
	ip_host = socket.gethostbyname(host)
cmd = raw_input('write commandes')

if cmd == ('PA'):
        starting_time = time.time()
        starting_time
        try:
                for port in  [21,22,23,25,53,69,80,109,110,123,137,138,139,143,156,389,443,546,547,995,993,2086,2087,2082,2083,3306,8443,10000]:
                        # xrange(0, MAX_PORT):
                        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
                        s.settimeout(15) 
                        try:
                                s.connect((ip_host, port))
                                print('port {0:5} : open'.format(port))
                        except socket.timeout, e:
                                print('port {0:5} : filtered ({1})'.format(port, e))
                        except socket.error, e:                                
                                print('port {0:5} : close    ({1})'.format(port, e))
                                s.close()
                                time.sleep(1)

        except KeyboardInterrupt:
                exit()
