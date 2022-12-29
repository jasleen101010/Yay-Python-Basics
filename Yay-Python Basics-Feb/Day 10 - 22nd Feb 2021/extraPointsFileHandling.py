# Reading up `file.txt`
with open("file.txt") as file:
    with open("50Chars.txt", "w") as writeFile:
        fileContent = file.read()
        print(f"Length of File Content: {len(fileContent)}")
        # print(f"Data: {fileContent}")
        print(f"1st 50 Characters: {fileContent[:50]}")
        writeFile.write(fileContent[:50])

