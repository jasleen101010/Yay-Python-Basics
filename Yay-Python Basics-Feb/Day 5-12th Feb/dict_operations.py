# declaring and printing a dictionary
dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(dictionary)
# finding all the keys of the dictionary
x = dictionary.keys()
print(x)

# updating and adding
dictionary["year"] = 2021
dictionary["color"] = "Red"
print(dictionary)

# copying a dictionary
mynewdict = dictionary.copy()
print(mynewdict)
