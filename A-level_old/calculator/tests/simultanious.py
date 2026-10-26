import sympy
import convert

expr1, symbols1 = convert.convert_equation("Enter a mathematical equation:\n")
expr2, symbols2 = convert.convert_equation("Enter a second mathematical equation:\n")

symbols = symbols1.copy()
symbols.update(symbols2)

lhs1, rhs1 = sympy.simplify(expr1.split("=")[0]), sympy.simplify(expr1.split("=")[1])
lhs2, rhs2 = sympy.simplify(expr2.split("=")[0]), sympy.simplify(expr2.split("=")[1])

eq1 = sympy.Eq(lhs1, rhs1)
eq2 = sympy.Eq(lhs2, rhs2)

answer = sympy.solve((eq1, eq2), list(symbols.values()))
for var in answer:
    if type(answer[var]) == list:
        for element in answer[var]:
            print(f"{var} = {element}")
    else:
        print(f"{var} = {answer[var]}")
