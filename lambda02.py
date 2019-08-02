def myfunc(n):
    return lambda b : b * n

doublestack = myfunc(2)

animals = ['cat','dog','mouse']

print(doublestack(animals))
