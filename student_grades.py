students = {
    "Tarun": "A",
    "Rahul": "B",
    "Aman": "C"
}

print("Current Student Grades:")
for name, grade in students.items():
    print(name, ":", grade)

name = input("\nEnter student name: ")
grade = input("Enter grade: ")

if name in students:
    students[name] = grade
    print("Student grade updated.")
else:
    students[name] = grade
    print("New student added.")

print("\nUpdated Student Grades:")
for name, grade in students.items():
    print(name, ":", grade)