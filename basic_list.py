"""
Program: basic_list.py
Author: Jessie Horvath
Last date modified: 03/05/2022

The purpose of this program is to prompt users for input a certain
number of times, depending on what they pass into the function. 
The make_list function validates that the user inputs a number and then 
returns the list once the number of times has been reached.
"""

def get_input():
        user_input = input("Enter some numeric input: ")
        return user_input

def make_list(n):
    input_list = []
    index = 0
    
    while index < n:
        num = get_input()
        try:
            num_as_int = int(num)
        except:
            print("That's not a number!")
        else:
            input_list.append(num_as_int)
            index += 1

    return input_list

if __name__ == '__main__':
    print(make_list(1))
    print(make_list(2))
    print(make_list(3))