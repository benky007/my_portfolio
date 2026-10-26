import re
import sympy


def convert_equation(prompt):
    symbol_dict = {}

    equation = input(prompt)
    mod = re.sub(r'([a-zA-Z])([a-zA-Z])', r'\1*\2', re.sub(r'([a-zA-Z])([(])|(\d+)([a-zA-Z])|(\d+)([(])|([)])([(])',
                                                           r'\1\3\5\7*\2\4\6\8', equation)).replace("^", "**")

    for char in equation:
        if char.isalpha() and char not in symbol_dict:
            symbol_dict[char] = sympy.symbols(char)

    return mod, symbol_dict
