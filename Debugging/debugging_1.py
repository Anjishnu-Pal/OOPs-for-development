def calculate_average(marks):
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)
    return average


def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"


students = {
    "Ravi": [80, 90, 85],
    "Priya": [70, 75, 72],
    "Amit": [95, 92, 98]
}

for name, marks in students.items():
    avg = calculate_average(marks)
    grade = assign_grade(avg)
    print(name, avg, grade)