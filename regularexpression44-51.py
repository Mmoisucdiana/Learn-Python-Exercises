# 44. Write a Python program to do a case-insensitive string replacement.
import re

import re

txt = "Python program"
print("Txt: ", txt)
redata = re.compile(re.escape('Python'), re.IGNORECASE)
new_txt = redata.sub('Python', 'PY program')
print("Using 'Python' replace PY")
print("TXT_new: ", new_txt)

# 46. Write a Python program to find all adverbs and their positions in a given sentence. Go to the editor

# Sample text : "Clearly, he has no excuse for such behavior."

import re

txt1 = "Clearly, he has no excuse for such behavior."
for n in re.finditer(r"\w+ly", txt1):
    print('%d-%d: %s' % (n.start(), n.end(), n.group(0)))

# 47. Write a Python program to split a string with multiple delimiters.
txt2 = "Clearly, he has no excuse for such behavior."
print(re.split(', |, |\*|\n', txt2))

# 48. Write a Python program to check a decimal with a precision of 2.
number = 3.567
print("The value of number till 2 decimal place is:", end="")
print('%.2f' % number)


def is_decimal(num):
    numre = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    decimal = numre.search(num)
    return bool(decimal)


print(is_decimal('2.345'))
print(is_decimal('2.34'))


# 48. Write a Python program to check a decimal with a precision of 4.#Extra
def is_decimal(num):
    numre = re.compile(r"""^[0-9]+(\.[0-9]{1,4})?$""")
    decimal = numre.search(num)
    return bool(decimal)


print(is_decimal('2.3456'))
print(is_decimal('2.34'))

# 49. Write a Python program to remove words from a string of length between 1 and a given number.

import re

txt = "Clearly, he has no excuse for such behavior."
deletestr = re.compile(r'\W*\b\w{1,4}\b')
print(deletestr.sub('', txt))

# 49. Write a Python program to remove words from a string of length between 2 and 3.#EXTRA
import re

txt0 = "Clearly he has no excuse for such behavior."
deletestr = re.compile(r'\W*\b\w{2,3}\b')
print(deletestr.sub('', txt0))

# 50. Write a Python program to remove the parenthesis area in a string. Go to the editor


import re

items = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for item in items:
    print(re.sub(r" ?\([^)]+\)", "", item))


