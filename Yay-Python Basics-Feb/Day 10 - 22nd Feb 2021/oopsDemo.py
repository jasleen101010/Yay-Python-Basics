# OOPs Demo for the Previous Problem
# Class `Employees`
class Employees:

    def __init__(self, name, age, designation, another_field = None):
        self.name = name
        self.age = age
        self.designation = designation
        self.another_field = another_field

    def showEmployee(self):
        print(f'Employee Name : {self.name} is {self.age} of age and is at the position of {self.designation}')
        print(f"Value of Another Field: {self.another_field}")


# Main Function
if __name__ == '__main__':
    emp1 = Employees('James', 24, 'Product Manager')
    emp2 = Employees('Rock', 52, 'SDE-1', 7)
    emp3 = Employees('John', 32, 'CEO')
    emp1.showEmployee()
    emp2.showEmployee()
    emp3.showEmployee()
    print(f"Type of Variable for `emp1` : {type(emp1)}")
