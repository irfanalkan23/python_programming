file_path = '../files/network_devices.txt'

file = open(file_path, 'r')

for line in file:
    print(line.strip())

file.close()

print('----------------------------------------------------------------')

with open(file_path, 'r') as file:
    for line in file:
        print(line.strip())