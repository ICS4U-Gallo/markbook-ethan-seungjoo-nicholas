"""
Markbook Application
Group members: Ethan, Seung Joo, Nicholas
"""
from typing import Dict


def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    assignment_dict = {
        "name": name, 
        "due": due, 
        "points": points
    }
    
    return assignment_dict


def create_classroom(course_code: str, course_name: str, period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    classroom = {
        'course_code': course_code,
        'course_name': course_name,
        'period': period,
        'teacher': teacher,
        'student_list': [],
        'assignment_list': []
    }
    return classroom

classroom = create_classroom('ics4u', 'computer science', 2, 'Mr. Gallo')
print(classroom)

def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    student['marks'].sort()
    
    total = 0
    for mark in student['marks']:
        total += mark
    average = total / len(student['marks'])
    return average
# answer = calculate_average_mark()

print(calculate_average_mark(student = {"marks": [50, 100]}))


def add_student_to_classroom(student: Dict, classroom: Dict):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    classroom['student_list'].append(student.items())
    #classroom['student_list'].update(student)

    return classroom



def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    classroom['student_list'].remove(student.items())
    return classroom


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    student["first_name"] = kwargs["first_name"]
    student["last_name"] = kwargs["last_name"]
    return student["first_name"]
