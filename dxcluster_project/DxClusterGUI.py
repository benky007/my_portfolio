import sqlite3
import telnetlib
from tkinter import *
from tkinter import ttk, messagebox

con = sqlite3.connect('c:\\users\\ben\\klog\\logbook.dat')
cur = con.cursor()
filename = "Recent.txt"
settings_file = "Settings.txt"
idfile = open(settings_file, "r")
if len(idfile.read()) > 1:
    server = idfile.split(" ")[0]
    port = idfile.split(" ")[1]
    call = idfile.split(" ")[2]
    locator = idfile.split(" ")[3]
server = None
port = None
call = None
locator = None

root = Tk()
root.configure(background="white")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.geometry("750x240")

style = ttk.Style()
style.theme_use('default')
style.theme_settings('default', {
    "TButton": {
        "configure": {"background": '#232323', "font": ('Segoe UI', 14), "foreground": 'white'},
        "map": {"background": [('active', '#ff0000')]
                }},
    "TLabel": {
        "configure": {"background": 'grey', "font": ('Segoe UI', 14), "foreground": 'black'},
        "map": {
        }},
    "TEntry": {
        "configure": {"background": 'white', "font": ('Segoe UI', 14), "foreground": 'black'},
        "map": {
        }},
    "TFrame": {
        "configure": {"background": 'grey', "font": ('Segoe UI', 14)},
        "map": {"background": [('active', 'grey')
                               ]
                }},
    "TNotebook": {
        "configure": {"background": 'grey', "font": ('Segoe UI', 14), "foreground": 'white'},
        "map": {"background": [('active', 'grey')
                               ]
                }},
    "TNotebook.Tab": {
        "configure": {"background": 'grey', "font": ('Segoe UI', 14), "foreground": 'white'},
        "map": {"background": [('active', 'grey')
                               ]
                }}
})

frame = Frame(root, background="grey")
frame.pack(fill=BOTH)
title1 = ttk.Frame(frame)
title1.pack(side=TOP, fill=X)
title = ttk.Label(title1, text="My Dx Cluster")
title.pack(side=TOP)
tabControl = ttk.Notebook(frame)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Cluster Info')
tabControl.add(tab2, text='Cluster Settings')
tabControl.add(tab3, text='Manual Cluster')
tabControl.pack(expand=True, side=TOP, fill=BOTH)

tab1_title = ttk.Label(tab1, text="Live Cluster Info Of Dx Spots Done", style="TLabel")
tab1_title.pack(side=TOP, expand=True)
tab1_scrollbar = Scrollbar(tab1)
tab1_scrollbar.pack(side=RIGHT, fill=Y)
tab1_myList = Listbox(tab1, yscrollcommand=tab1_scrollbar.set, width=130,
                      font=('Dejavu', 8, 'bold'), fg='white', bg='grey')
tab1_myList.pack(side=LEFT, fill=BOTH)
tab1_scrollbar.config(command=tab1_myList.yview)

tab2_frame = ttk.Frame(tab2)
tab2_frame.pack(side=TOP, expand=True, fill=BOTH)
tab2_top_frame = ttk.Frame(tab2_frame)
tab2_top_frame.pack(side=TOP, expand=True, fill=BOTH)
tab2_bottom_frame = ttk.Frame(tab2_frame)
tab2_bottom_frame.pack(side=TOP, expand=True, fill=BOTH)
tab2_server_label = ttk.Label(tab2_top_frame, text="Spider Server Name")
tab2_server_label.pack(side=LEFT, anchor=N, expand=True)
tab2_server_entry = ttk.Entry(tab2_top_frame, text="")
tab2_server_entry.pack(side=LEFT, anchor=N, expand=True)
tab2_port_label = ttk.Label(tab2_top_frame, text="Spider Server Port")
tab2_port_label.pack(side=LEFT, anchor=N, expand=True)
tab2_port_entry = ttk.Entry(tab2_top_frame, text="")
tab2_port_entry.pack(side=LEFT, anchor=N, expand=True)
tab2_call_label = ttk.Label(tab2_bottom_frame, text="Callsign")
tab2_call_label.pack(side=LEFT, anchor=S, expand=True)
tab2_call_entry = ttk.Entry(tab2_bottom_frame, text="")
tab2_call_entry.pack(side=LEFT, anchor=S, expand=True)
tab2_Locator_label = ttk.Label(tab2_bottom_frame, text="Grid Locator")
tab2_Locator_label.pack(side=LEFT, anchor=S, expand=True)
tab2_Locator_entry = ttk.Entry(tab2_bottom_frame, text="")
tab2_Locator_entry.pack(side=LEFT, anchor=S, expand=True)


def get():
    settings = []
    server = str(tab2_server_entry.get())
    port = int(tab2_port_entry.get())
    call = str(tab2_call_entry.get())
    locator = str(tab2_Locator_entry.get())
    settings.append(server)
    settings.append(port)
    settings.append(call)
    settings.append(locator)
    idfile = open(settings_file, "w")
    for i in range(len(settings)):
        idfile.write(str(settings[i]) + "")


tab2_button = ttk.Button(tab2_frame, text="confirm", command=get)
tab2_button.pack(expand=True)

bands = {"40M": 970, "20M": 1000, "30M": 1000, "80M": 500, "17M": 1000, "15M": 1000, "12M": 500, "10M": 500, "2M": 50}
HOST = server
PORT = port
user = call
password = ''


def cluster_settings(cursor, HOST, PORT, user, locator):
    if HOST is None or PORT is None or user is None or locator is None:
        idfile = open(settings_file, "r")
        settingsFile = str(idfile.read())
        if len(settingsFile) > 0:
            settingsList = settingsFile.split(" ")
            HOST = settingsList[0]
            PORT = settingsList[1]
            user = settingsList[2]
            locator = settingsList[3]
        else:
            cursor.execute("SELECT my_gridsquare, station_callsign FROM log ORDER BY qso_date DESC")
            test = cursor.fetchall()
            HOST = "gb7nhr.dynu.net"
            PORT = 7300
            user = test[0][1]
            locator = test[0][0]
            messagebox.showerror("ERROR",
                                 "You need to go to the settings tab and fill the entry boxes and press the button")


def startup_store_last_logid(cursor):
    cursor.execute("SELECT id FROM log ORDER BY id DESC")
    last = str(cursor.fetchone()[0])
    idfile = open(filename, "w")
    idfile.write(last)
    idfile.close()


def get_logs(cursor):
    idfile = open(filename, "r")
    rec = idfile.read()
    cursor.execute(
        f"SELECT log.id, call, freq, band.name AS band, comment FROM log, band WHERE band.id = log.bandid AND log.id > {rec}")
    logs = cursor.fetchall()
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
    if comment is None:
        comment = "TNX fer QSO 73 de Ben 73"
    if call is not None and call != '' and freq is not None and freq != '':

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

        return f"dx {call} {freq} {comment}"
    else:
        return f"Error: Call={call}, Freq={freq}, Comment={comment}"


def process_logs(HOST, PORT, user, password, logs, bands):
    dx = []
    for log in logs:
        # print(log)
        logid = log[0]
        band = str(log[3])
        band_distance = int(bands[band])
        distance = call_distance(HOST, PORT, user, password, log)
        print("Distance:", distance, "Band distance:", band_distance)
        if distance >= band_distance:
            # print("Here!!!")
            dx.insert(spot_dx(HOST, PORT, user, password, log))
        idfile = open(filename, "w")
        # print("logid:", str(logid))
        if str(logid) != '':
            idfile.write(str(logid))
        idfile.close()
    return dx


startup_store_last_logid(cur)


def run():
    logs = get_logs(cur)
    if logs:
        # print(logs)
        if HOST is None or PORT is None or user is None or locator is None:
            cluster_settings(cursor, HOST, PORT, user, locator)
        else:
            process_logs(HOST, PORT, user, password, logs, bands)
    root.after(1000, run)


root.after(1000, run)
root.mainloop()
