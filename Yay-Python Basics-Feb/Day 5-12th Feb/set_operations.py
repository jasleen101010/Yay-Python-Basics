fruits = {"apple","banana","cherry"}
print(fruits)

#get the length of the set
print(len(fruits))

#looping a set
for i in fruits:
    print(i)
    
#adding to a set
fruits.add("grapes")
print(fruits)

# adding from another set
numbers={15,23,54,66}
fruits.update(numbers)
print(fruits)

#union and intersection
setA={"apple",25,"grapes",11}
setB={25,11,"banana","cherry",189}
set_union=setA.union(setB)
print(set_union)
set_intersection=setA.intersection(setB)
print(set_intersection)