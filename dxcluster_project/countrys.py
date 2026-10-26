import telnetlib
import sqlite3

con = sqlite3.connect('c:\\users\\ben\\klog\\logbook.dat')
cur = con.cursor()
cutted = []
logs = []

'''
cur.execute(SELECT entity.name, COUNT(entity.name) AS Qty FROM entity, log 
WHERE log.dxcc = entity.dxcc AND (log.eqsl_qsl_rcvd = 'Y' OR lotw_qsl_rcvd = 'Y')
GROUP BY entity.name)
'''
'''
print("Version 1 all entirys in order of name\n\n\n\n\n")
cur.execute(SELECT entity.name, COUNT(entity.name) AS Qty, log.eqsl_qsl_rcvd AS Eqsl, log.lotw_qsl_rcvd AS Lotw
FROM entity, log WHERE log.dxcc = entity.dxcc
GROUP BY entity.name)
countrys = cur.fetchall()
for i in range(len(countrys)):
    print(countrys[i][0], countrys[i][1])
print("Version 2 all entirys in order of name and number from highest to lowest\n\n\n\n\n")
cur.execute(SELECT entity.name, COUNT(entity.name) AS Qty
FROM entity, log WHERE log.dxcc = entity.dxcc
GROUP BY entity.name
ORDER BY COUNT(entity.name) DESC)
countrys = cur.fetchall()
for i in range(len(countrys)):
    print(countrys[i][0], countrys[i][1])
print("Version 3 all entirys in order of name and number from lowest to highest\n\n\n\n\n")
cur.execute(SELECT entity.name, COUNT(entity.name) AS Qty
FROM entity, log WHERE log.dxcc = entity.dxcc
GROUP BY entity.name
ORDER BY COUNT(entity.name))
countrys = cur.fetchall()
for i in range(len(countrys)):
    print(countrys[i][0], countrys[i][1])
'''
print("Version 4 all entirys in order of name that i havent got\\n\n\n\n\n")
cur.execute('''SELECT name FROM (SELECT entity.name, COUNT(log.dxcc) AS Qty
FROM entity LEFT JOIN log ON entity.dxcc = log.dxcc GROUP BY entity.name ORDER BY COUNT(log.dxcc))
WHERE Qty = 0''')
countrys = cur.fetchall()
spacer = "    "
for i in range(len(countrys)):
    #print(countrys[i][0])
    logs.append(countrys[i][0])
    print(i)
    for a in range(1):
        spacer.join(logs)
        print(logs)

