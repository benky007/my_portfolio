import time

binary = 0
hexadecimal = 0
decimal = 1

def binary():
    binary = 1
    decimal = 0
    hexadecimal = 0

def decimal():
    binary = 0
    decimal = 1
    hexadecimal = 0

def hexadecimal():
    binary = 0
    decimal = 0
    hexadecimal = 1

def start():
    while True:
        hour = int(time.strftime("%H"))
        min = int(time.strftime("%M"))
        sec = int(time.strftime("%S"))
        bin_hour = bin(hour)
        bin_min = bin(min)
        bin_sec = bin(sec)
        hex_hour = hex(hour)
        hex_min = hex(min)
        hex_sec = hex(sec)
        if binary == 1:
            print(bin_hour, ":", bin_min, ":", bin_sec)
            time.sleep(1)
        elif hexadecimal == 1:
            print(hex_hour, ":", hex_min, ":", hex_sec)
            time.sleep(1)
        else:
            print(hour, ":", min, ":", sec)
            time.sleep(1)

if __name__ == '__main__':
    start()
