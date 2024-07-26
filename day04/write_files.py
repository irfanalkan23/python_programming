file = open('write_files_same_dir.txt','w')

file.write('Fourth line')

file = open('write_files_same_dir.txt','r')
print(file.read())

file.close()