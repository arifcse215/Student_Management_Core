def add_student(students):
    s_id = int(input("ID: "))
    if s_id < 1:
        print("Invalid ID\n")
        return
    
    for student in students:
        if student['id'] == s_id:
            print("ID already exists\n")
            return

    s_name = " ".join(input("Name: ").split())
    if not s_name:
        print("Name is empty.\n")
        return

    s_age = int(input("Age: "))
    if s_age < 10 or s_age > 100:
        print("Invalid age\n")
        return

    s_marks = int(input("Marks: "))
    if s_marks < 0 or s_marks > 100:
        print("Invalid marks\n")
        return

    student = dict()
    student['id'] = s_id
    student['name'] = s_name
    student['age'] = s_age
    student['marks'] = s_marks
    students.append(student)
    print("Student Added Successfully\n")

def show_students(students):
    if not students:
        print("No students found\n")
        return
    
    for student in students:
        print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Marks: {student['marks']}")

def search_student(students):
    s_id = int(input("Enter Student ID: "))
    if s_id < 1:
        print("Invalid ID! ID must be a positive number.\n")
        return

    for student in students:
        if student['id'] == s_id:
            print("Student Found")
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Marks: {student['marks']}\n")
            return
    print("Student Not Found\n")

def update_student(students):
    s_id = int(input("Enter Student ID: "))
    if s_id < 1:
        print("Invalid ID\n")
        return
    for student in students:
        if student['id'] == s_id:
            s_name = " ".join(input("Enter New Name: ").split())
            if not s_name:
                print("Name is empty.\n")
                return

            s_age = int(input("Enter New Age: "))
            if s_age < 10 or s_age > 100:
                print("Invalid age\n")
                return

            s_marks = int(input("Enter New Marks: "))
            if s_marks < 0 or s_marks > 100:
                print("Invalid marks\n")
                return

            student['name'] = s_name
            student['age'] = s_age
            student['marks'] = s_marks

            print("Student Updated Successfully\n")
            return

    print("Student Not Found!\n")

def delete_student(students):
    s_id = int(input("Enter Student ID: "))
    if s_id < 1:
        print("Invalid ID\n")
        return
    for student in students:
        if student['id'] == s_id:
            students.remove(student)
            print("Student Deleted Successfully\n")
            return

    print("Student Not Found\n")

def show_students_by_grade(students):
    s_grade = input("Enter Grade: ").upper()
    if not ("A" <= s_grade <= "D" or s_grade == "F"):
        print("Invalid Grade\n")
        return

    if s_grade == "A":
        c = 0
        for student in students:
            if student['marks'] >= 80:
                print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Marks: {student['marks']}")
                c += 1
        if not c:
            print("No Student Found\n")

    elif s_grade == "B":
        c = 0
        for student in students:
            if 70 <= student['marks'] <= 79:
                c += 1
                print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Marks: {student['marks']}")
        if not c:
            print("No Student Found\n")

    elif s_grade == "C":
        c = 0
        for student in students:
            if 60 <= student['marks'] <= 69:
                c += 1
                print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Marks: {student['marks']}")
        if not c:
            print("No Student Found\n")

    elif s_grade == "D":
        c = 0
        for student in students:
            if 50 <= student['marks'] <= 59:
                print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Marks: {student['marks']}")
                c += 1
        if not c:
            print("No Student Found\n")

    elif s_grade == "F":
        c = 0
        for student in students:
            if 0 <= student['marks'] <= 49:
                print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Marks: {student['marks']}")
                c += 1
        if not c:
            print("No Student Found\n")

def show_statistics(students):
    s_total = len(students)
    if not s_total:
        print("No Student Found")
        return
    
    print(f"Total Students: {s_total}")
    highest = students[0]['marks']
    lowest = students[0]['marks']
    total = 0
    Highest_Scorer = students[0]['name']
    Lowest_Scorer = students[0]['name']

    for student in students:
        total += student['marks']

        if student['marks'] > highest:
            highest = student['marks']
            Highest_Scorer = student['name']
            
        elif student['marks'] < lowest:
            lowest = student['marks']
            Lowest_Scorer = student['name']

    print(f"Average Marks: {total / s_total:.2f}")
    print(f"Highest Marks: {highest}")
    print(f"Highest Scorer: {Highest_Scorer}")
    print(f"Lowest Marks: {lowest}")
    print(f"Lowest Scorer: {Lowest_Scorer}")
        

students = [
    {
        "id": 1,
        "name": "Arif",
        "age": 22,
        "marks": 85
    },
    {
        "id": 2,
        "name": "Sadia",
        "age": 21,
        "marks": 92
    },
    {
        "id": 3,
        "name": "Tanvir",
        "age": 23,
        "marks": 78
    },
    {
        "id": 4,
        "name": "Nabila",
        "age": 20,
        "marks": 88
    },
    {
        "id": 5,
        "name": "Fahim",
        "age": 22,
        "marks": 65
    }
]

while True:
    print(
        """
================================
       STUDENT MANAGEMENT
================================

1. Add Student
2. Show All Students
3. Search Student
4. Update Student
5. Delete Student
6. Show Students by Grade
7. Show Statistics
8. Exit

        """
    )

    choice = input("Enter choice: ")
    if choice == '1':
        add_student(students)

    elif choice == '2':
        show_students(students)
        

    elif choice == '3':
        search_student(students)

    elif choice == '4':
        update_student(students)
        
    elif choice == '5':
        delete_student(students)

    elif choice == '6':
        show_students_by_grade(students)

    elif choice == '7':
        show_statistics(students)

    elif choice == '8':
        break