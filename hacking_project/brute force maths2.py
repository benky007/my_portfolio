num = 2
num1 = num - 1
num2 = num + 1
num3 = num - 2
list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
comb = []
base = len(list1)
tt = base ** num1
times = tt * 2
firstPos = 1 + times
nextPos = firstPos - 3
comb1 = ''
count = 0

if num3 >= 0:
    tt2 = base ** num3
else:
    tt2 = 0

for i in range(10):
    comb.append(list1[i])
    comb.append(' ')

for t in range(len(list1)):
    #print(t, 't is')
    for g in range(tt):
        #print(g, 'g is')
        comb.append(list1[t])
        comb.append(' ')

if num > 1:
    for e in range(tt):
        for b in range(len(list1)):
        #print(b, 'b is')
            for n in range(tt2):
                #print(n, 'n is')
                nextPos = nextPos + num3 + 3
                #print(nextPos)
                comb.insert(nextPos, list1[b])

for u in range(len(comb)):
    comb1 += comb[u]

print(comb1)
#print('num is', num)
#print('list is', len(list1))
#print('times is', tt)
