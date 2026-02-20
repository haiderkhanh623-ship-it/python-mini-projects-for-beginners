"""Mini Project 1 – Level 2 Upgrade

Now improve your Student Profile Tracker with these additions:

🎯 New Requirements

Show profile in proper formatted structure (multi-line report).

Add validation:

If age is less than 3 → show warning.

Remove unnecessary duplicate roll number printing.

Add a final summary sentence like:

----------- Student Profile -----------
Name           : Haider
Age            : 23
Class          : BS AI
Section        : B
Roll Number    : 0065
Age After 5 Yrs: 28
---------------------------------------
Haider will be 28 years old after 5 years."""

name = input("Enter the name: ")
age = int(input("Enter the age: "))
class_ = input("Enter the class: ")
section = input("Enter the section: ")
roll_no = input("Enter the roll number: ")

age_after_five = age + 5

# Validation
if age < 3:
    print("Warning: Age seems invalid for a school student.")

print("----------- Student Profile -----------")
print(f"Name           : {name}")
print(f"Age            : {age}")
print(f"Class          : {class_}")
print(f"Section        : {section}")
print(f"Roll Number    : {roll_no}")
print(f"Age After 5 Yrs: {age_after_five}")
print("---------------------------------------")
print(f"{name} will be {age_after_five} years old after 5 years.")

