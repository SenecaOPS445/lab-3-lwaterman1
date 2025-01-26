#!/usr/bin/env python3

# Author ID: 123151235

# Declare the list called "my_list" before any function definition.
my_list = [100, 200, 300, 'six hundred']


def give_list():
    
    return my_list


def give_first_item():
    
    return str(my_list[0])


def give_first_and_last_item():
    
    return [my_list[0], my_list[-1]]


def give_second_and_third_item():
    
    return my_list[1:3]


if __name__ == '__main__':  # Main block
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())

