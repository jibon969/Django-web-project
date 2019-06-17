
# Date: 9:17 AM 6/17/2019

# Python File

"""
What is a file?
How to open a file?
How to close a file Using Python?
How to write to File Using Python?
How to read files in Python?
Python File Methods

"""

# Syntax

# file object = open(file_name [, access_mode][, buffering])


# Python file operation are

"""
Open a file
Read or write
Close the file
"""

# How to open a file?

print("How to open a file : \n")


""" 
>>> f = open("test.txt")    # open file in current directory
>>> print(f)
"""


# How to file open and read in python

file = open('C:\\Users\\Jibon\Desktop\\new.txt', 'r')  # specifying full path
readFile = file.read()
print(readFile)
file.close()


# Another way to open file read... ( এইভাবে ফাইল ওপেন করলে ফাইল close()করতে হবে না । )

with open('C:\\Users\\Jibon\Desktop\\b.py', 'r') as x:
    newFile = x.read()
    print("Read File : ", newFile)
print('\n')


# How to write file in python

print("How to write file : \n")

my_file = open('C:\\Users\\Jibon\Desktop\\jibon.txt', 'w')  # w means write in text mode
x = my_file.write('Hello')
print("Write File : ", x)
my_file.close()


# Another way to file open and write

with open('C:\\Users\\Jibon\Desktop\\jibon.txt', 'w') as fw:
   fw.write('Welcome to file')

print('\n')


with open('C:\\Users\\Jibon\Desktop\\jibon.txt', 'r') as rf:
    a = rf.read()
    print("File : ", a)
    print("file which mode : ", rf.mode)  # Mode works file which mode

print('\n')


# Example of file open and write

print("File open and write : \n")

file = open('C:\\Users\\Jibon\Desktop\\jibon.txt', 'w')
file.write('Jibon\n')
file.write('Ahmed\n')
file.write('Kurigram\n')
file.write('Dhaka\n')
file.write('Bangladesh\n')
print('\n')


# Another way to handle file open and write

with open('C:\\Users\\Jibon\Desktop\\file.txt', 'w') as wf:
    wf.write('I am learning python file \n')
    wf.write('Python Programming \n')
    wf.write('Web Design \n')
print('\n')


# How to open  image open with binary format

print(" How to open  image open with binary format : \n")


f = open('C:\\Users\\Jibon\Desktop\\jibon-69.jpg', 'rb')
imageRead = f.read()
print("ImageRead : ", imageRead)
f.close()
print('\n')


#  Image open with binary format

with open('C:\\Users\\Jibon\Desktop\\jibon-69.jpg', 'rb') as ImageReadBinaryFormat:
    x = ImageReadBinaryFormat.read()
    print("ImageReadBinaryFormat : \n", x)
    print('\n')


# Python File Methods

print("Python File Methods : ")


"""
Method	                    Description
close()	                    Close an open file. It has no effect if the file is already closed.
detach()	                Separate the underlying binary buffer from the TextIOBase and return it.
fileno()	                Return an integer number (file descriptor) of the file.
flush()	                    Flush the write buffer of the file stream.
isatty()	                Return True if the file stream is interactive.
read(n)	                    Read atmost n characters form the file. Reads till end of file if it is negative or None.
readable()	                Returns True if the file stream can be read from.
readline(n=-1)	            Read and return one line from the file. Reads in at most n bytes if specified.
readlines(n=-1)	            Read and return a list of lines from the file. Reads in at most n bytes/characters if specified.
seek(offset,from=SEEK_SET)	Change the file position to offset bytes, in reference to from (start, current, end).
seekable()	                Returns True if the file stream supports random access.
tell()	                    Returns the current file location.
truncate(size=None)	        Resize the file stream to size bytes. If size is not specified, resize to current location.
writable()	                Returns True if the file stream can be written to.
write(s)	                Write string s to the file and return the number of characters written.
writelines(lines)	        Write a list of lines to the file.
"""


# The open Function

"""
r           Opens a file for reading only. The file pointer is placed at the beginning of the file. 
            This is the default mode.
                            
rh          Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file.
            This is the default mode.
                            
                            
r+          Opens a file for both reading and writing. The file pointer placed at the beginning of the file.


rb+         Opens a file for both reading and writing in binary format. 
            The file pointer placed at the beginning of the file.
                            
                            
w           Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist,
            creates a new file for writing. 
                             
                             
wb          Opens a file for writing only in binary format. Overwrites the file if the file exists. 
            If the file does not exist, creates a new file for writing.
                             
                             
w+          Opens a file for both writing and reading. Overwrites the existing file if the file exists.
            If the file does not exist, creates a new file for reading and writing.
                            
                            
wb+         Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists.
            If the file does not exist, creates a new file for reading and writing.  
                            
                             
a           Opens a file for appending. The file pointer is at the end of the file if the file exists. 
            That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
                            
                            
ab          Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. 
            That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
               
               
a+          Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. 
            The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
                
                                          
ab+         Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. 
            The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.
"""