class Employees:
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary}. Role is {self.role}."


jasleen = Employees()
jasleen.name = "Jasleen Sondhi"
jasleen.salary = 15000
jasleen.role = "Mentor"
print(jasleen.printdetails())
