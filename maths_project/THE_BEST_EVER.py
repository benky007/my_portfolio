import time
import os
def start(string):
    for i in range(79):
        string = string[78:]+string[:78]
        print('-'*80, '\n'*2, string,  '\n'*2, '-'*79)
        time.sleep(0.05)
        os.system('clear')
def end(string):
    string = string[51:]+string[:51]
    print('-'*80, '\n'*2, string, '\n'*2, '-'*79) 
    
