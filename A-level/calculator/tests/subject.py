import sympy
import convert

equation, symbols = convert.convert_equation("Enter a mathematical equation:\n")
variable = input("Enter the variable in the equation you want to make the subject:\n")

var = symbols[variable]
lhs, rhs = equation.split("=")
equation = f"({lhs}) - ({rhs})"

expr = sympy.simplify(equation)
equation = sympy.Eq(expr, 0)
for i in range(len(sympy.solve(equation, var))):
    answers = sympy.solve(equation, var)
    print(f"{variable} = {answers[i]}")
