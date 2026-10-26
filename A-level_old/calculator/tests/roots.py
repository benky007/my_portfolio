import sympy
import convert

expr, symbols = convert.convert_equation("Enter a mathematical equation:\n")

lhs, rhs = expr.split("=")

expression = f"({lhs})-({rhs})"

function = sympy.simplify(expression)

roots = sympy.roots(function)
print(roots)
