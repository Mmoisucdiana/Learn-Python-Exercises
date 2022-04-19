# This is a sample Python script.

#Regular expression

#Write a Python program that matches a string that has an a followed by zero or more b's.

import re
def text_match(text):
    patterns='^a(b*b)$'
    if re.search(patterns,text):
        return'Found a match!'
    else:
        return('Not matched!')
print(text_match('bb'))
print(text_match('ab'))
print(text_match('abc'))
print(text_match('abb'))
print(text_match('ba'))

#Write a Python program that matches a string that has an a followed by one or more b's.

import re
def text_match(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab"))
print(text_match("abc"))
print(text_match("a"))


#Verify the email

import re
def text_match(email):
    patterns='[a-zA-Z0-9]+@[a-zA-Z]+\.(com|org|net)'
    if re.search(patterns, email):
        return"Valid Email"
    else:
        return("Invalid Email")

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
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab"))
print(text_match("abc"))
print(text_match("abbc"))
print(text_match("aabbc"))
print(text_match("a"))
print(text_match("aaa"))


import re
def text_match(text):
        patterns = 'ab{3}'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match('abbb'))
print(text_match('abb'))

#Write a Python program that matches a string that has an a followed by two to three 'b'.

import re
def text_match(text):
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match('abbb'))
print(text_match('abb'))
print(text_match('ab'))

#Write a Python program that matches a string that has an a followed by two to five 'b'. #EXTRA
def text_match(text):
    patterns = 'ab{2,5}'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match('abbb'))
print(text_match('abb'))
print(text_match('ab'))



#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))

#Write a Python program to find sequences of uppercase letters joined with a underscore. #EXTRA
import re
def text_match(text):
        patterns = '^[A-Z]+_[A-Z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("AAAA_AABBC"))

#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

import re
def text_match(text):
        patterns = '^[A-Z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("A_abc"))


#9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'. Go to the editor
import re
def text_match(text):
        patterns = '^a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))


#Write a Python program that matches a word at the beginning of a string.

# "\w"-func.for word

import re
def text_match(text):
        patterns = '^\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match(" quick brown fox jumps over the lazy dog."))


#10. Write a Python program that matches a word at the beginning of a string.
import re
def text_match(text):
        patterns = '\w+\S*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("The quick brown fox jumps over the lazy dog. "))
print(text_match("The quick brown fox jumps over the lazy dog "))



#Write a Python program that matches a word at the end of a string, with "!" EXTRA
import re
def text_match(text):
        patterns = '\w+\S*!'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("The quick brown fox jumps over the lazy dog. "))
print(text_match("The quick brown fox jumps over the lazy dog!"))


#12. Write a Python program that matches a word containing 'z'.
import re
def text_match(text):
        patterns =("\w*z.\w*")
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ozone"))


#13. Write a Python program that matches a word containing 'z', not at the start or end of the word.
import re
def text_match(text):
        patterns = '\Bz\B'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python Exercises."))

#13. Write a Python program that matches a word containing 'z', not at the start or end of the word.
import re
def text_match(text):
        patterns = '\Bz'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python Exercises."))

#14. Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re
def text_match(text):
        patterns = "[A-Z,a-z,0-9,+_]"
        if re.search(patterns,text):
                return 'Found a match!'
        else:
                return('Not matched!')


#15. Write a Python program where a string will start with a specific number.

import re
def num_match(string):
        text=re.compile(r"^5")
        if text.match(string):
                return True
        else:
                return False
print(num_match('5-23456'))
print(num_match('6-78918'))


#16. Write a Python program to remove leading zeros from an IP address.

import re
def removeZeros(ip):
        new_ip=re.sub(r'\b0+(\d)',r'\1',ip)
        return new_ip
ip='100.002.003.450'
print(removeZeros(ip))

ip2='001.044.006.46'
print(removeZeros(ip2))

import re
ip = "216,08,094,196"
string = re.sub('\,[0]*', ',', ip)
print(string)


#17. Write a Python program to check for a number at the end of a string.
def num_match(string):
        text=re.compile(r".*[0-9]$")
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



