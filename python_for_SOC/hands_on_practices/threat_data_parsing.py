import csv
import requests

url = 'https://gitlab.com/exploit-database/exploitdb/-/raw/main/files_exploits.csv'

# sending request
response = requests.get(url)

if response.status_code != 200:  # if the response status code if not 200
    raise RuntimeError(f'Request failed. HTTP status code: {response.status_code}')  # then terminates the program

# Get the CSV data
csv_data = csv.reader(response.text.splitlines())
next(csv_data)  # skipping header

#for i, row in enumerate(csv_data, 1):
#    print(f"{i}. {row[2]}")

sorted_csv_data = sorted(csv_data, key=lambda row: int(row[0]), reverse=True)[:5] # extracting the top 10

for i, exploit in enumerate(sorted_csv_data, 1):
     print(f'{i}. {exploit[2]}') # displays the top 10 exploits titles
     print(exploit)



print("--------------------------------")


def show_latest_exploits(num: int):
    url = 'https://gitlab.com/exploit-database/exploitdb/-/raw/main/files_exploits.csv'

    response = requests.get(url)

    if response.status_code != 200:  # if the response status code if not 200
        raise RuntimeError(f'Request failed. HTTP status code: {response.status_code}')  # then terminates the program

    csv_data = csv.reader(response.text.splitlines())
    next(csv_data)

    sorted_csv_data = sorted(csv_data, key=lambda row: int(row[0]), reverse=True)[:num]

    for i, exploit in enumerate(sorted_csv_data, 1):
        print(f'{i}. {exploit[2]}')
        print(exploit)


show_latest_exploits(20)