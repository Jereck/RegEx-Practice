import re

text_file = open("file.txt", encoding="utf-8")
data = text_file.read()
text_file.close()

#FIND NAMES
print(re.findall(r'\w*, \w+', data))

#FIND PHONE NUMBERS
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-?\s?\d{4}', data))

#FIND EMAIL ADDRESSES
print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))

#FIND ALL GMAIL ADDRESSES
print(re.findall(r'\b[gmail]+\b', data, re.I))

#LEAVE OFF EMAIL ADDRESSES WITH .aol
print(re.findall(r'''
	\b@[-\w\d.]* 	# Find a word boundry, an @, and any number of characters
	[^aol\t]+ 		# Ignore 1 or more instances of letters aol
	\b 				# Match another word boundry
	''', data, re.VERBOSE|re.I))

print(re.findall(r"""
	\b[-\w]+,	# Find a word boundry, 1 or more hyphens or characters, and a comma
	\s 			# Find 1 whitespace
	[-\w ]+		# 1 or more hyphens and characters and explicit spaces
	[^\t\n]		# Ignore tabs and newlines
	""", data, re.X))

#GROUPS
line = re.compile(r'''
	^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t+ 	# Last and First Names
	(?P<email>[-\w\d.+]+@[-\w\d.]+)\t+ 						# Email
	(?P<phone>\(?\d{3}\)?-?\s?\d{3}-?\d{4})$	 			# Phone Number
	''', re.X|re.M)	

print(line.search(data).groupdict())
for match in line.finditer(data):
	print('{first} {last} <{email}>'.format(**match.groupdict()))