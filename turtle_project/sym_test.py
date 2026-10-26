import sympy as sp
from sympy.printing import StrPrinter

class CustomStrPrinter(StrPrinter):
    def _print_Symbol(self, expr):
        return f'{{{expr.name}}}'

a, b = sp.symbols('a b')
expr = a + b

custom_strPrinter = CustomStrPrinter().doprint
print(custom_strPrinter(expr))  # {a} + {b}
a = 1
b = 10
print(f"{custom_strPrinter(expr)}")