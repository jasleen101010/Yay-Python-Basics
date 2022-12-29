# Class Employee
class Employee:
    companyName = "High Radius"
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last
    # Using the Method as an Attribute
    @property
    def email(self):
        return f"{self.firstName.lower()}.{self.lastName.lower()}@{''.join(''.join(Employee.companyName.lower().split()))}.com"
    # String Method
    def __str__(self):
        return f"Employee Name : {self.firstName} {self.lastName}"
    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"
    # Full-Name Setter Method
    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.firstName = first
        self.lastName = last
    # Delete Method
    @fullName.deleter
    def fullName(self):
        print('Name Deleted!')
        self.firstName = None
        self.lastName = None
# Main Method
if __name__ == '__main__':
    emp1 = Employee("Rahul", "Bordoloi")
    print(emp1)
    print(emp1.email)
    print(emp1.fullName)
    emp1.fullName = "Rony Bordoloi"
    print(emp1.fullName)
    del emp1.fullName
    print(emp1.fullName)