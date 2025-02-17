#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Created :   2025/02/10 09:51:04
@Desc    :   Week 5 Exercises, uncomment each section to test the code
@Ref     :   
'''

# For beginners, all code in a single file without functions 
board_size = 10 
valid_orientations = ['horizontal', 'vertical']
is_valid = True

# Exercise 1: Basic Conditional Statements 
x, y = 5, 8

# TODO : 1. Check if coordinates are within the valid range
if x < 0 or x >= board_size:
    is_valid = False

if y < 0 or y >= board_size:
    is_valid = False

print(f"Coordinates {(x, y)} are valid: {is_valid}")


# # One more example 
# x, y = 10, -1

# # TODO : 2. Check if coordinates are within the valid range 
# # # Copy your code of TODO 1 here to test on x, y = 10, -1
# if x < 0 or x >= board_size:
#     is_valid = False

# if y < 0 or y >= board_size:
#     is_valid = False

# print(f"Coordinates {(x, y)} are valid: {is_valid}")


# # Exercise 2: Conditional with Logical Operators 
# x, y, orientation = 4, 6, 'horizontal'

# # TODO : 3. Validate user input for coordinates and orientation 
# # Add you code of TODO 3 here
# if x < 0 or x >= board_size:
#     is_valid = False

# if y < 0 or y >= board_size:
#     is_valid = False

# if orientation not in valid_orientations:
#     is_valid = False
# print(f"Input {(x, y, orientation)} is valid: {is_valid}")


# # One more example
# x, y, orientation = 11, 3, 'diagonal'

# # TODO : 4. Validate user input for coordinates and orientation 
# # Copy your code of TODO 3 here to test on x, y, orientation = 11, 3, 'diagonal'
# if x < 0 or x >= board_size:
#     is_valid = False

# if y < 0 or y >= board_size:
#     is_valid = False

# if orientation not in valid_orientations:
#     is_valid = False
# print(f"Input {(x, y, orientation)} is valid: {is_valid}")


# # Exercise 3: Nested Conditionals
# x, y, ship_length, orientation = 3, 5, 4, 'horizontal' 

# # TODO : 5. Validate the placement of a ship # Add you code of TODO 5 here
# if x < 0 or x >= board_size:
#     is_valid = False
# if y < 0 or y >= board_size:
#     is_valid = False

# if orientation == 'horizontal':
#     if x + ship_length > board_size:
#         is_valid = False
# elif orientation == 'vertical':
#     if y + ship_length > board_size:
#         is_valid = False
# else:
#     is_valid = False

# print(f"Placement {(x, y, ship_length, orientation)} is valid: {is_valid}")


# # One more example
# x, y, ship_length, orientation = 7, 7, 4, 'vertical' 

# # TODO : 6. Validate the placement of a ship # Copy your code of TODO 5 here to test on x, y, ship_length, orientation = 7, 7, 4, 'vertical'
# if x < 0 or x >= board_size:
#     is_valid = False
# if y < 0 or y >= board_size:
#     is_valid = False

# if orientation == 'horizontal':
#     if x + ship_length > board_size:
#         is_valid = False
# elif orientation == 'vertical':
#     if y + ship_length > board_size:
#         is_valid = False
# else:
#     is_valid = False

# print(f"Placement {(x, y, ship_length, orientation)} is valid: {is_valid}")