
# File writing in python

# ' W ' Open file write only

# ' Wb' Opens a file for writing only in binary format


#----------------------- Now Create a Text.txt File ----------------------@

'''

file = open('Text.txt', 'w')
file.write('Jibon\n')
file.write('Ahmed\n')
file.write('Kurigram\n')
file.write('Dhaka\n')
file.write('Bangladesh\n')

'''


#---------------------- Another way to write file----------------------------@


with open('Jibon.txt', 'w') as wf:
    wf.write('I am learning......\n')
    wf.write('Python Programming\n')
    wf.write('Web Design\n')

	

# Example

import math
print(math.pi)

print("Hello World")





