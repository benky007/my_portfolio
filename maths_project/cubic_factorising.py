def factors(num):
    thing = []
    for e in range(num):
        if num % (e + 1) == 0:
            thing.append(e + 1)
    return thing


def x2(list1, X2, quest):
    theEnd = []
    first = 0
    last = int(len(list1) - 1)
    length1 = last + 1 - first
    for i in range(length1 ** 3):
        counter = ''
        answer = ''
        run = True
        while run:
            counter = str(i % length1 + first) + counter
            i //= length1
            if i == 0:
                run = False
        ans = list(counter.zfill(3))
        for h in range(3):
            place = int(ans[h])
            answer = answer + str(list1[int(place)])
        # print('The ans is', ans)
        # print('The counter is', counter.zfill(3))
        if quest == 1:
            evaluate = list(answer)
            evaluate.insert(1, '+')
            evaluate.insert(3, '+')
            space = ' '
            end = eval(space.join(evaluate))
            if end == int(X2):
                theEnd.append(answer)
            elif int(X2) == 0:
                theEnd.append(answer)
        else:
            theEnd.append(answer)
    return theEnd


def multiple(theEnd1):
    endList = []
    for p in range(len(theEnd1)):
        q = list(theEnd1[p])
        q.insert(1, '*')
        q.insert(3, '*')
        space = ' '
        end1 = eval(str(space.join(q)))
        if end1 == 6:
            endList.append(theEnd1[p])
    return endList[0]


def x3(fac, X3, combs1):
    pass


a = input('what is your factorising cubic equation?\n')

sec = a.replace('+', ' +')
sec1 = sec.replace('-', ' -').split(' ')
f = factors(int(sec1[3]))
length = len(sec1[0])
if length > 3:
    x3 = sec1[0][:length - 3]
    x4 = factors(int(x3))
    combs = x2(f, 0, 0)
    end2 = x2(x4, 0, 0)
    result = x3(f, end2, combs)
    print(combs)
    print(end2)
XX = x2(f, sec1[1][1], 1)
XXX = multiple(XX)
print(XXX)