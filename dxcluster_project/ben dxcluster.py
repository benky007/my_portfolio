import telnetlib

HOST = "gb7nhr.dynu.net"
PORT = 7300
user = 'M7BAW'
password = ''
call = "HA1RB"

'''
tn = telnetlib.Telnet(host=HOST, port=PORT)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.read_until(b"dxspider >")
tn.write(f"sh/head {call}\n".encode('ascii'))

#print(tn.read_all().decode('ascii'))
head = tn.read_until(b"dxspider >").decode('ascii')
tn.write(b"bye\n")
print(head)
'''

head = '''sh/head HA1RB
HA Hungary-HA: 103 degs - dist: 996 mi, 1603 km Reciprocal heading: 299 degs
M7BAW de GB7NHR 29-Jan-2021 2021Z dxspider >'''
head = head.split(" mi")
head = head[0]
head = head.split("dist: ")
head = head[1]
#print(head[1], "miles")
if int(head) >= 1000:
    print("dx")
else:
    print("no")
