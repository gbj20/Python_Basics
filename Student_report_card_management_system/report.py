
students = {}
unique_subjects = set()

# calculate grade


def calculate_grade(percentage):
    if percentage >= 95:
        return 'O'
    elif percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    else:
        return 'D'

# 1. Add a student


def add_student():
    name = input("Enter Your Full Name: ")
    roll_no = input("Enter roll no: ")

    subjects = input("Enter subjects (comma separated): ").split(",")
    subjects = [sub.strip() for sub in subjects]

    marks = []
    for sub in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {sub}: "))
                marks.append(mark)
                break
            except ValueError:
                print("Invalid input! Enter a numeric value.")

    #  unique subjects set
    unique_subjects.update(subjects)

    # Store student info
    students[roll_no] = {
        "name": name,
        "subjects": subjects,
        "marks": marks
    }
    print("\n Student added successfully!\n")

# 2. view all students


def view_students():
    if not students:
        print("\nNo student records found.\n")
        return
    print("\nView All Students-----------------")
    for roll, info in students.items():
        total = sum(info['marks'])
        percentage = total / len(info['marks'])
        grade = calculate_grade(percentage)
        print(
            f"Roll No: {roll} | Name: {info['name']} | Percentage: {percentage:.2f}% | Grade: {grade}")
    print()

# 3. search a student by roll no


def search_student():
    roll_no = input("Enter Roll No to search: ")
    if roll_no in students:
        info = students[roll_no]
        print(f"\nStudent Found: {info['name']}")
        for sub, mark in zip(info['subjects'], info['marks']):
            print(f"{sub}: {mark}")
        total = sum(info['marks'])
        percentage = total / len(info['marks'])
        print(
            f"Percentage: {percentage:.2f}% | Grade: {calculate_grade(percentage)}\n")
    else:
        print("Student not found!\n")

# 4. display class topper


def display_topper():
    if not students:
        print("\nNo student records found.\n")
        return
    topper = None
    max_percentage = -1
    for info in students.values():
        percentage = sum(info['marks']) / len(info['marks'])
        if percentage > max_percentage:
            max_percentage = percentage
            topper = info['name']
    print(f"\nClass Topper: {topper} with {max_percentage:.2f}%\n")

# 5.show all unique subjects


def show_unique_subjects():
    if unique_subjects:
        print(f"\nUnique Subjects : {unique_subjects}\n")
    else:
        print("\nNo subjects found!\n")


# Main menu
while True:
    print("========= Student Report Card System =========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by Roll No")
    print("4. Display Class Topper")
    print("5. Show All Unique Subjects")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        display_topper()
    elif choice == '5':
        show_unique_subjects()
    elif choice == '6':
        print("Exiting program!")
        break
    else:
        print("Invalid choice! Please try again.\n")
