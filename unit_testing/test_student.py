import pytest
from student_service import StudentService


def test_add_student_success():
    service = StudentService()

    service.add_student(1, "Ravi", 85)

    student = service.get_student(1)

    assert student["name"] == "Ravi"
    assert student["marks"] == 85


def test_duplicate_student_error():
    service = StudentService()

    service.add_student(1, "Ravi", 85)

    with pytest.raises(ValueError):
        service.add_student(1, "Ravi", 90)


def test_invalid_marks_less_than_zero():
    service = StudentService()

    with pytest.raises(ValueError):
        service.add_student(1, "Ravi", -10)


def test_invalid_marks_greater_than_100():
    service = StudentService()

    with pytest.raises(ValueError):
        service.add_student(1, "Ravi", 120)


def test_get_unknown_student_error():
    service = StudentService()

    with pytest.raises(KeyError):
        service.get_student(99)


@pytest.mark.parametrize(
    "marks, expected_grade",
    [
        (95, "A"),
        (80, "B"),
        (65, "C"),
        (45, "D"),
        (30, "F"),
    ]
)
def test_calculate_grade(marks, expected_grade):
    service = StudentService()

    grade = service.calculate_grade(marks)

    assert grade == expected_grade


def test_get_result():
    service = StudentService()

    service.add_student(1, "Priya", 92)

    result = service.get_result(1)

    assert result["name"] == "Priya"
    assert result["marks"] == 92
    assert result["grade"] == "A"


def test_class_average():
    service = StudentService()

    service.add_student(1, "Ravi", 80)
    service.add_student(2, "Priya", 90)
    service.add_student(3, "Arjun", 70)

    average = service.class_average()

    assert average == 80


def test_class_average_no_students():
    service = StudentService()

    assert service.class_average() == 0