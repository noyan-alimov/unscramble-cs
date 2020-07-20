"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

tel_numbers = []

for text in texts:
    tel_numbers.append(text[0])

for text in texts:
    tel_numbers.append(text[1])

for call in calls:
    tel_numbers.append(call[0])

for call in calls:
    tel_numbers.append(call[1])


unique_numbers = []

for num in tel_numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(
    f'There are {len(unique_numbers)} different telephone numbers in the records.')
