def no_local_foo():
    exec('foo = "bar"')
    print(locals())
    print(locals()["foo"])

no_local_foo()
