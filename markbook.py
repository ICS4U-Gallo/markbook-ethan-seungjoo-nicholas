"""
Markbook Application
Group members: Ethan, Seung Joo, Nicholas
"""
import json
import os
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

def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    student['marks'].sort()
    
    total = 0
    for mark in student['marks']:
        total += mark
    average = total / len(student['marks'])
    return average
# answer = calculate_average_mark()


def add_student_to_classroom(student: Dict, classroom: Dict):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    classroom['student_list'].append(student.items())

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

def create_assignment_interface():
    os.system('clear')
    print('--------------------------------------------------------------- Create Assignment ---------------------------------------------------------------')
    name = input('Enter assignment name: ')
    due_date = input('Enter due date: ')
    marks = int(input('Enter maximum points: '))
    print(create_assignment(name, due_date, marks))

def create_classroom_interface():
    print('--------------------------------------------------------------- Create Classroom ---------------------------------------------------------------')
    code = input('Enter the course code: ')
    course_name = input('Enter the course name: ')
    period = input('Enter the period: ')
    teacher = input('Enter the teacher name: ')
    names = input('Enter the student list: ')
    student_list = names.split()
    assignments = input('Enter the assignment list: ')
    assignment_list = assignments.split()
    
    # args: course_code: str, course_name: str, period: int, teacher: str
    # pass

def average_mark_interface():
    # args: student: Dict -> within dict is ['marks': example marks: 10, 20, 30]
    pass

def add_student_interface():
    #args: student: Dict, classroom: Dict
    pass

def remove_student_interface():
    #args: student: Dict, classroom: Dict
    pass

def edit_student_interface():
    #args: student: Dict, **kwargs: Dict
    pass


def main():
    working = True
    print("------------------------------------------------------- Welcome to the Python Teacher Markbook -------------------------------------------------------")
    while working:
        user_input = int(input('''
Choose a program to run:
Create an Assignment: 1
Create a Classroom: 2
Calculate Average Mark: 3
Add a student to a classroom: 4
Remove a student from a classroom: 5
Edit student information: 6


Enter # Choice: '''))

        if user_input == 1:
            create_assignment_interface()
        elif user_input == 2:
            create_classroom_interface()
        elif user_input == 3:
            average_mark_interface()
        elif user_input == 4:
            add_student_interface()
        elif user_input == 5:
            remove_student_interface()
        elif user_input == 5:
            edit_student_interface()
        
        keep_going = input('do you want to do something else y/n')
        if keep_going == 'n':
            working = False



main()
