first = ord('A')
last = ord('z')
base = last + 1 - first
digits = 5
password = ''
answer = []
for i in range(base**digits):
    password = ''
    run = True
    while run:
        password = chr(i % base + first) + password
        i //= base
        if i == 0:
            run = False
    # print(password.zfill(digits), 'and the amount of digits currently', len(password), '/', digits)
    print(len(password))
    answer.append(password.zfill(digits))
print(answer)
