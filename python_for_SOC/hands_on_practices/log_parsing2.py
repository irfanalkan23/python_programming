# parsing the full log file (all the entries)

"""
In this example, we will parse SSH authentication log file (auth.log)

We will write a script that can show us how many failed attempts the IP addresses tried to log into our server
"""

import re  # importing the re module to be able to use regex expression functions
from collections import defaultdict
# importing the defaultdict which can be our data structure to store all the failed entries


log_file_path = '../files/auth.log'  # locating the log file

pattern = r'Failed password.*from (\d+\.\d+\.\d+\.\d+)'  # regex to extract the Failed Password logs

failed_attempts = defaultdict(int)  # created this to hold the number of failed attempts


with open(log_file_path, 'r') as file:  # read the file in python
    for line in file:  # getting each log entry from the log file
        match = re.search(pattern, line) # apply the pattern to get the failed password attempts
        if match:  # if the pattern was found in the line
            ip_address = match.group(1) # get the IP address
            failed_attempts[ip_address] += 1 # add the failed password attempts



for ip, count in failed_attempts.items(): # gives the ip address and how many times the IP address was attempted to login
    print(f'{ip} ====> {count} times failed attempts')

"""
The prompt that I gave to create the pattern that can extract only Failed password entries: 
Create a Python regex pattern to match 'Failed password' log entries, capturing the IP address.

store it into the variable pattern.
In your response only include the regex and nothing else 
"""

# to check the details of the IP address: https://www.virustotal.com/gui/home/search
# to check the reputation of the IP: https://www.ipqualityscore.com/ip-reputation-check