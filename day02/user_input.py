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

print('--------- String --------------')

s='python'
print(len(s))
print(s[-1])
print(s[0:3])  #excludes index 3 --> 'pyt'
#slicing string creates substring
print(s[:3])
print(s[3:])  # 'hon'

print('--------- reverse String --------------')
print(s[::-1])  # 'nohtyp'

print('--------- str class methods --------------')
s.lower()
s.upper()
s.capitalize()  # first character upper case
s.title()       # first character of each word upper case
s.strip()       # remove white spaces at both starting and ending
s.lstrip()      # remove white spaces at the starting
s.rstrip()      # remove white spaces at the end
s.index('p')    # 0
s.rindex('p')   # index of last occurrence
s.replace()
s.count()       # frequency of the given value
s.startswith()  # checks if the string starts with the given value
s.endswith()
s.islower()
s.isupper()
s.isdigit()
s.isalpha()     # checks if all the characters in the string are letters

