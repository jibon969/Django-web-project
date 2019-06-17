# Start : 1:32 PM 6/12/2019

# Python dictionary

"""
১. Dictionary ও  list এর মত কাজ করে ।
২. list এ যেমন index কে কল করে আইটেম গুলো পেতাম । আর Dictionary তে key ধরে ভেলু গুলো পাব ।
"""


# Dictionary

"""
1. Constructing a dictionary
2. Accessing objects from a dictionary
3. Nesting dictionary
4. Basic dictionary method
"""


# Example of how to declare dictionary
print('How to declare dictionary :\n')

dict1 = { }     # this is not a set
print(dict1)
print(type(dict1))


d = dict()
print(d)
print(type(d))


myDict = {'key': 'value'}
print('myDict :', myDict)
print('\n')


# Creating Dictionary
print('Creating Dictionary :\n')


dict1 = {'Name': "Python", 'Learn': 'Dictionary'}
print('Dictionary :', dict1)


# Example

d = dict(Name='Jibon',
         phone='01987132197',
         location='Dhaka',
         email='jayed.swe@gamil.com',)
print('Dictionary :', d)


# Example

my_marks = {"Bengali": [30, 35, 32], "English": [45, 52, 33], "Math": [60, 74, 58]}
print('Mark       :', my_marks)
print('\n')


#  How to access item in Dictionary
print('How to access item in Dictionary :\n')

a = {'name': "Python", 'nickname': 'Python 3', 'learn': 'Dictionary'}
print('all      :', a)
print('nickname : ', a['nickname'])
print('learn    :', a['learn'])
print('\n')


# Example of key and values
print('Dictionary key and values :\n')

d = {'name': 'Jayed', 'phone': '01840144627', 'email': 'jayed.swe@gamil.com', 'location': 'DIU'}
print('all      : ', d)
print('Name     :', d['name'])
print('keys     :', d.keys())
print('values   :', d.values())
print("\n")


# How to change or add elements in a dictionary
print("Change or add elements in a dictionary : \n")


person = {'name': 'Jui', 'location': 'Dhaka', 'address': '102/A'}
print('My friend address :', person)

# update items
x = person['location'] = 'Khulna'
print('Update Location   :', person)

# add new item
y = person['email'] = 'jui@gmail.com'
print("add email address : ", person)
print('\n')

a = {"Name ": "Jibon Ahmed ", "location": "Diu", "Dept": "Swe", "Id":  69}

for key, value in a.items():
    print(key, ':', value)

print('\n')


# Dictionary Method
print('Dictionary Method :\n')

a = {'name': "Jibon", 'dept': 'swe', 'id': 69}
b = {'present-address': 'Dhaka', 'post-code': 5600}

print('a          :', a)
print('Value of A :', a.values())
print('keys of  A :', a.keys())
print('Item of  A :', a.items())
print('\n')


print('b          :', b)
print('Value of B :', b.values())
print('keys of  B :', b.keys())
print('Item of  B :', b.items())
print('\n')

print('Department :', a.get('dept'))
print('Id         :', a.get('id'))


# যদি কখনো একটা Dictionary সব আইটেমকে  অন্য একটি Dictionary যোগ করার দরকার হয় তখন আমারা  update() function ব্যবহার করবো

x = a.update(b)
print('a :', a)
print('\n')


# End :- 2:42 PM 6/12/2019

