import inspect
lines = inspect.getsource(tuple.__new__())
print(lines)
