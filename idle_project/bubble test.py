Passengers = [0, 3, 5, 1, 8, 4, 7, 1, 4, 2, 7]
print(Passengers)
sorted1 = False
while not sorted1:
    count = 0
    flips = 0
    while count < len(Passengers)-1:
        print(count)
        if Passengers[count] > Passengers[count+1]:
            temp = Passengers[count]
            Passengers[count] = Passengers[count+1]
            Passengers[count+1] = temp
            flips += 1
        count += 1
    print(Passengers)
    if flips == 0:
        sorted1 = True
