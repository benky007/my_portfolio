import time
import keyboard

run = True
while run:
    # print(time.strftime("%b %d %Y %H:%M:%S"))
    h = time.strftime("%H")
    m = time.strftime("%M")
    s = time.strftime("%S")
    bh = bin(int(h))[2:].zfill(8)
    bm = bin(int(m))[2:].zfill(8)
    bs = bin(int(s))[2:].zfill(8)
    hh = hex(int(h))[2:]
    hm = hex(int(m))[2:]
    hs = hex(int(s))[2:]
    oh = hex(int(h))[2:]
    om = oct(int(m))[2:]
    os = oct(int(s))[2:]
    print(h, m, s, sep=':')
    time.sleep(1)
