
file = open('read_file_same_dir.txt','r')  # same directory

text = file.read()
# after using read() or readline() methods, you can not read again!

print(text)

print('------------------')

file = open('read_file_same_dir.txt','r')

first_line = file.readline()
print(first_line)

second_line = file.readline()
print(second_line)

print('------------------')

file = open('read_file_same_dir.txt','r')

for x in file.readlines():
    print(x)

file.close()