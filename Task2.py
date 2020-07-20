"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""


seconds_list = []

for call in calls:
    seconds_list.append(int(call[3]))

max_seconds = str(max(seconds_list))


def find_number():
    for call in calls:
        if max_seconds in call:
            return call[0]


number = find_number()

print(f'{number} spent the longest time, {max_seconds} seconds, on the phone during September 2016')
