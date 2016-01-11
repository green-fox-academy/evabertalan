# def greet(koszon, name):
#    return koszon + name + '!'
#
#result=greet("Csa ", "Tomi")
#print(result)


# def greet(name, hi):
#    return (hi + ", ") + '!'
#
#greet("Tomi", "hello")
#greet("Tomi", "szia")


# def greet(name, hi=None):
#    if hi is None:
#        hi="Hello"
#    print(hi + ", " + name)
#
#greet("Tomi", "hello")
#greet("Tomi", "szia")
#greet("Tomi", None)
#greet("Tomi")


def greet(name, hi="Hello"):

    print(hi + ", " + name)

greet("Tomi", "hello")
greet("Tomi", "szia")
greet("Tomi")
