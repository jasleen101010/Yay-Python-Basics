file = open('yay.txt', 'a')
file.write("This will add this line")
file.close()
for each in file:
    print(each)
