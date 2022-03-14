"""
Program: average_scores_args_and_kwargs.py
Author: Jessie Horvath
Last date modified: 03/05/2022

The purpose of this program is to allow users to input various numeric and key
word arguments, calculate the average of the numeric (GPA) arguments, and
output the students' first and last names, the course they're in and their average GPA.
"""
def average_scores(*args, **kwargs):
    # Use args for average calculation
    total = 0
    count = 0
    for num in args:
        total += num
        count += 1

    average = round((total / count), 2)

    for key, value in kwargs.items():
        if key == "first_name":
            f_name = value
        if key == "last_name":
            l_name = value
        if key == "course":
            course = value

    return f"Name: {f_name} {l_name}, GPA: {average}, Course: {course}"

if __name__ == '__main__':
    print(average_scores(4, 3.5, 4, first_name="Jessie", last_name="Horvath", course="Python"))
    print(average_scores(3.4, 4, 2, first_name = "Peter", last_name = "Parker", course = "Calculus"))
    print(average_scores(1.5, 3, 2.4, 4, 3, 2.3, 3, 3.1, last_name = "Chase", first_name = "Chevy", course = "Anthropology"))