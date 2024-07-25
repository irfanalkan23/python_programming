s = 'python'
for each_char in s:
    print(each_char)

for i in range(1, 11):
    print(i)

for x in range(1, 51):
    if x % 2 == 0:
        print(x)

print('----------- Branching Statements: break, continue, pass ----------')

for i in range(1, 11):
    pass

s = 'ABCDEF'
for z in s:
    if z == 'C' or z == 'f':
        pass
    print(z)

print('----------- tuples ----------')

x = ('a', 1)
y = 'b', 2
print(x + y)  #('a', 1, 'b', 2)
print(x * 2)  #('a', 1, 'a', 1)

print(x.index('a'))  #0
print(x.count('a'))  #1
