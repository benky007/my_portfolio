import random
while True:
    result = 0
    x = input("What die do you want? ")
    d = int(x[:x.find('d')])
    i = x[x.find('d')+1:]
    if i.find('+') != -1:
        c = int(i[:i.find('+')])
        e = int(i[i.find('+'):])
    elif i.find('-') != -1:
        c = int(i[:i.find('-')])
        e = int(i[i.find('-'):])
    for i in range(d):
        y = random.randint(1, (c))
        result += y
    print("You rolled ")
    if result == d:
        print("critical miss")
    elif result == c * d:
        print("critical hit")
    else:
        print(str(result + e))
