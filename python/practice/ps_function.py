def add(a, b):
    return a + b


a = 3
b = 2
c = add(a, b)
print(c)


def say():
    return 'hi'


print(say())


def addmony(*args):
    result = 0
    for i in args:
        result = result + i
    return result


result = addmony(1, 2, 3)
print(result)

