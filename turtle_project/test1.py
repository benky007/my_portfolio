def split_sides(eq):
    equals = eq.index("=")
    ls = eq[:equals]
    rs = eq[equals+1:]
    return ls, rs


def compute(eq, x):
    past_char = 0
    power = 0
    multiply = 0
    divide = 0
    for element in eq:
        for i, current_char in enumerate(element):
            if current_char == "*" and past_char == "*":
                power += 1
            if current_char == "*" and past_char != "*" and element[i + 1] != "*":
                multiply += 1
            if current_char == "/":
                divide += 1
            past_char = current_char


def parts():


equation = "x**2+2*x+1=0"
ls, rs = split_sides(equation)
if ls == 0 or rs == 0:
