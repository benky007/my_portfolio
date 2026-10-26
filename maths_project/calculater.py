import math
import time
import pi

def start():

    print("Hello and welcome to my calculator")
    q = input("Do you like the calculator so far?")
    
    while 1:
        try:
            a = float(input("Pick your first number for the calculater "))
            b = float(input("Pick your second number for the calculater "))
            break
        except:
            print("put a number next time")
        
    o = input("pick your operation ")
    
    if o == "divide":
        d = a/b
        time.sleep(1)
        print("Answer = ", d)
        
    elif o == "times":
        t = a*b
        time.sleep(1)
        print("Answer = ", t)
        
    elif o =="add":
        add = a+b
        time.sleep(1)
        print("Answer = ", add)
        
    elif o == "minus":
        m = a-b
        time.sleep(1)
        print("Answer = ", m)
        
    elif o == "to the power of":
        p = a**b
        time.sleep(1)
        print("Answer = ", p)

    elif o == "route":
        r = a//b
        time.sleep(1)
        print("Answer = ", r)

    elif o == "pi":
        while 1:
            try:                
                R = str(input("Do you want it rounded or not?"))
                break
            except:
                print("put yes or no next time")
        if R == "yes":
            p = math.pi
            while 1:
                try:
                    hi = int(input("Specify the amount of decimal places to round it to between 1-40"))
                    break
                except:
                    print("Between 1-40")
                    
            for u in range(40):
                if hi == u:
                    hi = round(float((math.pi[hi])))
            
            print("Okay solving...")
            time.sleep(1)
            print("Answer = ", hi)
                
        else:
            print("Jack the best")
                
if __name__ == '__main__':
    start()
