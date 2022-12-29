# Object Oriented Programming in Python


# `Student` Class
class Student:

    """
    Contains the Information of a Student
    """

    # Class Variables [Attributes]
    count = 0
    course_provider = 'YAY-Education'

    # Constructor
    def __init__(self, name, age, grade):

        # Instance Variables [Attributes]
        self.name = name
        self.age = age
        self.grade = grade  # 0 = 100

        # Updating Class Variable
        Student.count += 1

    # Class Instance Method
    def get_grade(self):
        return self.grade

    # Another Special Instance Method [DUNDER method]
    def __str__(self):
        return f'My Name is {self.name} & I am {self.age} years old.'


# `Course` Class
class Course:

    """
    Contains the Information of a Course
    """

    # Constructor
    def __init__(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students
        self.students = []

    # Class Instance Method
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    # Class Instance Method
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


# Main Method
if __name__ == '__main__':

    s1 = Student("Rahul", 21, 95)
    s2 = Student("Rony", 22, 75)
    s3 = Student("Krish", 25, 90)
    print(s3)
    print(s1)
    pythonCourse = Course("Python", 2)
    pythonCourse.add_student(s1)
    pythonCourse.add_student(s2)
    pythonCourse.add_student(s3)
    print(pythonCourse.get_average_grade())
    print(Student.count)
    print(Student.course_provider)
    print(Student.__doc__)                  # Printing the Doc - String
    print(Course.__doc__)


