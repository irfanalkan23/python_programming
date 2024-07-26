print('Test1 started')

name = 'Python'

try:
    print(name[100])
except:
    print('Something went wrong')

print('Test1 completed')

"""
Test1 started
Something went wrong
Test1 completed
"""

print('-----------------------------')

print('Test2 started')

try:
    print(1/0)
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')

print('Test2 completed')

"""
Test2 started
Something went wrong
Test2 completed
"""

print('-----------------------------')

print('Test3 started')

try:
    print(1/1)
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')

print('Test3 completed')

"""
Test3 started
1.0
Nothing went wrong
Test3 completed
"""

print('-----------------------------')

print('Test4 started')

try:
    print('Python'[50])
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
finally:
    print('"finally" codes are executed')

print('Test4 completed')

"""
Test4 started
Something went wrong
"finally" codes are executed
Test4 completed
"""

print('-----------------------------')

age = int(input('Enter your age:\n'))

if age <=0:
    raise Exception(f'Invalid age is given: {age}')

print(f'Your age is {age} years old')