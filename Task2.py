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


def find_number_with_longest_time(calls):
    nums = []
    for call in calls:
        nums.append(call[0])
        nums.append(call[1])

    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)

    unique_nums_obj = {}
    for num in unique_nums:
        unique_nums_obj[num] = 0

    for call in calls:
        if call[0] in unique_nums_obj:
            unique_nums_obj[call[0]] += int(call[3])
        if call[1] in unique_nums_obj:
            unique_nums_obj[call[1]] += int(call[3])

    seconds = []
    for k, v in unique_nums_obj.items():
        seconds.append(v)

    max_seconds = max(seconds)

    number = None
    for k, v in unique_nums_obj.items():
        if max_seconds == v:
            number = k

    return [number, max_seconds]


result = find_number_with_longest_time(calls)


print(f'{result[0]} spent the longest time, {result[1]} seconds, on the phone during September 2016')
