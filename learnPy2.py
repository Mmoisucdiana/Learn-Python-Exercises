
#Dictionaries####################################
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)


phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)


phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" %(name,number))

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)

#Numpy Arrays############################

import numpy as np

height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
np_height = np.array(height)
np_weight = np.array(weight)
print(np_height)

print(type(np_height))

bmi=np_height/np_weight **2
print(bmi)

print(bmi>23)
bmi[bmi>23]

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg=np.array(weight_kg)

np_weight_lbs=np_weight_kg * 2.2
print(np_weight_lbs)

dict= {"country":["Brazil",'Italy',"France","Belgium"],
       "area":[8.567,7.789,9.678,6.789],
       "population":[9.89,6.56,7.89,9.05]}
import pandas as pd
brics=pd.DataFrame(dict)
print(brics)
brics.index=["BR","IT","FR","BG"]
print(brics)


#Generators############################
import random

def lottery():
    for i in range(6):
        yield random.randint(1,30)
        yield random.randint(1,20)
for random_number in lottery():
       print("And the next number is.. %d!" %(random_number))


#List Comprehensions#####################
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "lazy"] #the number of letters
print(words)
print(word_lengths)

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [float(x) for x in numbers if x > 0] #only positive number
print(newlist)

for x in range(10):
    # Check if x is even
    if x % 2 == 1:
        continue
    print(x)

count=9
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
# Prints out 1,2,3,4


for i in range(1, 10):
    if(i%6==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
#Call functions###############

def list_avantage():
    return ["More organized code", "More readable code", "Easier code reuse",
            "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(avantage):
    return "%s is a avantage of functions!" %avantage

def name_the_avantage_of_functions():
    list_of_avantage = list_avantage()
    for avantage in list_of_avantage:
        print(build_sentence(avantage))

name_the_avantage_of_functions()



