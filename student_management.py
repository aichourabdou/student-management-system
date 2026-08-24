import json
print("="*60)
print("               Student Management System")
print("="*60)
students = []
def Add_student():
    print("\n--- Add Student ---")

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    grades = []

    for number in range(3):
        grade = float(input(f"Enter grade {number + 1}: "))
        grades.append(grade)

    student = {
        "name": name,
        "age": age,
        "grades": grades
    }

    students.append(student)

    save_students()
    print("Student added successfully!")
def Delete_student():
    print("\n--- Delete Student ---")
    name = input("Enter student name to delete: ")
    for student in students:
        if student["name"] == name:
            students.remove(student)
            save_students()
            print("Student deleted successfully!")
            return
    print("Student not found!")
def Search_student():
    print("\n--- Search Student ---")

    name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Grades:", student["grades"])
            return

    print("Student not found.")
def All_students():
     print("\n---All students--- ")
     if not students:
          print("No students found.")
     else:
          for student in students:
               print("Name:", student["name"])
               print("Age:", student["age"])
               print("Grades:", student["grades"])
               print()
def Update_students():
     print("\n---Update student---")
     name = input("Enter student name to update:")
     for student in students:
          if student["name"] == name:
               new_name =input("Enter new name :")
               new_age = int(input("Enter new age:"))
               new_grades=[]
               for number in range(3):
                    grade= float(input(f"Enter new grade {number + 1}:"))
                    new_grades.append(grade)
               student["name"]= new_name
               student["age"]=new_age
               student["grades"]=new_grades
               save_students()
               print("Student updated successfully!")
               return

     print("Student not found.")               
def Individual_average():
     print("\n ---individual average---")
     name = input("Enter student name to calculate average:")
     for student in students:
          if student["name"]==name:
               total = sum(student["grades"])
               average = total / len(student["grades"])

               print(f"Average grade for {student['name']}: {average}")
               return

     print("Student not found.")
def Find_top_student():
     print("\n ---top_student---")
     if not students :
          print("No students found.")
          return
     top_student = students[0]
     for student in students:
          current_average = sum(student["grades"]) / len(student["grades"])
          top_average = sum (top_student["grades"]) / len (top_student["grades"])
          if current_average > top_average:
               top_student = student
     average = sum(top_student["grades"]) / len(top_student["grades"])

     print("Top student:", top_student["name"])
     print("Average:", average)  
def Calculate_class_average():
     print("\n ---Class average---")
     if not students:
          print("No students found.")
          return
     total = sum(sum(student["grades"]) for student in students)
     count = sum(len(student["grades"]) for student in students)
     average = total / count if count > 0 else 0
     print("Class average:", average)
def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []
def save_students():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

students = load_students()

while True :
     print("1. Add student")
     print("2. Delete student")
     print("3. Search student")
     print("4. All students")
     print("5. update student")
     print("6. individual average-")
     print("7. top student")
     print("8. class average")
     print("9. Exit")
     choice=int(input("Enter your choice :")) 
     if choice == 1:
          Add_student()
     elif choice ==2:
          Delete_student()

     elif choice ==3:
          Search_student()
     elif choice ==4:
          All_students()
     elif choice ==5:
          Update_students()
     elif choice ==6:
          Individual_average()
     elif choice ==7:
          Find_top_student()
     elif choice ==8:
          Calculate_class_average()
     elif choice ==9:
          print("goodbye")
          break
     else :
          print("Invalid choice")
 