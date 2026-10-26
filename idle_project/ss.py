def bin_search(array, value):
    ans = 0
    og = 0
    count = 0
    searching = True
    while searching:
        length = len(array)
        index = int(round(((length + 1) / 2), 0)-1) # current problem is that it is rounding to the nearest even int so not right and then try to fix the index counting BEN
        if count == 0:
            og = index
        print(f"\n{index}")
        print(length)
        print(og)
        print(array)
        middle = array[index]
        if middle == value:
            if count > 0:
                og += index
            ans = (value, og, count)
            searching = False
        elif middle > value:
            if count > 0:
                og -= index
            array = array[:index]
        elif middle < value:
            if count > 0:
                og += index
            array = array[index+1:]
        print(f"\n{array}")
        print(og)
        count += 1

    return ans


def lin_search():
    pass


def merge_sort():
    pass


def insert_sort():
    pass


def bubble_sort():
    pass


print(bin_search([0, 4, 5, 6, 6, 7, 9, 10], 4))
