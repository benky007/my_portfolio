import os
from THE_BEST_EVER import start, end
def start_up():
    timer = 0
    word = 'Bens Statement Converter'+' '*(79-24)
    while True:
        start(word)
        timer += 1
        if timer == 3:
            end(word)
            st = input('')
            if st == '\n':
                start(word)
            else:
                break
def title():
    word = 'Bens Statement Converter!'+' '*(79-25)
    end(word)
def left():
    word = 'Bye good customer'+' '*(79-17)
    start(word)
    os.system('clear')
    end(word)
