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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

call_numbers = {}
for call in calls:
    call_numbers[call[0]] = True
for call in calls:
    if call[1] in call_numbers:
        call_numbers[call[1]] = False
for text in texts:
    if text[0] in call_numbers:
        call_numbers[text[0]] = False
for text in texts:
    if text[1] in call_numbers:
        call_numbers[text[1]] = False


outgoing_call_numbers = set()
for k, v in call_numbers.items():
    if v:
        outgoing_call_numbers.add(k)

print('These numbers could be telemarketers:')
for num in sorted(outgoing_call_numbers):
    print(num)
