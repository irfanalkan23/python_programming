import numbers


def square(num: numbers = 0) -> numbers:
    result = num * num
    return result


def cube(num: numbers = 0) -> numbers:
    return square(num) * num

def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
     if operator == '-':
         return num1 - num2
     elif operator == '+':
         return num1 + num2
     elif operator == '*':
         return num1 * num2
     elif operator == '/':
         return num1 / num2
     else:
         print('Invalid operator')
         return 0