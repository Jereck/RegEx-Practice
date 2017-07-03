import re

text_file = open("file.txt", encoding="utf-8")
data = text_file.read()
text_file.close()

first_name = r'Jake'
last_name = r'Reck'

print(re.match(last_name, data))
print(re.search(first_name, data))

#FIND NAMES
print(re.findall(r'\w*, \w+', data))
#FIND PHONE NUMBERS
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-?\s?\d{4}', data))
#FIND EMAIL ADDRESSES
print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))