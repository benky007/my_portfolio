# 2x+2y(-6y+3x)=2x^(2)-x
# 2x-7y+34-7z-45+87y
import time
import numpy as np


def split_algebra(eq):
    if "=" in eq:
        ls = eq[:eq.index("=")]
        rs = eq[eq.index("=") + 1:]
    else:
        ls = eq
        rs = None
    ls_list = []
    ls_symbols = []
    parens = 0
    for i, char in enumerate(ls):
        if char == "(" or char == ")":
            parens += 1
        if (char == "+" or char == "-") and parens % 2 == 0:
            ls_symbols.append(i)
    for u, pos in enumerate(ls_symbols):
        # print(f"{u}: {ls_symbols.index(pos) == 0}")
        # print(f"{u}: {ls_symbols.index(pos) == len(ls_symbols)-1}")
        # print(f"{u}: {ls_symbols.index(pos) != 0}")
        if ls_symbols.index(pos) == 0:
            ls_list.append(ls[:pos])
            ls_list.append(ls[pos])
        if ls_symbols.index(pos) != 0:
            ls_list.append(ls[ls_symbols[ls_symbols.index(pos) - 1] + 1:pos])
            ls_list.append(ls[pos])
        if ls_symbols.index(pos) == len(ls_symbols) - 1:
            ls_list.append(ls[pos + 1:])
    if rs is not None:
        rs_list = []
        rs_symbols = []
        for i, char in enumerate(rs):
            if char == "(" or char == ")":
                parens += 1
            if (char == "+" or char == "-") and parens % 2 == 0:
                rs_symbols.append(i)
        for pos in rs_symbols:
            if rs_symbols.index(pos) == 0:
                rs_list.append(rs[:pos])
                rs_list.append(rs[pos])
            if rs_symbols.index(pos) != 0:
                rs_list.append(rs[rs_symbols[rs_symbols.index(pos) - 1] + 1:pos])
                rs_list.append(rs[pos])
            if rs_symbols.index(pos) == len(rs_symbols) - 1:
                rs_list.append(rs[pos + 1:])
    try:
        return ls_list, rs_list
    except UnboundLocalError:
        return ls_list, None


def expand(expr):
    # print(expr)
    expr_list = []
    parens = []
    for i, char in enumerate(expr):
        if char == "(" or char == ")":
            parens.append(i)
        if char == "(" and expr[i - 1] != "(":
            expr_list.append(expr[:i])
            expr_list.append(expr[i:])
    expr = expr_list[0] + "*" + expr_list[1]
    print(expr)
    out = list(expr.split("*")[0])
    expr = expr.split("(")[1].split(")")[0]
    print(out)
    print(expr)
    expr_list = []
    symbols = []
    for i, char in enumerate(expr):
        if char.isalpha():
            symbols.append(i)
    for pos in symbols:
        if expr[pos - 1].isnumeric():
            new = "*"
        else:
            new = "1*"
        if symbols.index(pos) == 0:
            expr_list.append(expr[:pos])
            expr_list.append(new)
        if symbols.index(pos) != 0:
            expr_list.append(expr[symbols[symbols.index(pos) - 1]:pos])
            expr_list.append(new)
        if symbols.index(pos) == len(symbols) - 1:
            expr_list.append(expr[pos:])
    temp = ""
    for element in expr_list:
        temp += element
    expr = temp
    print(expr)


# TODO: solving linear equations
def linear_solve(eq):
    return eq


# TODO: solving quadratic equations
def quadratic_solve(eq):
    equ = eq
    for char in eq:
        if char.isalpha():
            sym = char
        else:
            sym = "x"
    eq = "".join(eq.split(" "))
    if eq[-2:] == "=0":
        eq = eq[:-2]
    eq = eq.replace(f"+{sym}", f"+1{sym}").replace(f"-{sym}", f"-1{sym}").replace(f"{sym}+", f"{sym}^1+") \
        .replace(f"{sym}-", f"{sym}^1-")
    if eq[0] == "-" and eq[1] == sym:
        eq = eq[0] + "1" + eq[1:]
    if eq[0] == sym:
        eq = "+1" + eq
    if eq[0].isnumeric():
        eq = "+" + eq
    if eq[-1].isnumeric():
        eq = eq + f"{sym}^0"
    nums = eq.split(sym)
    nums.insert(2, str(nums[1].split("^2")[1]))
    nums[1] = nums[1].split(nums[2])[0]
    nums.insert(4, str(nums[3].split("^1")[1]))
    nums[3] = nums[3].split(nums[4])[0]
    abc = []
    for i in range(0, len(nums), 2):
        abc.append(nums[i])
    print(abc)
    a, b, c = int(abc[0]), int(abc[1]), int(abc[2])
    x = ((-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a), (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a))
    return equ, x


# TODO: solving simultaneous equations
def simultaneous_solve(eq1, eq2):
    # 2w + x + 4y + 3z = 5
    # w - 2x + 3z = 3
    # 3w + 2x - y + z = -1
    # 4x - 5z = -3
    A = [[2, 1, 4, 3], [1, -2, 0, 3], [3, 2, -1, 1], [0, 4, 0, 5]]
    Y = [5, 3, -1, 3]

    res = np.linalg.inv(A).dot(Y)
    return res


# TODO: inequalities (maybe)
def inequalities_solve(eqs, coord):
    return eqs


# TODO: formula (y = x/2 + 7)
def find_vars(eq):
    return eq


def formulate(eq, vals):
    return eq


# TODO: values in sequences
# TODO: solving sequences
# TODO: plotting equations
# TODO: plotting simultaneous equations
# TODO: plotting inequalities (maybe)
# TODO: simplifying expressions
def expression_simp(eq):
    ls, rs = split_algebra(eq)
    print(ls)
    print(rs)
    return ls, rs


# TODO: make _ the subject
def subject_change(eq, sub):
    return eq


# running = False
running = True
while running:
    time.sleep(5)
    print('Select one:')
    print('\t1 -> Solve a linear equation')
    print('\t2 -> Solve quadratic equation')
    print('\t3 -> Solve simultaneous equations')
    print('\t4 -> Is value in the inequalities')
    print('\t5 -> Use formula to find the value')
    print('\t6 -> Sequences')
    print('\t7 -> Plotting equations')
    print('\t8 -> Simplifying expressions')
    print('\t9 -> make _ the subject')
    print('\t0 -> Exit program')
    choice = input()
    if choice == "1":
        print("Enter the equation with only one unknown:")
        equation = input()
        ans = linear_solve(equation)
        print(ans)
    elif choice == "2":
        print("Enter the quadratic equation with only one unknown:")
        equation = input()
        equation, ans = quadratic_solve(equation)
        print(f"The answer to your equation: {equation}\nWas: x={ans[0]} and x={ans[1]}")
    elif choice == "3":
        print("Enter the first equation with only one unknown:")
        equation1 = input()
        print("Enter the second equation with only one unknown")
        equation2 = input()
        ans = simultaneous_solve(equation1, equation2)
        print(ans)
    elif choice == "4":
        inequalities = []
        equating = True
        while equating:
            if len(inequalities) == 0:
                print("Enter the first inequality(or calculate to stop entering)")
            else:
                print("Enter the next inequality(or calculate to stop entering)")
            equation = input()
            if equation == "calculate":
                equating = False
            inequalities.append(equation)
        testing = True
        while testing:
            print("Enter a coordinate you want to test with(or enter menu to go back)")
            coordinate = input()
            if coordinate == "menu":
                testing = False
            ans = inequalities_solve(inequalities, coordinate)
            print(ans)
    elif choice == "5":
        print("Enter formula to have values put in to calculate the unknown\n"
              "(in the format W=____ for W to be returned):")
        equation = input()
        variables = find_vars(equation)
        values = {}
        for variable in variables:
            print(f"Enter value for {variable}:")
            value = input()
            values[variable] = value
        ans = formulate(equation, values)
        print(ans)
    elif choice == "6":
        # sequences
        pass
    elif choice == "7":
        # plotting
        pass
    elif choice == "8":
        print("Enter the expression:")
        equation = input()
        ans = expression_simp(equation)
        # print(ans)
        running = False
    elif choice == "9":
        print("Enter the equation:")
        equation = input()
        print("Enter what you want to be made the subject:")
        subject = input()
        ans = subject_change(equation, subject)
        print(ans)
    elif choice == "0":
        print("Thanks for using my calculator")
        running = False
