# Student Record Management System

# Global list to store all students
students = []

# ---------------------- Function 1 ----------------------
def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'


# ---------------------- Function 2 ----------------------
def add_student():
    roll = input("Enter Roll Number: ")

    # Prevent duplicate roll numbers
    for student in students:
        if student["roll"] == roll:
            print("Student with this Roll Number already exists!")
            return

    name = input("Enter Student Name: ")

    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for Subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")


# ---------------------- Function 3 ----------------------
def view_all_students():
    if len(students) == 0:
        print("No students available.\n")
        return

    for student in students:
        print("----------------------------------")
        print(f"Name     : {student['name']}")
        print(f"Roll No  : {student['roll']}")
        print(f"Marks    : {student['marks']}")
        print(f"Total    : {student['total']}")
        print(f"Average  : {student['average']:.2f}")
        print(f"Grade    : {student['grade']}")
    print("----------------------------------\n")


# ---------------------- Function 4 ----------------------
def search_student():
    roll = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("Student Found:")
            print(f"Name     : {student['name']}")
            print(f"Marks    : {student['marks']}")
            print(f"Total    : {student['total']}")
            print(f"Average  : {student['average']:.2f}")
            print(f"Grade    : {student['grade']}\n")
            return

    print("Student not found.\n")


# ---------------------- Function 5 ----------------------
def class_statistics():
    if len(students) == 0:
        print("No students available.\n")
        return

    total_students = len(students)
    total_class_marks = 0

    highest = students[0]
    lowest = students[0]

    for student in students:
        total_class_marks += student["average"]

        if student["total"] > highest["total"]:
            highest = student

        if student["total"] < lowest["total"]:
            lowest = student

    class_average = total_class_marks / total_students

    print("\nClass Statistics")
    print("----------------------")
    print(f"Total Students : {total_students}")
    print(f"Class Average  : {class_average:.2f}")
    print(f"Highest Scorer : {highest['name']} ({highest['total']})")
    print(f"Lowest Scorer  : {lowest['name']} ({lowest['total']})\n")


# ---------------------- Main Menu ----------------------
def main():
    while True:
        print("===== Student Record Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Class Statistics")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            class_statistics()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the program
main()