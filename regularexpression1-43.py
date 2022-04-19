# Regular expression

# Write a Python program that matches a string that has an a followed by zero or more b's.

import re


def text_match(text):
    patterns = '^a(b*b)$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match('bb'))
print(text_match('ab'))
print(text_match('abc'))
print(text_match('abb'))
print(text_match('ba'))

# Write a Python program that matches a string that has an a followed by one or more b's.

import re


def text_match(text):
    patterns = 'ab+?'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("ab"))
print(text_match("abc"))
print(text_match("a"))

# Verify the email

import re


def text_match(email):
    patterns = '[a-zA-Z0-9]+@[a-zA-Z]+\.(com|org|net)'
    if re.search(patterns, email):
        return "Valid Email"
    else:
        return ("Invalid Email")


print(text_match("marius@gmail.com"))

import re


def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)


print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("*&%@#!}{"))

import re


def text_match(text):
    patterns = 'ab?'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("ab"))
print(text_match("abc"))
print(text_match("abbc"))
print(text_match("aabbc"))
print(text_match("a"))
print(text_match("aaa"))

import re


def text_match(text):
    patterns = 'ab{3}'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match('abbb'))
print(text_match('abb'))

# Write a Python program that matches a string that has an a followed by two to three 'b'.

import re


def text_match(text):
    patterns = 'ab{2,3}'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match('abbb'))
print(text_match('abb'))
print(text_match('ab'))


# Write a Python program that matches a string that has an a followed by two to five 'b'. #EXTRA
def text_match(text):
    patterns = 'ab{2,5}'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match('abbb'))
print(text_match('abb'))
print(text_match('ab'))

# Write a Python program to find sequences of lowercase letters joined with a underscore.

import re


def text_match(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))

# Write a Python program to find sequences of uppercase letters joined with a underscore. #EXTRA
import re


def text_match(text):
    patterns = '^[A-Z]+_[A-Z]+$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("AAAA_AABBC"))

# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re


def text_match(text):
    patterns = '^[A-Z]+_[a-z]+$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("A_abc"))

# 9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'. Go to the editor
import re


def text_match(text):
    patterns = '^a.*?b$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))

# Write a Python program that matches a word at the beginning of a string.

# "\w"-func.for word

import re


def text_match(text):
    patterns = '^\w+'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match(" quick brown fox jumps over the lazy dog."))

# 10. Write a Python program that matches a word at the beginning of a string.
import re


def text_match(text):
    patterns = '\w+\S*$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("The quick brown fox jumps over the lazy dog. "))
print(text_match("The quick brown fox jumps over the lazy dog "))

# Write a Python program that matches a word at the end of a string, with "!" EXTRA
import re


def text_match(text):
    patterns = '\w+\S*!'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("The quick brown fox jumps over the lazy dog. "))
print(text_match("The quick brown fox jumps over the lazy dog!"))

# 12. Write a Python program that matches a word containing 'z'.
import re


def text_match(text):
    patterns = ("\w*z.\w*")
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("ozone"))

# 13. Write a Python program that matches a word containing 'z', not at the start or end of the word.
import re


def text_match(text):
    patterns = '\Bz\B'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python Exercises."))

# 13. Write a Python program that matches a word containing 'z', not at the start or end of the word.
import re


def text_match(text):
    patterns = '\Bz'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("The quick fox jumps over the lazy dog."))
print(text_match("Python Exercises."))

# 14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re


def text_match(text):
    patterns = "[A-Z,a-z,0-9,+_]"
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


# 15. Write a Python program where a string will start with a specific number.

import re


def num_match(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False


print(num_match('5-23456'))
print(num_match('6-78918'))

# 16. Write a Python program to remove leading zeros from an IP address.

import re


def removeZeros(ip):
    new_ip = re.sub(r'\b0+(\d)', r'\1', ip)
    return new_ip


ip = '100.002.003.450'
print(removeZeros(ip))

ip2 = '001.044.006.46'
print(removeZeros(ip2))

import re

ip = "216,08,094,196"
string = re.sub('\,[0]*', ',', ip)
print(string)


# 17. Write a Python program to check for a number at the end of a string.
def num_match(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False


print(num_match('abc56'))
print(num_match('bc78918'))
print(num_match('bcdef'))

import re

import re

results = re.finditer(r'([0-9]{1,3})', "Exercises number 1, 12, 13, and 34 are important")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))

#19. Write a Python program to search some literals strings in a string. Go to the editor

import re

patterns = ['fox', 'dog', 'horse','cat']
text = 'The quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text), )
    if re.search(pattern, text):
        print('Matched!')
    else:
        print('Not Matched!')


#20.Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.
import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % \
    (match.re.pattern, match.string, s, e))


#21.Write a Python program to find the substrings within a string.

import re

text = 'Python project, PHP project, C# project'
pattern = 'project'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)


#23. Write a Python program to replace whitespaces with an underscore and vice versa
import re
text="Master Project"
text=text.replace(" ","_")
print(text)

text=text.replace("_"," ")
print(text)


#Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

import re
def date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",date_format(dt1))


#26. Write a Python program to match if two words from a list of words starting with letter 'P'.
import re
text = 'Python project, PHP project, C# project'
def text_match(text):
    patterns = '^P'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')



import re

# Sample strings.
words = ["Python project", "Java project","PHP project"]

for w in words:
    m = re.match("(P\w+)\W(P\w+)", w)
    # Check for success
    if m:
        print(m.groups())

#27. Write a Python program to separate and print the numbers of a given string
import re
# Sample string.
text1 = "Five 5, Twenty 20, Thirty 30"
result = re.split("\D+", text1)
# Print results.
for element in result:
    print(element)
#27. Write a Python program to separate and print the text of a given string #Extra

# Sample string.
text1 = "Five 5, Twenty 20, Thirty 30"
result = re.split("\s+", text1)
# Print results.
for element in result:
    print(element)

#28. Write a Python program to find all words starting with 'a' or 'e' in a given string. Go to the editor
str="Amber,Elen, Alice,Mark"
name = re.findall("[ae]\w+", str)
print(name)

#Write a Python program to separate and print the numbers and their position of a given string
import re
text="Write a Python program to separate and print the numbers 60,70,90 and their position of a given string"
for p in re.finditer("\d+", text):
    print(p.group(0))
    print("Index position:", p.start())

#Write a Python program to abbreviate 'Italy' as 'IT.' in a given string.
country="Made in Italy"
abr=re.sub("Italy","IT",country)
print(abr)

#Write a Python program to replace all occurrences of space, comma, or dot with a line
country="Made in Italy"
replace1=re.sub("[ ,.]","|",country)
print(replace1)


#33. Write a Python program to find all five characters long word in a string.

text="Write a Python program to find all five characters long word in a string"
abr=re.findall(r"\b\w{5}\b",text)
print(abr)

#34. Write a Python program to find all three, four, five characters long words in a string
text="Write a Python program to find all five characters long word in a string"
abr=re.findall(r"\b\w{3,5}\b",text)
print(abr)


#35. Write a Python program to find all words which are at least 4 characters long in a string.
text="Write a Python program to find all five characters long word in a string"
abr=re.findall(r"\b\w{4,}\b",text)
print(abr)


#35. Write a Python program to find all words which are maximum 4 characters long in a string. #Extra
text="Write a Python program to find all five characters long word in a string"
abr=re.findall(r"\b\w{,4}\b",text)
print(abr)

#36. Write a python program to convert camel case string to snake case string


import re

def change_case(str):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

str = "PythonForWork"
print(change_case(str))

#37. Write a python program to convert snake case string to camel case string.
import re

def change_case(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(change_case("Python_For_Work"))


import re
txt = '"Python", "Excel", "PowerBI"'
print(re.findall(r'"(.*?)"', txt))


#39. Write a Python program to remove multiple spaces in a string.
text="Write  a  Python  program  to  find  all  five characters  long word in a string"

def change_case(text):
    return ''.join(x.capitalize() or ' ' for x in text.split(' '))
print(change_case(text))


#40. Write a Python program to remove all whitespaces from a string.

text="Write a Python program to find all five characters long word in a string"

def change_case(text):
    return ''.join(x.capitalize() or ' ' for x in text.split(' '))
print(change_case(text))


#41.Write a Python program to remove everything except alphanumeric characters from a string.

import re
txt = '**//good dashboard// - 14.8! '
pattern = re.compile('[\W_]+')
print(pattern.sub('', txt))


#42. Write a Python program to find urls in a string.
import re
url = "http://workapps.com ?rvf5"
url_true = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url)
print(url_true)


#43. Write a Python program to split a string at uppercase letters.
uppercase = "PythonForWork"

print(re.findall('[A-Z][^A-Z]*', uppercase))

#43. Write a Python program to output just the first uppercase letters #Extra
print(re.findall('[A-Z][^a-z]*', uppercase))

