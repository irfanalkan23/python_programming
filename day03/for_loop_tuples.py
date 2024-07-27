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

print('------------------ unpacking a tuple ------------------')

my_tuple = ('apple', 'banana', 'cherry')
fruit1, fruit2, fruit3 = my_tuple
print(fruit1, fruit2, fruit3)  # apple banana cherry

print('------------------ using * operator to unpack a tuple ------------------')

fruits = ('apple', 'banana', 'cherry', 'date', 'elderberry')
fruit1, *fruits_remaining = fruits
print(fruit1)  # apple
print(fruits_remaining)  # ['banana', 'cherry', 'date', 'elderberry']


devices = [
    ("Router1","192.168.1.1","Online"),
    ("Switch1","192.168.1.2","Online"),
    ("Firewall","192.168.1.3","Offline"),
    ("Server1","192.168.1.4","Online"),
]

for device, ip, status in devices:
    print(f"Device: {device}, IP: {ip}, Status: {status}")

# find online devices
online_devices = [device for device, ip, status in devices if status == "Online"]
print("Online Devices:", online_devices)

# find total number of online and offline devices
total_devices = len(devices)
online_devices_count = len(online_devices)
offline_devices_count = total_devices - online_devices_count
print(f"Total Devices: {total_devices}, Online Devices: {online_devices_count}, Offline Devices: {offline_devices_count}")

# find average IP address

