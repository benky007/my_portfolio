def add():
    pass


def sub():
    pass


def times():
    pass


def rotate():
    pass


def translate():
    pass


def scale():
    pass


def rotate3D():
    pass


def translate3D():
    pass


def scale3D():
    pass


def form(array, dim):
    length = len(array)
    rows = 1
    columns = 1
    depth = 1
    dimensions = 1
    for element in dim:
        if element == "x":
            dimensions += 1
    try:
        shape = dim.split("x")
        rows = int(shape[0])
        columns = int(shape[1])
        depth = int(shape[2])
    except IndexError:
        pass
    print(rows, columns, depth, dimensions, length)
    count = 0
    if dimensions == 3 and length == rows * columns * depth:
        empty = [[[x for x in range(columns)] for _ in range(rows)] for _ in range(depth)]
    elif dimensions == 2 and length == rows * columns * depth:
        empty = [[x for x in range(columns)] for _ in range(rows)]
    elif dimensions == 1 and length == rows * columns * depth:
        empty = [x for x in range(rows)]
    else:
        empty = None
    try:
        for index, D2 in enumerate(empty):
            for index1, D1 in enumerate(D2):
                for index2, element in enumerate(D1):
                    empty[index][index1][index2] = array[count]
                    count += 1
    except TypeError:
        pass
    return empty


print(form([0, 1, 2, 3, 4, 5, 34, 7, 8, 9, 10, 11], "12"))
