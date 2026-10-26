def get_matching_paren(exp: str) -> int:
    """ Returns the index of the right parenthesis which matches the first left parenthesis.
        exp[0] should be a left parenthesis
    """
    if exp[0] != '(':
        raise ValueError('Given string must begin with \'(\' character')
    left = 1
    right = 0
    i = 1
    while left > right:
        if exp[i] == '(':
            left += 1
        elif exp[i] == ')':
            right += 1
        i += 1
    return i - 1


class InvalidElementError(Exception):
    """ This exception is raised when an element cannot successfully be created. This may occur if there are mismatched
        parenthesis, or if a symbol is used that is not recognized by Kanu
    """

    def __init__(self):
        pass


class InvalidVariableError(Exception):
    """ This exception is raised when the variable of an expression is a valid number, and the coefficient is 1.
        For example, Element e has coefficient of 1, and variable of 27. They should be flipped because 27 is a valid
        number."""

    def __init__(self, coefficient: float):
        self.coefficient = coefficient


class Element:
    def __init__(self, rep: str):
        elem = Element.separate_coefficient(rep)
        try:
            self.coefficient = float(elem[0])
        except ValueError:
            raise InvalidElementError()
        if self.coefficient != 0.0:
            try:
                self.variable = Variable(elem[1])
            except InvalidVariableError as ive:
                self.coefficient = ive.coefficient
                self.variable = Variable(None)
        else:
            self.variable = Variable(None)

    def __repr__(self):
        if self.variable is None:
            return f'{self.coefficient}'
        if self.coefficient == 0:
            return '0'
        if self.coefficient == 1.0:
            if self.variable.components == {}:
                return '1'
            return f'{self.variable}'
        if self.coefficient % 1 == 0.0:
            return f'{int(self.coefficient)}{self.variable}'
        return f'{self.coefficient}{self.variable}'

    def __eq__(self, other):
        return self.variable == other.variable and self.coefficient == other.coefficient

    @classmethod
    def separate_coefficient(cls, e: str) -> tuple:
        if e[0] == '+':
            e = e[1:]

        if '^' in e and (e[:e.index('^')].isdigit() or e[1:e.index('^')].isdigit() and e[0] == '-'):
            """ This check is for when e represents a real number raised to a power, not a variable.
                i.e. -2^4
            """
            return '1', e

        for i in range(len(e)):
            if e[i].isalpha():
                if i == 0:
                    return '1', e
                elif i == 1 and not e[0].isdigit():
                    return f'{e[:1]}1', e[1:]
                return e[:i], e[i:]
        # If the for loop completes, there was no variable in e
        return e, None

    @classmethod
    def add(cls, e1, e2):
        if e1.variable == e2.variable:
            return Element(f'{e1.coefficient + e2.coefficient}{e1.variable}')
        else:
            raise ValueError('Cannot add or subtract elements of different terms')

    @classmethod
    def sub(cls, e1, e2):
        if e1.variable == e2.variable:
            return Element(f'{e1.coefficient - e2.coefficient}{e1.variable}')
        else:
            raise ValueError('Cannot add or subtract elements of different terms')

    @classmethod
    def mul(cls, e1, e2):
        coefficient = e1.coefficient * e2.coefficient

        e1_copy = Element(f'{repr(e1)}')
        var = Variable.mul(e1_copy.variable, e2.variable)
        return Element(f'{coefficient}{var}')

    @classmethod
    def div(cls, e1, e2):
        coefficient = e1.coefficient / e2.coefficient

        e1_copy = Element(f'{repr(e1)}')
        var = Variable.div(e1_copy.variable, e2.variable)
        return Element(f'{coefficient}{var}')

    @classmethod
    def pow(cls, e1, e2):
        if not repr(e2).isdigit():
            return Element(f'{e1}^({e2})')
        elem = Element('1')
        for i in range(int(repr(e2))):
            elem = Element.mul(elem, e1)
        return elem


class Variable:
    def __init__(self, rep: str):
        self.name = ''
        self.components = {}  # dictionary, mapping a letter variable to it's frequency, represented as an Element
        self._parse_variable(rep)
        self.write_name()

    def __repr__(self):
        if self.name == '':
            return ''
        return self.name

    def __eq__(self, other):
        return self.components == other.components

    @classmethod
    def mul(cls, v1, v2):
        for e in v2.components:
            if v1.components.get(e) is None:
                v1.components[e] = v2.components[e]
            else:
                v1.components[e] = Element.add(v1.components[e], v2.components[e])
        v1.write_name()
        return v1

    @classmethod
    def div(cls, v1, v2):
        for e in v2.components:
            if v1.components.get(e) is None:
                v1.components[e] = Element.mul(v2.components[e], Element('-1'))
            else:
                v1.components[e] = Element.sub(v1.components[e], v2.components[e])
        v1.write_name()
        return v1

    def write_name(self):
        self._remove_redundant_variables()
        self.name = ''
        if self.components != {}:
            keys = sorted(list(self.components.keys()))
            for key in keys:
                if self.components[key] == Element('1'):
                    self.name += f'{key}'
                elif not repr(self.components[key]).isdigit() and len(repr(self.components[key])) > 1:
                    self.name += f'{key}^({self.components[key]})'
                else:
                    self.name += f'{key}^{self.components[key]}'

            first_key = list(self.components.keys())[0]
            if len(self.components) == 1 and first_key.isdigit() and self.components[first_key] == Element('1'):
                raise InvalidVariableError(float(list(self.components.keys())[0]))

    def _parse_variable(self, name: str):
        if name is not None:
            name += 'z'  # not part of the variable name, just so the loop can execute once more
            curr_var = name[0]
            check_exponent = False
            power = Element('1')
            i = 1
            while i < len(name):
                if check_exponent:
                    if name[i] == '(':
                        right_paren = get_matching_paren(name[i:])
                        power = Element(f'{name[i + 1:i + right_paren]}')
                        i += right_paren
                        check_exponent = False
                    else:
                        # end is the index of the first letter character after name[i], that is not an exponent
                        end = None
                        for j in range(i + 1, len(name)):
                            if name[j].isalpha() and name[j - 1] != '^':
                                end = j
                                break

                        if end == i + 1 and name[i] == '-':
                            power = Element(name[i:end + 1])
                            i += 1
                        else:
                            power = Element(name[i:end])
                            i = end - 1
                        check_exponent = False
                elif name[i] == '^':
                    check_exponent = True
                else:
                    #  this code is run when a new letter has been read
                    if self.components.get(curr_var) is None:
                        self.components[curr_var] = power
                    else:
                        self.components[curr_var] += power
                    curr_var = name[i]
                    power = Element('1')
                i += 1

    def _remove_redundant_variables(self):
        """ Removes all keys with value of zero because it equals one, and that is redundant.
            Also calculates exponents of two integers.
        """
        keys_to_remove = []
        keys_to_add = []
        for c in self.components:
            if self.components[c] == Element('0'):
                keys_to_remove.append(c)
            if repr(self.components[c]).isdigit() and c.isdigit():
                keys_to_remove.append(c)
                keys_to_add.append(repr(Element.pow(Element(c), self.components[c])))
        for k in keys_to_remove:
            del self.components[k]
        for k in keys_to_add:
            self.components[k] = Element('1')


operations = {'+': Element.add, '-': Element.sub, '*': Element.mul, '/': Element.div, '^': Element.pow}
operator_precedence = {'+': 2, '-': 2, '*': 3, '/': 3, '^': 4}


class InvalidExpressionError(Exception):
    """This exception is raised when an expression is syntactically invalid"""

    def __init__(self):
        pass


class MismatchedParenthesisError(InvalidExpressionError):
    """This exception is raised when there are mismatched parenthesis in an expression"""

    def __init__(self):
        pass


class OperatorList:
    def __init__(self, *elements, operation='+'):
        """ Elements is composed of Elements and OperatorLists
            op is an operation character: +, *, /
            There are no subtraction lists because they will just be addition lists with negative numbers
        """
        self.members = []
        is_first_element = True
        for e in elements:
            if isinstance(e, Element):
                if not is_first_element and operation == '-':
                    self.members.append(Element.mul(e, Element('-1')))
                else:
                    self.members.append(e)
            elif isinstance(e, OperatorList):
                if operation in ('*', '/'):
                    self.members.append(e)
                elif not is_first_element and operation in ('+', '-') and e.operation == '-':
                    for i in range(1, len(e.members)):
                        e.members[i] = Element.mul(e.members[i], Element('-1'))
                    self.members.extend(e.members)
                else:
                    self.members.extend(e.members)
            else:
                raise ValueError('Invalid argument for an OperatorList')
            is_first_element = False

        if operation == '-':
            self.operation = '+'
        else:
            self.operation = operation

        self.simplify()
        self.operation = '+'

    def __repr__(self):
        expression = ''
        for i in self.members:
            expression += f'{i} {self.operation} '
        return expression[:-2]

    def __eq__(self, other):
        return self.operation == other.operation and self.members == other.members

    def print(self) -> str:
        if self.operation == '+':
            output = [repr(self.members[0])]
            for i in range(1, len(self.members)):
                if self.members[i].coefficient < 0:
                    output.append('-')
                    output.append(repr(Element.mul(self.members[i], Element('-1'))))
                else:
                    output.append('+')
                    output.append(repr(self.members[i]))

            # Shave off all decimals past the hundredths column
            for i in range(len(output)):
                if '.' in output[i] and len(output[i]) >= output[i].index('.') + 2:
                    # if output[i] has a decimal, and there are at least two digits after the decimal
                    output[i] = str(round(float(output[i]), 2))
                    if float(output[i]) == int(output[i][:output[i].index('.')]):
                        output[i] = str(int(output[i][:output[i].index('.')]))
            return ' '.join(output)
        else:
            raise ValueError('Cannot print expression')

    def simplify(self):
        i = 0
        while i < len(self.members) - 1:
            j = i + 1
            restart = False
            while j < len(self.members):
                try:
                    e = operations[self.operation](
                        self.members[i],
                        self.members[j]
                    )
                    self.members.pop(j)
                    self.members.pop(i)
                    self.members.insert(i, e)
                    restart = True
                except ValueError:
                    j += 1
                except AttributeError:
                    j += 1
            if restart:
                i = 0
            else:
                i += 1

        while True:
            try:
                self.members.remove(Element('0'))
            except AttributeError:
                break
            except ValueError:
                break

        if (self.operation == '*' or self.operation == '/') and len(self.members) == 2:
            """if the preceding condition is true, this OperatorList must be simplified using the distributive
                property
            """
            new_members = []

            # first and second are OperatorLists and are cast to OperatorLists if they are not already
            first = self.members[0] if isinstance(self.members[0], OperatorList) else OperatorList(self.members[0])
            second = self.members[1] if isinstance(self.members[1], OperatorList) else OperatorList(self.members[1])

            # TODO: This works for mul, not div
            for i in first.members:
                for j in second.members:
                    new_members.append(operations[self.operation](i, j))
            self.members = new_members
            self.operation = '+'
            self.simplify()


def format_parens(exp: str) -> str:
    exp_list = list(exp)
    i = 0
    while i < len(exp_list):
        if i > 0 and exp_list[i] == '(' and \
                (exp_list[i - 1].isdigit() or exp_list[i - 1] == ')' or exp_list[i - 1].isalpha()):
            exp_list.insert(i, '*')
            i += 1
        elif i < len(exp_list) - 1 and exp_list[i] == ')' and \
                (exp_list[i + 1].isdigit() or exp_list[i + 1].isalpha()):
            exp_list.insert(i + 1, '*')
            i += 1

        i += 1
    return ''.join(exp_list)


def parse_expression(exp: str) -> list:
    # the '-' character is not part of the expression, it's function is so that the while loop executes once more
    exp = ''.join(exp.split()) + '-'
    elements = []
    begin = 0
    if exp[0] == '(':
        elements.append('(')
        begin += 1

    i = 1
    while i < len(exp):
        if exp[i] in operations or exp[i] in ('(', ')') or exp[i].isalpha():
            if (exp[i] in ('+', '-') and (exp[i - 1] in operations or exp[i - 1] == '(')) or exp[i].isalpha() \
                    and exp[i - 1] in operations:
                # if the above is true, then the sign is a negative sign, rather than a minus sign
                pass
            else:
                if begin != i:
                    elements.append(exp[begin:i])
                if exp[i].isalpha() and (exp[i - 1].isdigit() or exp[i - 1].isalpha()):
                    elements.append('*')
                elements.append(exp[i])
                begin = i + 1
        i += 1
    return elements[:-1]


def to_rpn(elements: list) -> list:
    """Conversion to reverse polish notation, implementing the Shunting-yard algorithm"""
    i = 0
    output_queue = []
    op_stack = []
    while i < len(elements):
        token = elements[i]
        try:
            # If token is not a valid element string, it will raise an InvalidElementError
            output_queue.append(Element(token))
        except InvalidElementError:
            if token in ('+', '-', '*', '/', '^'):
                while len(op_stack) > 0 and \
                        op_stack[-1] != '(' \
                        and operator_precedence[op_stack[-1]] >= operator_precedence[token]:
                    output_queue.append(op_stack.pop())
                op_stack.append(token)
            elif token == '(':
                op_stack.append(token)
            elif token == ')':
                while len(op_stack) > 0 and op_stack[-1] != '(':
                    output_queue.append(op_stack.pop())

                if len(op_stack) == 0:
                    raise MismatchedParenthesisError()
                op_stack.pop()
        i += 1

    while len(op_stack) > 0:
        output_queue.append(op_stack.pop())
    return output_queue


def to_op_list(elements: list) -> OperatorList:
    """elements should be a properly written reverse polish notation expression to be made into OperatorLists"""
    if len(elements) == 0:
        raise InvalidExpressionError()
    new_elements = []
    for e in elements:
        if isinstance(e, Element):
            new_elements.append(e)
        elif e in operations:
            operand_2 = new_elements.pop()
            operand_1 = new_elements.pop()
            result = OperatorList(operand_1, operand_2, operation=e)
            if len(result.members) == 1:
                result = Element(repr(result.members[0]))
            new_elements.append(result)
    if len(new_elements) > 1:
        raise ValueError("was not able to process expression")

    if type(new_elements[0]) == OperatorList:
        return new_elements[0]
    return OperatorList(*new_elements, operation='+')


def all_together_now(expression: str) -> OperatorList:
    """Calls all needed methods to have a readable expression"""
    ex = format_parens(expression)
    ex = parse_expression(ex)
    ex = to_rpn(ex)
    return to_op_list(ex)


class NonLinearEquationError(Exception):
    """ Raised when the given equation is non-linear
    """
    pass


def find_variables(exp: OperatorList) -> set:
    variables = set()
    for elem in exp.members:
        variables = variables.union(elem.variable.components.keys())
    return variables


def solve_single_linear_equation(equation: str) -> str:
    equal_sign = equation.index('=')

    try:
        ls = all_together_now(equation[:equal_sign])
        rs = all_together_now(equation[equal_sign + 1:])
    except (MismatchedParenthesisError, InvalidElementError, InvalidExpressionError):
        return 'This equation is syntactically invalid!'

    ls_vars = find_variables(ls)
    rs_vars = find_variables(rs)

    if len(ls_vars.union(rs_vars)) > 1:
        raise ValueError('Cannot solve single equation with multiple variables')
    elif len(ls_vars.union(rs_vars)) == 0:
        return 'There are no variables to solve for!'

    # Here, it is confirmed that there is only one variable in the equation
    # The variable is isolated on the left side:

    while len(find_variables(rs)) > 0:
        for element in rs.members:
            if element.variable.components != {}:
                # subtracting the element with a variable from both sides
                rs = OperatorList(*rs.members, Element.mul(element, Element('-1')))
                ls = OperatorList(*ls.members, Element.mul(element, Element('-1')))
                break

    for elem in ls.members:
        if elem.variable.components != {}:
            keys = list(elem.variable.components.keys())
            for key in keys:
                if elem.variable.components[key] != Element('1'):
                    raise NonLinearEquationError()

    while len(find_variables(ls)) < len(ls.members):
        # if the above condition is true, there are elements in ls which do not have variables
        for element in ls.members:
            if element.variable.components == {}:
                # subtracting the element with a variable from both sides
                rs = OperatorList(*rs.members, Element.mul(element, Element('-1')))
                ls = OperatorList(*ls.members, Element.mul(element, Element('-1')))
                break

    if len(ls.members) == 0 and len(rs.members) == 0:
        return 'There are infinite solutions'

    if len(ls.members) == 0 or len(rs.members) == 0:
        return f'{ls_vars.pop()} = 0'

    if len(ls.members) == 1 and len(rs.members) == 1:
        divisor = Element(f'{ls.members[0].coefficient}')
        ls = OperatorList(ls.members[0], divisor, operation='/')
        rs = OperatorList(rs.members[0], divisor, operation='/')

    return f'{ls.print()} = {rs.print()}'


while True:
    print('Select one:')
    print('\t1 -> Solve a linear equation')
    print('\t2 -> Simplify any expression')
    print('\t3 -> Exit program')

    choice = input()
    if choice == '1':
        print('Enter the equation:', end=' ')

        try:
            print(solve_single_linear_equation(input()))
        except NonLinearEquationError:
            print('You entered a non-linear equation. The current version of Kanu can only solve linear equations!')
    elif choice == '2':
        print('Enter the expression:', end=' ')
        print(all_together_now(input()))
    elif choice == '3':
        print('Thank you for using kanu!\nPlease contact me at jake@jakelgoodman.com with any bugs or suggestions.')
        break
    else:
        print('You must select an option from the menu!')
    print()
