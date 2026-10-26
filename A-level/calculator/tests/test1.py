def parse(s):
    li = []

    open1 = 0
    closed = False
    start_index = -1

    for index, c in enumerate(s):
        if c == '(':
            if open1 == 0:
                start_index = index
            open1 += 1

        elif c == ')':
            open1 -= 1
            if open1 == 0:
                closed = True

        elif closed:
            li.append(s[start_index: index + 1])
            closed = False

        elif open1 == 1:
            li.append(c)

    start = s[:start_index]
    past = ""
    for index, element in enumerate(li):
        if element.isdigit():
            li[index] = start + li[index]
        if element == ".":
            element[index-1:index] = element[index-1] + element[index]
        if past.isdigit() and element.isdigit():
            element[index-1:index] = element[index-1] + element[index]
        past = element

    return li


ans = parse("2*(3+4)")
print(ans)
