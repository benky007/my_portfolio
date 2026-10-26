class Queue:
    def __init__(self, data: list = None, maximum: int = None, queueType: str = "fixed") -> None:
        if data is None:
            data = []
        if data is not None:
            self._next_item_pointer: int = 0
        else:
            self._next_item_pointer: int = -1
        self._free_pointer: int = 0
        self._queue: list = list(data)
        self._attributes: dict = {"max": len(self._queue), "type": queueType}
        if maximum is not None:
            self._attributes["max"] = maximum

        if not str(self._attributes["max"]).isnumeric():
            raise ValueError("Max size of fixed queue must be an integer value")
        else:
            self._attributes["max"] = int(self._attributes["max"])
        if self._attributes["type"] != "fixed" and self._attributes["type"] != "circular":
            raise TypeError("Queues can only be type fixed or circular")
        if len(self._attributes) > 2:
            for key in self._attributes.keys():
                if key != "max" and key.lower() == "max":
                    temp = self._attributes[key]
                    del self._attributes[key]
                    self._attributes["max"] = temp
                elif key != "type" and key.lower() == "type":
                    temp = self._attributes[key]
                    del self._attributes[key]
                    self._attributes["type"] = temp
                elif key != "max" and key != "type":
                    del self._attributes[key]
                else:
                    pass

        if len(self._queue) < self._attributes["max"]:
            more = self._attributes["max"] - len(self._queue)
            for _ in range(more):
                self._queue.append(None)
        elif len(self._queue) > self._attributes["max"]:
            more = self._attributes["max"] - len(self._queue)
            for _ in range(more):
                self._queue = self._queue[:-1]
        else:
            pass

        for index, item in enumerate(self._queue, -len(self._queue)):
            index = abs(index) - 1
            if self._queue[index] is not None:
                self._next_item_pointer = index
            if self._queue[index] is None:
                self._free_pointer = index

    def enqueue(self, item):
        if not self.is_full():
            if self._attributes["type"] == "fixed":
                if self._free_pointer == self._attributes["max"] - 1:
                    self._queue[-1] = item
                    self._free_pointer = None
                else:
                    self._queue[self._free_pointer] = item
                    self._free_pointer += 1
            else:
                self._queue[self._free_pointer] = item
                self._free_pointer = (self._free_pointer + 1) % self._attributes["max"]
            if self._next_item_pointer == -1:
                self._next_item_pointer += 1
        else:
            raise IndexError("No free spaces in queue")

    def dequeue(self):
        if not self.is_empty():
            if self._attributes["type"] == "fixed":
                if self._next_item_pointer == self._attributes["max"] - 1:
                    self._next_item_pointer = None
                    to_return = self._queue[-1]
                    self._queue[-1] = None
                else:
                    to_return = self._queue[self._next_item_pointer]
                    self._queue[self._next_item_pointer] = None
                    self._next_item_pointer += 1
            else:
                to_return = self._queue[self._next_item_pointer]
                self._queue[self._next_item_pointer] = None
                self._next_item_pointer = (self._next_item_pointer + 1) % self._attributes["max"]
            return to_return
        else:
            raise IndexError("No elements in queue to dequeue")

    def is_full(self) -> bool:
        if self._attributes["type"] == "fixed":
            if self._free_pointer is None:
                return True
            else:
                return False
        else:
            if self._free_pointer == self._next_item_pointer:
                return True
            else:
                return False

    def is_empty(self) -> bool:
        count = 0
        for element in self._queue:
            if element is None:
                count += 1
        if self._attributes["type"] == "fixed":
            if count == len(self._queue) and not self.is_full():
                return True
            else:
                return False
        else:
            if count == len(self._queue):
                return True
            else:
                return False

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return repr(self._queue)

    def __str__(self):
        return str(self._queue)

    def __eq__(self, comparison):
        if self == comparison or self._queue == comparison:
            return True
        else:
            return False

    def __ne__(self, comparison):
        return not self.__eq__(comparison)

    @property
    def data(self):
        return self._queue

    @data.setter
    def data(self, items):
        self._queue = items
        self._attributes["max"] = len(self._queue)

    @property
    def pointers(self):
        return self._free_pointer, self._next_item_pointer

    @pointers.setter
    def pointers(self, items):
        self._free_pointer = items[0]
        self._next_item_pointer = items[1]


class Array(list):
    def __init__(self, *args):
        super().__init__(args)
        self._nested = (type(self) == self.type())
        self._dimensions = 1

    def __repr__(self) -> str:
        dimensioning = True
        test = self[0]
        while dimensioning:
            try:
                test = test[0]
                self._dimensions += 1
            except IndexError:
                dimensioning = False
        if self._nested:
            return f"{self._dimensions}DArray{super().__repr__()}"
        else:
            return f"Array{super().__repr__()}"

    def __setitem__(self, index, value):
        raise TypeError("'Array' object does not support item assignment")

    def __delitem__(self, index):
        raise TypeError("'Array' object does not support item deletion")

    def append(self, value):
        raise TypeError("'Array' object does not support append operation")

    def extend(self, values):
        raise TypeError("'Array' object does not support extend operation")

    def insert(self, index, value):
        raise TypeError("'Array' object does not support insert operation")

    def remove(self, value):
        raise TypeError("'Array' object does not support remove operation")

    def pop(self, index=-1):
        raise TypeError("'Array' object does not support pop operation")

    def clear(self):
        raise TypeError("'Array' object does not support clear operation")

    def copy(self):
        pass

    def count(self, __value):
        pass

    def sort(self, *, key=None, reverse=False):
        pass

    def __reversed__(self):
        pass

    def __reduce__(self):
        pass

    def checkType(self):
        first = self[0]
        for element in self:
            current = element
            if type(first) != type(current):
                raise TypeError("All elements must be the same data type")
        return True

    def __add__(self, other):
        raise TypeError("'Array' object cannot be concatenated'")

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __imul__(self, other):
        pass

    def __eq__(self, other):
        if isinstance(other, Array):
            return self.data == other.data
        raise False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        raise

    def __ge__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    @property
    def data(self) -> tuple:
        return tuple(self)

    @property
    def type(self):
        return type(self[0])


class EasyArray:
    def __init__(self, items: list, dataType: str = None) -> None:
        self._array = items
        self._type = dataType
        types = {"str": 1,
                 "int": 3,
                 "float": 3,
                 "complex": 0,
                 "list": 0,
                 "tuple": 3,
                 "range": 0,
                 "dict": 0,
                 "set": 0,
                 "frozenset": 0,
                 "bool": 2,
                 "bytes": 2,
                 "bytearray": 0,
                 "memoryview": 0,
                 "nonetype": 2,
                 "queue": 0,
                 "EasyArray": 1,
                 "Array": 1,
                 "record": 0,
                 "stack": 0,
                 "tree": 0,
                 "graph": 0,
                 "hash": 0}
        if self._type is None:
            for element in self._array:
                types[repr(type(element)).split("'")[1]] += 1
            sortedTypes = {key: value for key, value in sorted(types.items(), key=lambda item: item[1], reverse=True)}
            testing = True
            temp = [None for _ in range(len(self._array))]
            typeIndex = 0
            while testing:
                greatest = list(sortedTypes.keys())[typeIndex]
                try:
                    for index, data in enumerate(self._array):
                        exec(f"temp[index] = {greatest}(data)")
                    self._array = temp
                    testing = False
                except ValueError:
                    typeIndex += 1
                if typeIndex == len(sortedTypes):
                    raise TypeError("Elements can not all be classified under one data type")
            self._type = list(sortedTypes.keys())[typeIndex]
        else:
            try:
                self._type = str(self._type)
            except ValueError:
                raise TypeError("Type argument must be a string")
            count = 0
            for t in types:
                if self._type.lower() == t:
                    self._type = self._type.lower()
                else:
                    count += 1
            if count == len(types) and self._type is not None:
                raise TypeError("Invalid data type for the array")
            for i in range(len(self._array)):
                exec(f"self._array[i] = {self._type}(self._array[i])")

    def __getitem__(self, index: int):
        if type(index) == "int":
            raise IndexError("Index must be an integer")
        else:
            if 0 <= index < len(self._array):
                return self._array[index]
            else:
                raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if 0 <= index < len(self._array):
            if type(value) != type(self._array[0]):
                try:
                    exec(f"value = {self._type}(value)")
                except ValueError:
                    raise TypeError(f"Value must be able to be casted to a {self._type}")
            self._array[index] = value
        else:
            raise IndexError("Index out of range")

    def __len__(self) -> int:
        return len(self._array)

    def __repr__(self):
        return repr(self._array)

    def __str__(self) -> str:
        return str(self._array)

    def __eq__(self, comparison) -> bool:
        if self == comparison or self._array == comparison:
            return True
        else:
            return False

    def __ne__(self, comparison) -> bool:
        return not self.__eq__(comparison)

    @property
    def data(self) -> list:
        return self._array


# TODO: fix all this and fill in any pass's i have
class stack(list):
    def __init__(self, data: list = None, maximum: int = None):
        super().__init__(data)
        self._stack = super().copy()
        self._max: int = maximum

    def __repr__(self):
        return repr(self._stack)

    def __contains__(self, item):
        return item in self._stack

    def __iter__(self):
        return iter(self._stack)

    def __hash__(self):
        return hash(self._stack)

    def __len__(self) -> int:
        return len(self._stack)

    def append(self, data):
        self.push(data)

    def extend(self, __iterable):
        for item in __iterable:
            self.append(item)
            self._max += 1

    def insert(self, __index, __object):
        raise IndexError("'stack' object cannot be inserted")

    def remove(self, index):
        self.pop()

    def pop(self, index=0):
        if not self.is_empty():
            self._stack.pop(0)
            return super().pop(0)
        else:
            raise IndexError("Cannot pop from an empty stack")

    def clear(self):
        while not self.is_empty():
            self.pop()

    def copy(self):
        temp = []
        for i in range(len(self._stack)):
            temp.append(self.pop())
        new = stack(maximum=self._max)
        temp = temp.reverse()
        for item in temp:
            new.push(item)
            self.push(item)

    def count(self, __value):
        super().count(__value)

    def sort(self, *, key=None, reverse=False):
        raise TypeError("'stack' object cannot be sorted")

    def reverse(self):
        super().reverse()

    def push(self, item):
        super().insert(0, item)
        self._stack.insert(0, item)

    def peak(self):
        if not self.is_empty():
            return self._stack[0]
        else:
            return None

    def is_empty(self) -> bool:
        if len(self._stack) == 0:
            return True
        else:
            return False

    def is_full(self) -> bool:
        if len(self._stack) == self._max:
            return True
        else:
            return False

    def __add__(self, item):
        self.push(item)
        return self._stack

    def __radd__(self, other):
        self.__add__(other)

    def __iadd__(self, other):
        self.__add__(other)

    def __mul__(self, other):
        raise TypeError("'stack' object cannot be multiplied")

    def __rmul__(self, other):
        self.__mul__(other)

    def __imul__(self, other):
        self.__mul__(other)

    def __eq__(self, other):
        if super() == other or self._stack == other or self == other:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if len(self._stack) > len(other):
            return True
        else:
            return False

    def __ge__(self, other):
        if len(self._stack) >= len(other):
            return True
        else:
            return False

    def __lt__(self, other):
        if len(self._stack) < len(other):
            return True
        else:
            return False

    def __le__(self, other):
        if len(self._stack) <= len(other):
            return True
        else:
            return False

    @property
    def data(self) -> list:
        return self._stack

    @data.setter
    def data(self, new):
        if type(new) == list:
            self._stack = new
            for i in range(len(self._stack)):
                super().pop()
            for item in self._stack:
                super().append(item)
        else:
            try:
                self._stack = list(new)
                for i in range(len(self._stack)):
                    super().pop()
                for item in self._stack:
                    super().append(item)
            except TypeError:
                raise TypeError("Replacement stack data cannot be implemented as a stack")

    @property
    def type(self):
        return type(self._stack[0])

    @type.setter
    def type(self, t):
        for index, element in enumerate(self._stack):
            try:
                exec(f"self._stack[index] = {t}({element})")
            except NameError:
                raise TypeError(f"parameter {t} is not a valid type")
        for i in range(len(self._stack)):
            super().pop()
        for element in self._stack:
            super().append(element)

    def __reduce__(self): raise NotImplementedError("this weird tell me please")
    def __subclasshook__(cls, __subclass): raise NotImplementedError("this weird tell me please")
    def __dir__(self): raise NotImplementedError("this weird tell me please")
    def __class__(self): raise NotImplementedError("this weird tell me please")
    def __or__(self, other): raise TypeError(f"'stack' object cannot be compared")
    def __and__(self, other): raise TypeError(f"'stack' object cannot be compared")
    def __cmp__(self, other): raise TypeError(f"'stack' object cannot be compared")
    def __ior__(self, other): raise TypeError(f"'stack' object cannot be compared")
    def __new__(cls): raise NotImplementedError("this weird tell me please")
    def __setattr__(self, __name: str, __value) -> None: raise NotImplementedError("this weird tell me please")
    def __delattr__(self, __name: str) -> None: raise NotImplementedError("this weird tell me please")
    def __format__(self, __format_spec: str) -> str: raise NotImplementedError("this weird tell me please")
    def __getattribute__(self, __name: str): raise NotImplementedError("this weird tell me please")
    def __sizeof__(self) -> int: raise NotImplementedError("this weird tell me please")
    def __init_subclass__(cls) -> None: raise NotImplementedError("this weird tell me please")
    def __getitem__(self, item): raise TypeError("'stack' object cannot be indexed")
    def __setitem__(self, key, value): raise TypeError("'stack' object cannot be indexed")
    def __delitem__(self, key): raise TypeError("'stack' object cannot be indexed")
    def __del__(self): raise NotImplementedError("if you get this error message tell me please")


'''
class linkedList(list):
    def __init__(self, listType="single"):
        super().__init__()
        self._head = None
        self._type = listType
        if self._type != "double" and self._type != "circular" and self._type != "single":
            raise TypeError("'linkedList' object can only be of type single, double or circular.")

    def __repr__(self):
        return f"linkedList{super().__repr__()}"

    def __contains__(self, item):
        for node in self:
            if node.data == item:
                return True
        return False

    def __getitem__(self, item):
        next = self._head.next
        if "-" not in str(item):
            for i in range(item):
                next =

#TODO: i dont get linked lists like how do i get the nodes and list to communicate or should i scrap nodes idk

    def __setitem__(self, key, value):
        self[self._next.index(key)] = value

    def __delitem__(self, key):


    def __iter__(self):
        pass

    def __hash__(self):
        pass

    def __len__(self):
        pass

    def append(self, __object):
        pass

    def extend(self, __iterable):
        pass

    def insert(self, __index, __object):
        pass

    def remove(self, __value):
        pass

    def pop(self, __index=-1):
        pass

    def clear(self):
        pass

    def count(self, __value):
        pass

    def sort(self, *, key=None, reverse=False):
        pass

    def reverse(self):
        pass

    def __reversed__(self):
        pass

    def __reduce__(self):
        pass

    def head(self):
        pass

    def tail(self):
        pass

    def traverse(self):
        pass

    def __add__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __imul__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    @property
    def data(self):
        pass

    @property
    def type(self):
        pass

    @property
    def order(self):
        pass


class Node:
    def __init__(self, data):
        self._data = data
        self._next = None
        self._previous = None

    def __repr__(self):
        return repr(self._data)

    def __contains__(self, item):
        return self._data == item

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new):
        self._data = new

    @property
    def type(self):
        return type(self._data)

    @type.setter
    def type(self, new):
        exec(f"self._data = {new}(self._data)")

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new):
        self._next = new

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, new):
        self._previous = new
'''

'''
class tree:
# binary search and binary

class graph:

class heap:

class matrix:

class record:
'''

# yo ben so you have to fill in the methods that have pass in them and them continue through data structures
