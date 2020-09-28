"""
Markbook Application
Group members: Ethan, Seung Joo, Nicholas
"""
import json
import os
from typing import Dict

"""Ethan"""


def create_assignment(name: str, due: str, points: int) -> Dict:
    """Creates an assignment represented as a dictionary
    Args:
        name: the name of the assignment.
        due: the due date for the assignment.
        points: what the assignment is out of (denominator).
    Returns:
        Assignment as a dictionary.
    """
    # makes a dictionary with key-value pairs of name, due, and points
    assignment_dict = {
        "name": name,
        "due": due,
        "points": points
    }

    return assignment_dict

"""Nicholas"""


def create_classroom(course_code: str, course_name: str,
                     period: int, teacher: str) -> Dict:
    """Creates a classroom dictionary"""
    """makes a dictionary with key-value pairs of course_code, course_name,
    period, teacher, student_list, and assignment_list"""
    classroom = {
        'course_code': course_code,
        'course_name': course_name,
        'period': period,
        'teacher': teacher,
        'student_list': [],
        'assignment_list': []
    }
    with open('classroom.txt', 'w') as f:
        json.dump(classroom, f)
    return classroom
# Seung Joo


def calculate_average_mark(student: Dict) -> float:
    """Calculates the average mark of a student"""
    # sorts elements of a given list in ascending order
    student['marks'].sort()
    total = 0
    lowest = 100
    for mark in student["marks"]:
        if mark < lowest:
            lowest = mark
    for mark in student['marks']:
        if mark != lowest:
            total += mark
    # calculates the average of the marks
    average = int(total / (len(student['marks']) - 1))
    return average
# answer = calculate_average_mark()

"""Ethan and Nicholas"""


def add_student_to_classroom(student: Dict, classroom: Dict):
    """Adds student to a classroom

    Args:
        student: Student dict
        classroom: The classroom to add the student to
    """
    # a student is appended to the classroom
    classroom['student_list'].append(student)
    with open('classroom.txt', 'w') as f:
        json.dump(classroom, f)
    return classroom


"""Ethan"""


def remove_student_from_classroom(student: Dict, classroom: Dict):
    """Removes student from classroom

    Args:
        student: The student to be removed
        classroom: the class from which the student will be removed.
    """
    i = classroom['student_list'].index(student)
    # removes student from the classroom dictionary
    # classroom['student_list'].remove(student)
    del classroom['student_list'][i]
    with open('classroom.txt', 'w') as f:
        json.dump(classroom, f)
    return classroom

"""Nicholas"""


def edit_student(student: Dict, **kwargs: Dict):
    """Edits the student's info with the provided key/value pairs

    Args:
        student: The student whose data needs to be udated.
        **kwargs: KeyWordARGumentS. The key/value pairs of the
            data that needs to be changed. Can come in the form
            of a dictionary.
    """
    with open('classroom.txt') as f:
        classroom = json.load(f)

    i = classroom['student_list'].index(student)
    """ replaces the first name of the student dictionary
    with the first name of the kwargs dictionary"""
    student["first_name"] = kwargs["first_name"]
    """replaces the last name of the student dictionary
    with the last name of the kwargs dictionary"""
    student["last_name"] = kwargs["last_name"]

    classroom['student_list'][i] = student
    with open('classroom.txt', 'w') as f:
        json.dump(classroom, f)
    return student

"""Nicholas, Seungjoo and Ethan worked together for the rest of this code"""


def create_assignment_interface():
    os.system('clear')
    print('--------------------------------------------------------------- Create Assignment ---------------------------------------------------------------')
    name = input('Enter assignment name: ')
    due_date = input('Enter due date: ')
    # makes sure that the user inputs an integer
    while True:
        try:
            marks = int(input('Enter maximum points: '))
        except:
            print('Points must be a number, please try again.')
        else:
            break
    print(create_assignment(name, due_date, marks))


def create_classroom_interface():
    os.system('clear')
    print('--------------------------------------------------------------- Create Classroom ---------------------------------------------------------------')
    code = input('Enter the course code: ')
    course_name = input('Enter the course name: ')
    # makes sure that the user enters an integer
    while True:
        try:
            period = input('Enter the period: ')
        except:
            print('Period must be a number, please try again.')
        else:
            break
    teacher = input('Enter the teacher name: ')
    # names = input('Enter the student list: ')
    # student_list = names.split()
    # assignments = input('Enter the assignment list: ')
    # assignment_list = assignments.split()
    print(create_classroom(code, course_name, period, teacher))
    # args: course_code: str, course_name: str, period: int, teacher: str
    # pass


def average_mark_interface():
    os.system('clear')
    print('--------------------------------------------------------------- Average Mark ---------------------------------------------------------------')
    # makes sure that the user enters an integer
    while True:
        try:
            marks = input("Enter list of marks: ")
        except:
            print("Marks must be numbers.")
        else:
            break
    # splits the string into a list
    mark_list = marks.split(', ')
    i = 0
    """converts the strings into integers by
    iterating through the list with a for loop"""
    for mark in mark_list:
        mark_list[i] = int(mark)
        i += 1
    # assigns the marks key with the list of inputted marks
    student = {"marks": mark_list}
    print(calculate_average_mark(student))
    """ args: student: Dict ->
    within dict is ['marks': example marks: 10, 20, 30]"""


def add_student_interface():
    """args: student: Dict, classroom: Dict"""
    os.system('clear')
    print('-------------------------------------------------------------------- Add Student --------------------------------------------------------------------')
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")
    while True:
        try:
            grade = int(input("Enter the student's grade: "))
        except:
            print('The grade must be a number, please try again.')
        else:
            break
    marks = input('Enter any marks the student has (Make sure to seperate marks with a ", "): ').split(', ')
    with open('classroom.txt', 'r') as f:
        classroom = json.load(f)
    student = {
        'first_name': first_name,
        'last_name': last_name,
        'grade': grade,
        'marks': marks
    }
    print(add_student_to_classroom(student, classroom))


def remove_student_interface():
    """args: student: Dict, classroom: Dict"""
    os.system('clear')
    print('-------------------------------------------------------------------- Remove Student --------------------------------------------------------------------')
    first_name = input("Enter the student's first name: ")
    last_name = input("Enter the student's last name: ")
    with open('classroom.txt') as f:
        classroom = json.load(f)

    if classroom['student_list'] != []:
        for person in classroom['student_list']:
            if person['first_name'] == first_name and person['last_name'] == last_name:
                student = person
                print(remove_student_from_classroom(student, classroom))
    else:
        print('No student to remove')

"""Ethan"""


def edit_student_interface():
    """args: student: Dict, **kwargs: Dict"""
    os.system('clear')
    print("---------------------------------------------------------------- Edit student -----------------------------------------------")
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")

    new_first = input("Enter student's new first name: ")
    new_last = input("Enter student's new last name: ")

    with open('classroom.txt') as f:
        classroom = json.load(f)

    for person in classroom['student_list']:
        if person['first_name'] == first_name and person['last_name'] == last_name:
            student = person

    print(edit_student(student, first_name=new_first, last_name=new_last))


def main():
    working = True
    os.system('clear')
    print("------------------------------------------------------- Welcome to the Python Teacher Markbook -------------------------------------------------------")
    while working:
        os.system('clear')
        print("------------------------------------------------------- Welcome to the Python Teacher Markbook -------------------------------------------------------")
        user_input = int(input('''
Choose a program to run:
1: Create an Assignment
2: Create a Classroom
3: Calculate Average Mark
4: Add a student to a classroom
5: Remove a student from a classroom
6: Edit student information


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
        elif user_input == 6:
            edit_student_interface()

        keep_going = input('Return to menu? (y/n): ')
        if keep_going == 'n':
            working = False

main()
