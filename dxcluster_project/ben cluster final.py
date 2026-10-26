import sqlite3
import time
import telnetlib

con = sqlite3.connect('c:\\users\\ben\\klog\\logbook.dat')
co = con.cursor()
loop = True
band1 ={"40M":1000, "20M":1000, "30M":1000, "80M":500, "17M":1000, "15M":1000, "12M":750, "10M":750, "2M":50}
HOST = "gb7nhr.dynu.net"
PORT = 7300
user = 'M7BAW'
password = ''
dxcall = []

def startup(c):
    c.execute("SELECT id FROM log ORDER BY id DESC")
    last = str(c.fetchone()[0])
    text = open("Recent.txt", "w")
    text.write(last)
    text.close()

def check(c):
    text = open("Recent.txt", "r")
    rec = text.read()
    c.execute(f"SELECT log.id, call, freq, band.name AS band, comment FROM log, band WHERE band.id = log.bandid AND log.id > {rec}")
    recent = c.fetchall()
    text.close()
    return recent

def execute(recent1, band2, Dis, dxCall):
    if recent1 == []:
        id_next = ''
        print("DX is done")
    else:
        #id_next = recent1[0][0]
        for i in recent1:
            recid = i[0]
            call = i[1]
            freq = i[2]
            band = str(i[3])
            comment = i[4]
            test = int(band2[band])
            print(recid, call, freq, band, comment, test)
            Dis = int(Dis[i])
            if Dis >= test:
                #print("dx", call, freq, "TNX fer QSO 73 de Ben 73")
                dxCall.append((call, freq, comment))
            next1 = open("Recent.txt", "w")
            if str(recid) != '':
                next1.write(str(recid))
            next1.close()
        return dxCall
            

def distance(HOST1, PORT1, user1, password1, Recent1):
    Head = []
    if Recent1 == []:
        id_next = ''
        print("DX is done")
    else:
        #id_next = Recent1[0][0]
        for i in Recent1:
            Call = i[1]

            '''
            tn = telnetlib.Telnet(host=HOST, port=PORT)

            tn.read_until(b"login: ")
            tn.write(user.encode('ascii') + b"\n")
            if password:
                tn.read_until(b"Password: ")
                tn.write(password.encode('ascii') + b"\n")

            tn.read_until(b"dxspider >")
            tn.write(f"sh/head Call\n")

            #print(tn.read_all().decode('ascii'))
            head = tn.read_until(b"dxspider >").decode('ascii')
            tn.write(b"bye\n")
            '''

            head = '''sh/head HA1RB
            HA Hungary-HA: 103 degs - dist: 996 mi, 1603 km Reciprocal heading: 299 degs
            M7BAW de GB7NHR 29-Jan-2021 2021Z dxspider >'''
            head = head.split(" mi")
            head = head[0]
            head = head.split("dist: ")
            head = head[1]
            #print(head[1], "miles")
            Head.append(head)
        return Head

def dx(Check):
    for g in check:
        Call1 = g[0]
        Freq = g[1]
        Comment = g[2]
        '''
        tn = telnetlib.Telnet(host=HOST, port=PORT)

        tn.read_until(b"login: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")

        tn.read_until(b"dxspider >")
        tn.write(f"dx {Call1} {Freq} {Comment} \n".encode('ascii'))

        #print(tn.read_all().decode('ascii'))
        #head = tn.read_until(b"dxspider >").decode('ascii')
        tn.write(b"bye\n")
        '''
        print(f"dx {Call1} {Freq} {comment}")
    
startup(co)
while loop == True:
    result = check(co)
    if result == []:
        print("again")
    else:
        dis = distance(HOST, PORT, user, password, result)
        print(dis)
        check1 = execute(result, band1, dis, dxcall)
        if len(check1) > 0:
            dx(check1)
    time.sleep(30)
