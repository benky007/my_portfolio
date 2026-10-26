import math


class Matrix:
    def __init__(self, dim=None, vector=False, a=[]):
        if not vector:
            self._dim = dim
            self._array = a
            self._length = 1
            self._coord = None
            self._rows = 1
            self._columns = 1
            self._depth = 1
            self._dimensions = 1
            for element in self._dim:
                if element == "x":
                    self._dimensions += 1
            try:
                self._size = self._dim.split("x")
                self._rows = int(self._size[0])
                self._columns = int(self._size[1])
                self._depth = int(self._size[2])
            except IndexError:
                pass
            if self._array:
                pop = True
                self._length = len(self._array)
            else:
                pop = False
                self._length = self._rows * self._columns * self._depth
                self._array = [0 for i in range(self._length)]
            if self._dimensions == 3 and self._length == self._rows * self._columns * self._depth:
                empty = [[[x for x in range(self._columns)] for _ in range(self._rows)] for _ in range(self._depth)]
            elif self._dimensions == 2 and self._length == self._rows * self._columns * self._depth:
                empty = [[x for x in range(self._columns)] for _ in range(self._rows)]
            elif self._dimensions == 1 and self._length == self._rows * self._columns * self._depth:
                empty = [x for x in range(self._rows)]
            else:
                empty = None
            self._value = empty
            if pop:
                self.populate(self._array)
            else:
                pass
        else:
            self.vector(a)

    def populate(self, array):
        count = 0
        self._array = array
        if self._dimensions == 3:
            for index, D2 in enumerate(self._value):
                for index1, D1 in enumerate(D2):
                    for index2, element in enumerate(D1):
                        self._value[index][index1][index2] = self._array[count]
                        count += 1
        elif self._dimensions == 2:
            for index, D2 in enumerate(self._value):
                for index1, element in enumerate(D2):
                    self._value[index][index1] = self._array[count]
                    count += 1
        elif self._dimensions == 1:
            for index, element in enumerate(self._value):
                self._value[index] = self._array[count]
                count += 1
        else:
            pass

    def vector(self, coord):
        self._dimensions = 2
        self._array = None
        self._coord = coord
        self._columns = 1
        self._depth = 1
        if len(coord) == 2:
            self._rows = 3
            self._length = 3
            self._size = ["3", "1"]
            self._value = [[coord[0]], [coord[1]], [1]]
        elif len(coord) == 3:
            self._rows = 4
            self._length = 4
            self._size = ["4", "1"]
            self._value = [[coord[0]], [coord[1]], [coord[2]], [1]]
        else:
            self._dimensions = None
            self._array = None
            self._coord = None
            self._columns = None
            self._depth = None
            self._rows = None
            self._length = None
            self._size = None
            self._value = None

    def get(self, var):
        if var == "value":
            return self._value
        elif var == "coord":
            return self._coord
        elif var == "dim":
            return self._dim
        elif var == "size":
            return self._size
        elif var == "dimensions":
            return self._dimensions
        elif var == "rows":
            return self._rows
        elif var == "columns":
            return self._columns
        elif var == "depth":
            return self._depth
        elif var == "length":
            return self._length
        elif var == "array":
            return self._array
        else:
            return None

    def check(self, matrix, operation=2):
        if operation == 1:
            if self._size == matrix.get("size"):
                return True
            else:
                return False
        elif operation == 2:
            if self._columns == matrix.get("rows"):
                return True
            else:
                return False
        elif operation == 3:
            if self._rows == 3 and self._columns == 1:
                return True
            else:
                return False
        elif operation == 4:
            if self._rows == 4 and self._columns == 1:
                return True
            else:
                return False
        else:
            return False

    def add(self, matrix):
        if self.check(matrix, 1):
            product = Matrix(self._dim)
            res = product.get("array")
            for index, element in enumerate(self._array):
                res[index] = element + matrix.get("array")[index]
            product.populate(res)
            return product.get("value")
        else:
            return None

    def sub(self, matrix):
        if self.check(matrix, 1):
            product = Matrix(self._dim)
            res = product.get("array")
            for index, element in enumerate(self._array):
                res[index] = element - matrix.get("array")[index]
            product.populate(res)
            return product.get("value")
        else:
            return None

    def times(self, matrix):
        if self.check(matrix, 2):
            if self._dimensions == 2:
                product = Matrix(f"{self._rows}x{matrix.get('columns')}")
                res = product.get("array")
                a = self._array
                m = matrix.get("value")
                r = matrix.get("rows")
                c = matrix.get("columns")
                new = [i for i in range(matrix.get("length"))]
                for index, val in enumerate(new):
                    if index != 0:
                        if (index / r).is_integer():
                            next1 = int(index / r)
                    else:
                        next1 = 0
                    new[index] = m[index % r][next1]
                # print(a)
                # print(new)
                next3 = 0
                og = a[0:0 + int(len(a) / self._rows)]
                next3 = next3 + int(len(a) / self._rows)
                count = 0
                for loop1 in range(self._rows):
                    next2 = 0
                    using = new[next2:next2 + int(len(a) / c)]
                    next2 += int(len(a) / c)
                    for loop in range(c):
                        # print(f"og: {og}")
                        # print(f"using: {using}")
                        temp = 0
                        for index, i in enumerate(og):
                            # print(i, using[index])
                            temp += i * using[index]
                        using = new[next2:next2 + int(len(a) / c)]
                        next2 += int(len(a) / c)
                        res[count] = temp
                        count += 1
                    og = a[next3:next3 + int(len(a) / self._rows)]
                    next3 += int(len(a) / self._rows)
                product.populate(res)
                return product.get("value")
        else:
            return None

    def rotate(self, angle, axis="z"):
        angle = -1 * angle
        try:
            sine = math.sin(math.radians(angle))
            cosine = math.cos(math.radians(angle))
        except TypeError:
            cosine = 0
            sine = 1
        if self.check(None, 3):
            transformation = Matrix("3x3", a=[cosine, -1 * sine, 0, sine, cosine, 0, 0, 0, 1])
            self._value = transformation.times(self)
            for i in range(len(self._value)-1):
                self._coord[i] = self._value[i]
        elif self.check(None, 4):
            if axis == "x":
                transformation = Matrix("4x4", a=[1, 0, 0, 0, 0, cosine, -1 * sine, 0, 0, sine, cosine, 0, 0, 0, 0, 1])
                self._value = transformation.times(self)
                for i in range(len(self._value) - 1):
                    self._coord[i] = self._value[i]
            elif axis == "y":
                transformation = Matrix("4x4", a=[cosine, 0, sine, 0, 0, 1, 0, 0, -1 * sine, 0, cosine, 0, 0, 0, 0, 1])
                self._value = transformation.times(self)
                for i in range(len(self._value) - 1):
                    self._coord[i] = self._value[i]
            elif axis == "z":
                transformation = Matrix("4x4", a=[cosine, -1 * sine, 0, 0, sine, cosine, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1])
                self._value = transformation.times(self)
                for i in range(len(self._value) - 1):
                    self._coord[i] = self._value[i]
            else:
                self._value = None
        else:
            self._value = None
        return self._coord

    def translate(self, vector=(0, 0)):
        if self.check(None, 3):
            (x, y) = vector
            transformation = Matrix("3x3", a=[1, 0, x, 0, 1, y, 0, 0, 1])
            self._value = transformation.times(self)
            for i in range(len(self._value)-1):
                self._coord[i] = self._value[i]
        elif self.check(None, 4):
            (x, y, z) = vector
            transformation = Matrix("4x4", a=[1, 0, 0, x, 0, 1, 0, y, 0, 0, 1, z, 0, 0, 0, 1])
            self._value = transformation.times(self)
            for i in range(len(self._value)-1):
                self._coord[i] = self._value[i]
        else:
            self._value = None
        return self._coord

    def scale(self, vector=(1, 1)):
        if self.check(None, 3):
            (x, y) = vector
            transformation = Matrix("3x3", a=[x, 0, 0, 0, y, 0, 0, 0, 1])
            self._value = transformation.times(self)
            for i in range(len(self._value)-1):
                self._coord[i] = self._value[i]
        elif self.check(None, 4):
            (x, y, z) = vector
            transformation = Matrix("4x4", a=[x, 0, 0, 0, 0, y, 0, 0, 0, 0, z, 0, 0, 0, 0, 1])
            self._value = transformation.times(self)
            for i in range(len(self._value)-1):
                self._coord[i] = self._value[i]
        else:
            self._value = None
        return self._coord

'''
l1 = [0, 3, 4, 2, 5, 3]
l2 = [0, 6, 2, -3, 8, 3]
m1 = Matrix("2x3")
m1.populate(l1)
# print(m1.get("value"))
m2 = Matrix("3x2")
m2.populate(l2)
# print(m2.get("value"))
# ans = m1.add(m2)
# ans = m1.sub(m2)
ans = m1.times(m2)
# print(ans)

v1 = Matrix(None, True, [4, 3])
print(v1.get("coord"))
SF = (-1, -1)
ans = v1.rotate(90)
print(ans)
'''