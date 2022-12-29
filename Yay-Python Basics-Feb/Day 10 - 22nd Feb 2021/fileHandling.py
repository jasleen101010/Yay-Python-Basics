# File Handling

"""
“ r “, for reading.
“ w “, for writing.
“ a “, for appending.
“ r+ “, for both reading and writing
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""

## Opening a File and Reading it's Contents
# file = open("file.txt")
# print(file.read())
# print(open("file.txt").read())             # Doing the Same Task using a Single LOC (Line of Code)

## Using Exception Handling Practices to Work with Files
# try:
#     file = open("file.txt")
#     for i in file:
#         print(i)
#     raise IOError("File Doesn't Exit")
# except IOError as ioe:
#     pass
# finally:
#     if 'file' in locals():
#         file.close()
#         print('File Closed')

## Another Technique to Read in a File [Using Read Lines Function]
# file = open('file.txt')
# for i in file.readlines():
#     print(i)
# file.close()

## Splitting the Words Separately from the Sentences while forming a List
# file = open("file.txt")
# data = file.readlines()
# for line in data:
#     word = line.split()
#     print(word)
# file.close()

## Writing Contents into a New File
# file = open("writeFile.txt", "w")
# stringForFile = """This a File I created using Python.
# I'm using Multi-Line String.
# Have a Nice Day Ahead"""
# file.write(stringForFile)
# file.write("\nFile End")
# file.close()

## Appending Example
# file = open("writeFile.txt", "a")
# stringForFile = "\n\nAppending New Information to Existing File"
# file.write(stringForFile)
# file.close()

## Different Ways of Reading a File [Using Normal Approach and Constructors]
# try:
#     with open("file.txt") as file:             # In this Case, you don't need to Close the file Manually.
#         data = file.read()
#         print(data)
# except Exception as e:
#     print(e)

## Reading up Binary Files
# try:
#     with open('ronaldo.jpg', 'rb') as readFile:
#         print(file.read())
# except Exception as e:
#     print("An Exception has Occurred!")


## Copying Image Files into Another Newly Created Image File
# try:
#     with open('ronaldo.jpg', 'rb') as readFile:
#         with open("ronaldoCopy.jpg", "wb") as writeFile:
#             # print(file.read())
#             fileContent = readFile.read()
#             writeFile.write(fileContent)
#
# except Exception as e:
#     print("An Exception has Occurred!")

## Copying Text Files
try:
    with open('writeFile.txt', 'r') as readFile:
        with open("fileCopy.txt", "w") as writeFile:
            fileContent = readFile.read()
            writeFile.write(fileContent)

except IOError as e:
    print("An Exception has Occurred!")


