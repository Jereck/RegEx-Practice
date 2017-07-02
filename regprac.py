import re

text_file = open("file.txt", encoding="utf-8")
data = text_file.read()
text_file.close()

first_name = r'Jake'
last_name = r'Reck'

print(re.match(first_name, data))
print(re.search(last_name, data))