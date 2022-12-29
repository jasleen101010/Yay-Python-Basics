class Student:
    school_name = "YAY"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def cal_averge(self):
        average = sum(self.marks) / len(self.marks)
        print(self.school_name)
        print(f"Average Marks: {average}")


if __name__ == '__main__':
    obj1 = Student("Rahul", [90, 95, 95])
    obj1.cal_averge()
    obj2 = Student("Rony", [453553543])
    print(Student.school_name)