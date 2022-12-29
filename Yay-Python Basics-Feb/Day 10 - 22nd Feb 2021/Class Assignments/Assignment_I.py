""" Assignment - I
    Write a Text File using Python. Copy the contents of that file to another file.
    And also to inculcate the use of try..except..raise..finally and also to close the file at the end [Text File]
"""

# Program [Answer]

## Writing Content into File 1 using Python
try:
    with open("Assignment_File1.txt", "w") as file_1:
        stringInput = """This is a File I created using Python.
        I'm a Genius Now!!!!
        """
        file_1.write(stringInput)
except IOError:
    print("Error Handling the File!!")
else:
    print("File 1 Created Successfully!")

## Reading from File 1 and Copying into File 2 using Python
try:
    with open("Assignment_File1.txt", "r") as file_1:
        with open("Assignment_File2.txt", "w") as file_2:
            fileContents =  file_1.read()
            file_2.write(fileContents)

    print("File Operation Successful!!!")
    raise IOError("File DNE!")

except IOError as error:
    pass

finally:
    if ('file_1' in locals()) & ('file_2' in locals()):
        file_1.close()
        file_2.close()
    print('Files Closed Successfully!')
