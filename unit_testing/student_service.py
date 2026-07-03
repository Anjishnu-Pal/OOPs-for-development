class StudentService:

    def __init__(self):
        self.students = {}

    def add_student(self, roll_no, name, marks):
        if roll_no in self.students:
            raise ValueError("Student already exists")

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        self.students[roll_no] = {
            "name": name,
            "marks": marks
        }

    def get_student(self, roll_no):
        if roll_no not in self.students:
            raise KeyError("Student not found")

        return self.students[roll_no]

    def calculate_grade(self, marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 40:
            return "D"
        else:
            return "F"

    def get_result(self, roll_no):
        student = self.get_student(roll_no)
        marks = student["marks"]
        grade = self.calculate_grade(marks)

        return {
            "name": student["name"],
            "marks": marks,
            "grade": grade
        }

    def class_average(self):
        if len(self.students) == 0:
            return 0

        total = 0

        for student in self.students.values():
            total += student["marks"]

        return total / len(self.students)