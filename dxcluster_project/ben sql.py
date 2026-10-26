import sqlite3
import time

con = sqlite3.connect('c:\\users\\ben\\klog\\logbook.dat')
co = con.cursor()
loop = True
band1 = {"40M": 1000, "20M": 1000, "30M": 1000, "80M": 500, "17M": 1000, "15M": 1000, "12M": 750, "10M": 750, "2M": 50}
dis = 750


def check(c):
    c.execute("SELECT id, call FROM log")
    call = c.fetchall()
    c.execute("SELECT id, freq FROM log")
    freq = c.fetchall()
    text = open("Recent.txt", "r")
    rec = text.read()
    c.execute(
        f"SELECT log.id, call, freq, band.name AS band, comment FROM log, band WHERE band.id = log.bandid WHERE log.id > {rec}")
    recent = c.fetchall()
    text.close()
    return recent


def execute(recent1, band2):
    if recent1 == []:
        id_next = ''
        print("DX is done")
    else:
        # id_next = recent1[0][0]
        for i in recent1:
            recid = i[0]
            call = i[1]
            freq = i[2]
            band = i[3]
            comment = i[4]
            print("dx", call, freq, "TNX fer QSO 73 de Ben 73")
            next1 = open("Recent.txt", "w")
            if str(recid) != '':
                next1.write(str(recid))
            next1.close()


while loop == True:
    result = check(co)
    if result == []:
        print("again")
    else:
        execute(result, band1)
    time.sleep(30)
