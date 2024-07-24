print(help(input))

name=input('Enter your name:\n')

print(f'Your name is {name}')

age=int(input('Enter your age:\n'))

print(f'Your age is {age}')

print(age * 3)

print('-----------------------')

number=int(input('Enter a number:\n'))
result=None
if number > 0:
    result='Positive'
elif number < 0:
    result='Negative'
else:
    result='Zero'
print(result)