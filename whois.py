import httplib
url = raw_input('write you target to get info : ')
if ('://') in url :
    go = url.replace('https://','')
    go = url.replace('http://','')
else :
    go = url

conn = httplib.HTTPConnection("check-host.net")
send = conn.request("GET",'/ip-info?host='+go)
r1 = conn.getresponse()
print r1.status, r1.reason
data = r1.read()
opener = open('index.html','w')
index = opener.write(data)

conn.close()
