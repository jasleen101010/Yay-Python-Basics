thisList=["orange","apple","banana"]
#printing a list
print(thisList)
#indexing a list
print(thisList[1])
#appending an element to the list
thisList.append("grapes")
print(thisList)
#insert an element to the list
thisList.insert(2,"mango")
print(thisList)
#replacing/changing an element in the list
thisList[1:2]=["cherry","kiwi"]
print(thisList)
#remove an element from the list
thisList.remove("mango")
print(thisList)
#pop an element from the list
thisList.pop(0)
print(thisList)
#sort the list
thisList.sort()
print(thisList)
#looping a list
for i in thisList:
    print(i)