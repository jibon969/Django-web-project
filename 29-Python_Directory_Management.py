
# Python Directory and Files Management

# Note : open python shell or cmd help() then os enter দিলে সব গুলো function দেখতে পাবো ।

print("\n")

""" 
Table of Contents :-

    What is Directory in Python?
    Get Current Directory
    Changing Directory
    List Directories and Files
    Making a New Directory
    Renaming a Directory or a File
    Removing Directory or File

"""

# What is Directory in Python?

"""
    A directory or folder is a collection of files and sub directories.
"""


# Example Get Current Directory
import os


print(" Get Current Directory : \n")

x = os.getcwd()     # getcwd() দ্বারা আমারা Current Directory দেখতে পাবো
print("Current Location : ", x)
print('\n')


# Example Changing Directory

print("Changing Directory : \n")

"""
    We can change the current working directory using the chdir() method.
"""


os.chdir('C:\\Users\\Jibon\Desktop')
print("Current Location : ", os.getcwd())
print('\n')


# Example List Directories and Files

print("List Directories and Files : \n")


"""
    All files and sub directories inside a directory can be known using the listdir() method.
"""

import os
os.chdir('C:\\Users\\Jibon\Desktop')
print("Current Location : ", os.getcwd())
print(os.listdir())     # listdir() দ্বারা আমরা current working directory সব কিছু দেখতে পাবো ।
print('\n')


# Making a new directory in python

print("Making a New Directory : \n")

"""
    We can make a new directory using the mkdir() method.
"""

import os
os.chdir('C:\\Users\\Jibon\Desktop')
x = os.mkdir("Folder")
print("Create Folder : ", x)
print(os.listdir())
print("\n")


# Renaming a Directory or a File

print("Renaming a Directory or a File : \n")

"""
    The rename() method can rename a directory or a file.
"""

import os
os.chdir("C:\\Users\\Jibon\Desktop")
os.mkdir("Old_Folder")
os.rename("Old_Folder", "New_Folder")
print(os.listdir())
print("\n")


# Removing Directory or File

"""
A file can be removed (deleted) using the remove() method.
Similarly, the rmdir() method removes an empty directory.
"""

# How to Remove Python Directory/File?

"""
import os
os.chdir('C:\\Users\\Jibon\Desktop\\Python 2019')
os.listdir()
os.rmdir("Python 2019")
print("listdir : ", os.listdir())
print("\n")

"""


# Joining and Splitting Path

print("Joining and Splitting Path :\n")

"""
join() in python joins path components and returns a path as a string.
"""

import os
x = os.path.join('C:', 'Users', 'Jibon', 'Desktop')
print("Joins Path : ", x)
print("\n")


# Example

"""
split() splits the path into components, removing the separator.
"""
import os
y = os.path.split("C:\\Users\\Jibon\Desktop")
print("Split Path : ", y)
print("\n")


# Checking if Python Directory Exists
print("Checking if Python Directory Exists : \n")

import os

a = os.path.exists("C:\\Users\\Jibon\Desktop")
print("Exists Path : ", a)
print("\n")


# Example Recursively Traversing a Directory in Python

print("Recursively Traversing a Directory in Python : \n")

"""
    The walk() function lets us recursively traverse a directory.
"""


for roots, dirs, files in os.walk('C:\\Users\\Jibon\Desktop\Gulp_Doc'):
    print("roots : ", roots)
    print("dirs  : ", len(dirs))
    print("files : ", len(files))

print("Stop Program !")
print("\n")



"""
help> os
Help on module os:

NAME
    os - OS routines for NT or Posix depending on what system we're on.

DESCRIPTION
    This exports:
      - all functions from posix or nt, e.g. unlink, stat, etc.
      - os.path is either posixpath or ntpath
      - os.name is either 'posix' or 'nt'
      - os.curdir is a string representing the current directory (always '.')
      - os.pardir is a string representing the parent directory (always '..')
      - os.sep is the (or a most common) pathname separator ('/' or '\\')
      - os.extsep is the extension separator (always '.')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)
      
      ... Continue ...
"""


print("Python Directory methods : \n")

"""
Here is the tabular list of Python directory methods defined in os module for directory management.


Python directory methods        Description

os.access(path, mode)           Use the real uid/gid to test for access to the path.

os.chdir(path)                  Used to change the current working directory to the path specified.

os.chflags(path, flags)         Set the flags of path to the numeric flags.

os.chmod(path, mode)            Change the mode of path to the numeric mode.

os.chown(path, uid, gid)        Change the owner and group id of path to the numeric uid and gid. To leave one of the ids unchanged, set it to -1.

os.chroot(path)                 Changes the root directory of the current process to the specified path.

os.fchdir(fd)                   Changes the current working directory to the directory represented by the file descriptor fd. The descriptor must refer to an opened directory.

os.getcwd()                     It returns a string representing the current working directory.

os.getcwdu()                    It returns a Unicode object representing the current working directory.

os.lchflags(path, flags)        Set the flags of path to the numeric flags, like chflags( ), but do not follow symbolic links.

os.lchmod(path, mode)           It changes the mode of path to the numeric mode.

os.lchown(path, uid, gid)       It changes the owner and group id of path to the numeric uid and gid. 
                                This function will not follow symbolic links.

os.listdir(path)                Returns a list containing the names of the entries in the directory given by path.

os.lstat(path)                  It works like stat( ), but do not follow symbolic links.

os.makedirs(path[, mode])       It creates directories recursively.

os.mkdir( )                     Creates a new directory named path.

os.mkfifo(path[, mode])         Create a FIFO (a named pipe) named path with numeric mode. The default mode is 0666 (octal).

os.readlink(path)               Returns a string representing the path to which the symbolic link points.

os.removedirs(path)             Remove directories recursively starting from child to parent.

os.rename(src, dst)             Rename the directory src to dst.

os.renames(old, new)            It renames the old directories with a new name recursively.

os.rmdir(path)                  Removes the directory path specified.

os.stat(path)                   Perform a stat system call on the given path.
"""





