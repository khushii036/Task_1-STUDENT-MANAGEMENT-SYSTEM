from models import Student

students = []


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    student = Student(student_id, name, age, course)
    students.append(student)

    print("\nStudent Added Successfully!\n")


def view_students():
    if not students:
        print("\nNo student records found.\n")
        return

    print("\n----- Student Records -----")
    for student in students:
        print(student)
    print()


def search_student():
    sid = input("Enter Student ID to Search: ")

    for student in students:
        if student.student_id == sid:
            print("\nStudent Found:")
            print(student)
            return

    print("\nStudent Not Found.\n")


def update_student():
    sid = input("Enter Student ID to Update: ")

    for student in students:
        if student.student_id == sid:
            print("\nEnter New Details")

            student.name = input("New Name: ")
            student.age = input("New Age: ")
            student.course = input("New Course: ")

            print("\nStudent Updated Successfully!\n")
            return

    print("\nStudent Not Found.\n")


def delete_student():
    sid = input("Enter Student ID to Delete: ")

    for student in students:
        if student.student_id == sid:
            students.remove(student)

            print("\nStudent Deleted Successfully!\n")
            return

    print("\nStudent Not Found.\n")