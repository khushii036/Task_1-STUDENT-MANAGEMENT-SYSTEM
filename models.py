class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def __str__(self):
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Course: {self.course}"