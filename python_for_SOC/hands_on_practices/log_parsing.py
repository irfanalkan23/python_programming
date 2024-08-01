import re  # importing the re module to be able to use regex expression functions

# Parsing one log entry practice:

# read log entry
log_entry = "Jul 27 12:25:18 websystem sshd[29172]: Received disconnect from 218.92.0.97 port 59219:11:  [preauth]"

# create the pattern for parsing
pattern = r'(?P<datetime>[A-Z][a-z]{2} \d{1,2} \d{2}:\d{2}:\d{2}) (?P<hostname>\S+) (?P<processname>\S+)\[(?P<processid>\d+)\]: (?P<logmessage>.+)'

# apply the pattern to your log entry
match = re.match(pattern, log_entry)

# displayed each group from the match
if match:
    print(f'Date and Time: {match.group(1)}')
    print(f'Hostname: {match.group(2)}')
    print(f'Service: {match.group(3)}')
    print(f'PID: {match.group(4)}')
    print(f'Log Message: {match.group(5)}')

"""
 The prompt to give too the AI to generate the regex for paring log files:

 Generate a Python regex pattern to match log entries with groups: 
    date and time ('Month Day HH:MM:SS')
    hostname, 
    process name, 
    process ID (number in square brackets), 
    and log message. 

 Store the pattern in a variable named pattern.
 In your response only give me the regex and nothing else 

"""