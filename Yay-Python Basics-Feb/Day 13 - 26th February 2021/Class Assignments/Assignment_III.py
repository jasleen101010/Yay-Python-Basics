""" Assignment - III
    WAP a to implement Hierarchical Inheritance taking in example of Boss and Employees of a Company.
"""

# Assignment Answer


# `Employee` Class
class Employees:
    name_of_company = 'YAY - Associates'  # Class Variable

    # Constructor
    def __init__(self, emp_id, name):
        self.id = emp_id
        self.name = name

    # `__str__` Magic Method to display out information
    def __str__(self):
        return f"I'm {self.name} and my ID is {self.id}."


# `HOD` Class -> Boss
class HOD(Employees):

    # Constructor
    def __init__(self, emp_id, name, department, salary):
        super().__init__(emp_id, name)  # Calling in the Constructor of Parent Method
        self.department = department
        self.salary = salary

    # `__str__` Magic Method to display out information
    def __str__(self):
        return f'ID : {self.id}, Boss Name : {self.name}, Department : {self.department}, Salary : ${self.salary}'

    # Static Method to Give out Department
    @staticmethod
    def about():
        print("I'm the Boss!")


# `Manager` Class
class Managers(Employees):
    no_of_managers = 0  # Class Variable

    def __init__(self, emp_id, name, department):
        super().__init__(emp_id, name)  # Calling in the Constructor of Parent Method
        self.department = department
        Managers.count_managers()

    # Class Method to Count Number of Managers
    @classmethod
    def count_managers(cls):
        cls.no_of_managers += 1

    # `__str__` Magic Method to display out information
    def __str__(self):
        return f'ID : {self.id}, Manager Name : {self.name}, Department : {self.department}'


#  Main Method
def main():
    # Defining the Classes and it's associated instances/variables
    emp = Employees(7, 'Rahul')
    hod_1 = HOD(1, 'Elon Musk', 'Space R&D', 7500000)
    hod_2 = HOD(3, 'Jeff Bezos', 'Sales & Marketing', 12000000)
    manager1 = Managers(56, 'Pablo', 'Space R&D')
    manager2 = Managers(97, 'Diablo', 'Space R&D')
    manager3 = Managers(24, 'Pacheo', 'Consultancy')

    # Displaying out Information
    print(f'Company Name : {Employees.name_of_company}')
    print(emp)
    print(hod_1)
    hod_2.about()
    print(manager1)
    print(f'No. of Managers : {Managers.no_of_managers}')


#  Driver Method
if __name__ == '__main__':
    main()

