import time
import datetime

def start():
    clock = "decimal"

    try:
        while True:
            t = datetime.datetime.now()
            hour, minute, second = t.strftime("%T").split(":")
            if clock=="binary":
                hour = bin(int(hour))[2:].zfill(5)
                minute = bin(int(minute))[2:].zfill(5)
                second = bin(int(second))[2:].zfill(5)
            if clock=="hexadecimal":
                hour = hex(int(hour))[2:].zfill(2).upper()
                minute = hex(int(minute))[2:].zfill(2).upper()
                second = hex(int(second))[2:].zfill(2).upper()
            print(hour + ":" + minute + ":" + second) 
            time.sleep(1)
    except:
        pass

if(__name__ == "__main__"):
    start()
