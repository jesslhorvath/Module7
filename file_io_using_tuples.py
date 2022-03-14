"""
Program: file_io_using_tuples.py
Author: Jessie Horvath
Last date modified: 03/05/2022

The purpose of this program is a set of functions that allow the user to
pass in a student's name and enter as many test scores for the student as
they wish. The name and scores are merged into a tuple and the second
function writes the tuple to a file. The last function reads the 
file line by line and prints it to the console.
"""
import os as os

def write_to_file(tup):
    str_tup = str(tup)
    f = open('student_info.txt', 'a')
    f.write(f"{str_tup}\n")
    f.close()


def get_student_info(student_name):
    scores_list = []
    while True:
        scores = input(f"Enter test score for {student_name} or 'q' to quit: ")
        if scores == 'q':
            break
        else:
            scores_list.append(scores)


    student_record = ((student_name, scores_list))
    write_to_file(student_record)

def read_from_file():
    f = open('student_info.txt', 'r')
    for line in f:
        print(line)

if __name__ == '__main__':
    open('student_info.txt','w').close()
    get_student_info("Mary Jones")
    get_student_info("Strawberry Shortcake")
    get_student_info("Mr. Krabs")
    get_student_info("Boston Rob")
    read_from_file()