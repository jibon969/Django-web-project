
# Start :- 12:37 PM 6/14/2019

# OS Module in python

import os
import time

x = dir(os)     # os এর সব Module গুলো দেখতে পারবো ।
print('dir :', x)
print('\n')


# Current dir

y = os.getcwd()     # Current dir
print('Current dir :', y)
print('\n')


# Location

z = os.chdir('C:\\Users\\Jibon Ahmed\\Desktop')
print(os.getcwd() )


# Now create a folder this location
os.mkdir('Folder')


# Create sub folder
os.makedirs("NewFolder/Sub_Folder")


# Remove folder
os.rmdir('Folder')


# Remove Sub_Folder
os.removedirs('NewFolder/Sub_Folder')
print(os.getcwd())
print('\n')


# Example এইখানে আমারা যেকোনো location এর সবকিছু দেখতে পারবো ।
for dir_path, dir_names, file_names, in os.walk('C:\\Users\\Jibon Ahmed\\Desktop'):

    print('Current path :', dir_path)
    print('Directory    :', dir_names)
    print('File Name    :', file_names)
    print('\n')


# Example 2 second পর পর একটি ফোল্ডার create হবে এবং ফোল্ডার এর নাম change  হবে ।


import os
curDir = os.getcwd()
print(curDir)

os.mkdir("newFolder")

import time

time.sleep(2)

os.renames("newFolder", "Jayed")
time.sleep(2)


# End :- 1:02 PM 6/14/2019

