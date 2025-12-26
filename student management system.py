students = {}

def add_student():
    name = input("Student name: ")
    marks = input("Marks: ")
    students[name] = marks
    print("Student added!")

def view_students():
    for name, marks in students.items():
        print(name, ":", marks)

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
