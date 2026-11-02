def calculate_grade(mark):
    if mark >= 70:
        return "A"
    elif mark >= 60:
        return "B"
    elif mark >= 50:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"


students = []

for i in range(3):
    name = input("Enter student name: ")
    mark = int(input("Enter student mark: "))

    grade = calculate_grade(mark)

    students.append({
        "name": name,
        "mark": mark,
        "grade": grade
    })

students.sort(
    key=lambda student: student["mark"],
    reverse=True
)

print("\nSTUDENT RESULTS")

for student in students:
    print(
        f"{student['name']} - "
        f"{student['mark']} marks - "
        f"Grade {student['grade']}"
    )