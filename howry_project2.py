"""
Creating a height converter

File Name: howry_project2.py
Author: Ken Howry
Date: 22.9.17
Course: COMP 1351
Assignment: Project II
Collaborators: N/A
Internet Source: N/A
"""

print("Meter to Foot Converter")

#variables
meters = float(input("Enter the height in meters: "))

feet = int(meters * 3.281)
inches = ((meters * 3.281) - feet) * 12

#program + negative_error_message
if meters >= 0:
    print(f"A height of {meters} meters is {feet} feet and {round(inches, 2)} inches.")
else:
    print("The height entered is negative. Please enter a positive value.")