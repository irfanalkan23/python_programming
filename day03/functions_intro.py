import numbers


def square(side):
    return side * side


print(square(4))


def multiply(a: numbers = 0, b: numbers = 0):
    return a * b


x = multiply()
print(x)

y = multiply(5,5)
print(y)