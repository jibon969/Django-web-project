
# Start : -  10:36 PM 6/11/2019
# List comprehension

"""
List comprehension হল এক লাইনে ফর লুপ ব্যবহার করে লিস্ট এর list data structure তৈরি করতে পারবো ।

Syntax :- [ expression for item in list ] or [ expression for val in collection ]
"""
print('\n')


# Example

print('How list comprehension work : \n')
my_list = [ ]
for letter in "Hello":
    my_list.append(letter)
print(my_list)
print('\n')


# Using list comprehension

list1 = [letter for letter in 'World']
print('Using list comprehension :', list1)
print('\n')


# Example of Multiply

n = [n*2 for n in range(1, 10)]
print('Multiply :', n)
print('\n')


# Even number list comprehension

myList = [number for number in range(10) if number % 2 == 0]
print('Even Number :', myList)


# Odd number list comprehension

myList = [number for number in range(10) if number % 2 == 1]
print('Odd Number  :', myList)
print('\n')


# Example

movie = ['pk', 'g', 'h', 'gp', 'boss', 'good']

movies = [title for title in movie if title.startswith('g')]
print('movie list :', movies)
print('\n')


# Example

scenario = """
Consider a Garment system where foreign buyer gives some order to the garment. 
The garment management receives the order and distributes the work to its employees. 
After the completing the task employees send the task to the QC department to check. 
QC checks the work quality and send it back to employee for correction if there is any defect found. 
Employee resolve the defects and re-send the corrected work to the QC again. 
QC checks the corrected work and submit the final report to the management (if the work pass the QC test). 
Management then deliver the shipment the buyer (along with the QC report). 
All user need to log in the system to use it.
"""
print(scenario)

new_list = scenario.split()  # split () দ্বারা আমি প্রত্যেকটি word কে অলাদা অলাদা করলাম ।

find_word = [title for title in new_list if title.startswith('r')]

print('Find word :', find_word)

print('\n')


# End :- 11:41 PM 6/11/2019

