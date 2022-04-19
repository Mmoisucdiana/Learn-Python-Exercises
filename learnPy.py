print("This is a multiline comment")

x = 1
if x == 1:
    print("x is 1")

mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)

mylist = [1, 2, 3]
print("A list: %s" % mylist)

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True:  # else if
    # do something else
    pass
else:
    # do another thing
    pass

for x in range(3, 10, 3):
    print(x)

for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)


def my_function():
    print("Hello From My Function!")


def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))


def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" %benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")



    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
car1= Vehicle()
name="Fer"
kind="convertible"
color="red"
value=60000.00

car2= Vehicle()
name="Jump"
kind="van"
color="blue"
value=10000.00
print(car1.description())
print(car2.description())






