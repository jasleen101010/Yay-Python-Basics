# # Declaring a Class
# class Library:
#     librarian_name = "Rahul"                 # library_name => Class Variable
#
#     def __init__(self, age):
#         self.book_age = age                # bppk_age => Instance Variable
#
#
# # Main Method
# if __name__ == '__main__':
#     libInfo = Library(17)
#     bibInfo_2 = Library(20)
#     print(libInfo.book_age)
#     print(bibInfo_2.librarian_name)
#     print(bibInfo_2.book_age)
#     print(libInfo.librarian_name)

# Student Class
class Student:

    # Class Variable
    name_of_school = "Yay - Education"

    # Instance Variables
    def __init__(self, name, age, roll_no, division):
        self.age = age
        self.name = name
        self.roll_no = roll_no
        self.division = division


# Instantiating an Class [Object Creation]
obj1 = Student("Rahul", 21, 1705328, "4th Year")
# print(obj1.name)
obj2 = Student("Hello", 22, 1705329, "3rd Year")
# obj1.name = "Rony"
# print(obj1.name)
# print(obj2.name)
print(obj1.name_of_school)
print(obj2.name_of_school)
Student.name_of_school = "GS - Education"
print(obj1.name_of_school)
print(obj2.name_of_school)
print(f"Printing Students: {Student}")



