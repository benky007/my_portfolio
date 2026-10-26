num = 1
num1 = num - 1
list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
comb = []
w = 0
wTimes = 0

tt = 10**num1
tt2 = 10**num
tt3 = tt2 * 2
times = tt
times2 = tt3 - 1
number = times / 10

for i in range(num):
    for u in range(len(list1)):
        if i > 0:
            if u == 0:
                w = 1 + num1
            else:
                v = 3 + num1
                w += v
                wTimes = w + times2
            comb.insert(wTimes, list1[u])

        else:
            for e in range(num):
                print(e, 'e is')
                for t in range(len(list1)):
                    print(t, 't is')
                    for g in range(times):
                        print(g, 'g is')
                        comb.append(list1[t])
                        comb.append(' ')

print(comb)
