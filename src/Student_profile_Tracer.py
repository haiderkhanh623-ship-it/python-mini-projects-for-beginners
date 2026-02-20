"""Mini Project 1: Student Profile Tracker

Concepts Used: Name, Age, Class, Section, Age after 5 years, Roll Number conversion
Task:

Store student name, age, class, section, roll number.

Convert roll number to integer.

Calculate age after 5 years.

Print a full student profile nicely formatted.

Outcome: Learn how to combine inputs, calculations, and formatting.


"""

name = input("Enter the name")
age = int(input("Enter the age"))
class_ = input("enter the class")
section = input("Enter the sectio")
roll_no = input("Enter the Roll_NO")

"""Convert roll number to integer."""
converted_roll_no = int(roll_no)

"""Calculate age after 5 years."""
age_after_five_years = age+5

print("---Student profile--- ")
print(f"---Student Profile---\nName: {name} | Age: {age} | Class: {class_} | Section: {section} | Roll No: {converted_roll_no} | Age after 5 years: {age_after_five_years}")

