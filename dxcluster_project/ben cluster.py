import sqlite3
import time
import telnetlib

con = sqlite3.connect('c:\\users\\ben\\klog\\logbook.dat')
cur = con.cursor()
filename = "Recent.txt"
bands = {"40M": 970, "20M": 1000, "30M": 1000, "80M": 500, "17M": 1000, "15M": 1000, "12M": 500, "10M": 500, "2M": 50}
HOST = "gb7nhr.dynu.net"
PORT = 7300
user = '2E0WGT'
password = ''


def startup_store_last_logid(cur):
    cur.execute("SELECT id FROM log ORDER BY id DESC")
    last = str(cur.fetchone()[0])
    idfile = open(filename, "w")
    idfile.write(last)
    idfile.close()


def get_logs(cur):
    idfile = open(filename, "r")
    rec = idfile.read()
    cur.execute(
        f"SELECT log.id, call, freq, band.name AS band, comment FROM log, band WHERE band.id = log.bandid AND log.id > {rec}")
    logs = cur.fetchall()
    idfile.close()
    return logs


def call_distance(HOST, PORT, user, password, log):
    call = log[1]

    tn = telnetlib.Telnet(host=HOST, port=PORT)

    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.read_until(b"dxspider >", timeout=2)
    tn.write(f"sh/head {call}\n".encode('ascii'))

    distance = tn.read_until(b"dxspider >").decode('ascii')
    tn.write(b"bye\n")

    '''
    distance = sh/head HA1RB
    HA Hungary-HA: 103 degs - dist: 996 mi, 1603 km Reciprocal heading: 299 degs
    M7BAW de GB7NHR 29-Jan-2021 2021Z dxspider >
    '''
    distance = distance.split(" mi")
    distance = distance[0]
    distance = distance.split("dist: ")
    distance = int(distance[1])
    return distance


def spot_dx(HOST, PORT, user, password, log):
    call = log[1]
    freq = log[2]
    comment = log[4]
    if comment == None:
        comment = "TNX fer QSO 73 de Ben 73"
    if call != None and call != '' and freq != None and freq != '':

        tn = telnetlib.Telnet(host=HOST, port=PORT)

        tn.read_until(b"login: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")

        tn.read_until(b"dxspider >", timeout=2)
        tn.write(f"dx {call} {freq} {comment}\n".encode('ascii'))

        tn.read_until(b"dxspider >", timeout=2)
        tn.write(b"bye\n")

        print(f"dx {call} {freq} {comment}")
    else:
        print(f"Error: Call={call}, Freq={freq}, Comment={comment}")


def process_logs(HOST, PORT, user, password, logs, bands):
    for log in logs:
        # print(log)
        logid = log[0]
        band = str(log[3])
        band_distance = int(bands[band])
        distance = call_distance(HOST, PORT, user, password, log)
        print("Distance:", distance, "Band distance:", band_distance)
        if distance >= band_distance:
            # print("Here!!!")
            spot_dx(HOST, PORT, user, password, log)
        idfile = open(filename, "w")
        # print("logid:", str(logid))
        if str(logid) != '':
            idfile.write(str(logid))
        idfile.close()


startup_store_last_logid(cur)
while True:
    logs = get_logs(cur)
    if logs:
        # print(logs)
        process_logs(HOST, PORT, user, password, logs, bands)
    time.sleep(10)
