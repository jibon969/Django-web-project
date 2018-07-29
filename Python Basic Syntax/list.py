# lists in python
# list is collection of every type of objects in python
# whether it be string integer float it can be anything
# to create a list square brackets are used([])
list=[] #this is an empty list. here we are assigning a list type object to the "list" variable
# this text on the left hand side of the "=" is a variable that means you can give it your name too
print(type(list)) #type is a method which is used to show the type of the object passed rigth into it
# ________OUTPUT_________
# <class 'list'>
#________________________

# now to add element in the list one can do
list.append(3)
# now if you print the list
print(list)
# ________OUTPUT_________
# [3]
# ________OUTPUT_________
# list can be collection of any kind of object that means it can even be a collection of mixed object type also
list.append('s')
# here a character is added to our list and it is perferctly fine
print(list)
# ________OUTPUT_________
# [3,'s']
# ________________________
# there are lot more methods of list