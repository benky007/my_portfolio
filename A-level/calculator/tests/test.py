import re
from sympy import *
name = "test"
value = "'m0'"
exec("%s=%s" % (name, value), globals())
exec("{}={}".format(name, value), globals())
print(test)


def symplify(expr):
    letters = list(dict.fromkeys(re.findall(r'[a-zA-Z]+', expr)))
    letter = letters[0]
    name = letter
    value = "'symbols(letter)'"
    exec("%s=%s" % (name, value), globals())
    exec("{}={}".format(name, value), globals())
    ans = simplify(expr)
    print(ans)


def sym2(expr):
    letters = list(dict.fromkeys(re.findall(r'[a-zA-Z]+', expr)))
    dict1 = {}
    for count, letter in enumerate(letters):
        eq = re.sub(letter, str(count+1), expr)
        dict1[letter] = count
    print(dict1)
    ans = int(eval(eq))
    for i in range(len(letters)):
        ans = ans/(i+1)
        ans = str(int(ans))
    ans1 = "".join(letters)
    print(ans+ans1)
