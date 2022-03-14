"""
Program: search_and_sort_list.py
Author: Jessie Horvath
Last date modified: 03/05/2022

The purpose of this program is to sort a list numerically and to search for an
element in a list and return its index or position in the list. I also used
the basic_list.py script to generate random lists of numbers and used these lists
for the sort and search functions. The third function sorts a list and then 
searches for the element of interest in the sorted list.
"""
import random

def get_input():
    number_choices = [2, 34, 85, 43, 100, 23, 7, 87]
    user_input = random.choice(number_choices)
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

def sort_list():
    unsorted_list = make_list(10)
    sorted_list = sorted(unsorted_list)
    return sorted_list
    


def search_list(n):
    list_of_interest = make_list(10)
    try:
        item_of_interest = list_of_interest.index(n)
    except:
        print(f"{n} is not in the list.")
    else:
        return item_of_interest # Return statement exits the function, where the print statement simply displays the value.

def search_sorted_list(n):
    the_final_list = make_list(10)
    sorted_final_list = sorted(the_final_list)
    try:
        final_item_of_interest = sorted_final_list.index(n)
    except:
        print(f"{n} is not in the list.")
    else:
        return final_item_of_interest # Return statement exits the function, where the print statement simply displays the value.

if __name__ == '__main__':
    print(sort_list())

    # Returns the index of a number that is in the list. (Note: List creation is random so 23 may or may not be in the list.)
    print(search_list(23))
    # Returns a statement that '3' is not in the list.
    print(search_list(3))

    # Returns the index of a number that is in the list. (Note: List creation is random so 23 may or may not be in the list.)
    print(search_sorted_list(23))
    # Returns a statement that '3' is not in the list.
    print(search_sorted_list(3))
