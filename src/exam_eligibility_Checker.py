"""Mini System Task 1: Exam Eligibility Checker
Scenario:

A student can sit in exam only if:

Attendance is 75% or above

Fees are paid

You must store:

Student name

Attendance percentage

Fees paid (True/False)"""

print("----- Exam Eligibility Checker Scenario -----")
"""You must store:

Student name

Attendance percentage

Fees paid (True/False)"""

student_name = input("Enter your name ")
attendance_percentage = float(input("Enter your attendance %"))
fees_paid = True
#Attendance is 75% or above
if attendance_percentage  >= 75 and fees_paid == True:
    print("Eligible for exam")
else:
    print("Not eligible ")


