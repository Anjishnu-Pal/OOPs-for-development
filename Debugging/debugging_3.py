"""
School Result Processing System

Task:
1. Calculate each student's total.
2. Calculate average.
3. Assign grade.
4. Find topper.

The program runs successfully,
but the average and grades are wrong.

Find the bug using the Python Debugger.
"""

students = [
    {"name": "Ravi", "marks": [85, 90, 80]},
    {"name": "Priya", "marks": [70, 75, 72]},
    {"name": "Amit", "marks": [95, 92, 98]},
    {"name": "Neha", "marks": [60, 65, 70]},
    {"name": "John", "marks": [88, 84, 86]}
]


def calculate_total(marks):

    total = 0

    for mark in marks:
        total += mark

    return total


def calculate_average(total, marks):

    # ----------------------------
    # BUG IS HERE
    # ----------------------------
    average = total / 100 #len(marks)  # This line is incorrect. It should be total / len(marks)

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


topper = ""
highest_total = 0

print("-" * 50)

for student in students:

    name = student["name"]

    marks = student["marks"]

    total = calculate_total(marks)

    average = calculate_average(total, marks)

    grade = assign_grade(average)

    print(f"Name     : {name}")
    print(f"Marks    : {marks}")
    print(f"Total    : {total}")
    print(f"Average  : {average:.2f}")
    print(f"Grade    : {grade}")
    print("-" * 50)

    if total > highest_total:
        highest_total = total
        topper = name

print("\nTopper :", topper)
print("Highest Total :", highest_total)