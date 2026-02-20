"""Mini System Task 2:

Scenario:

Scholarship rules:
If marks ≥ 90 → 100% scholarship
If marks ≥ 80 → 50% scholarship
Otherwise → No scholarship

You must store:
Student name
Total marks
Tuition fee amount

Output:
Scholarship percentage
Final payable fee after scholarship

🎯 Think:
Which variables need calculation?
What type should marks and fee be?"""

print("----- Scholarship Calculator -----")

student_name = input("Enter your name: ")
total_marks = int(input("Enter your marks: "))
tuition_fee = float(input("Enter your tuition fee amount: "))

# Determine scholarship percentage
if total_marks >= 90:
    scholarship = 100
elif total_marks >= 80:
    scholarship = 50
else:
    scholarship = 0

# Calculate payable amount
payable_fee = tuition_fee - (tuition_fee * scholarship / 100)

# Output
print("\n----- Result -----")
print(f"Student Name        : {student_name}")
print(f"Marks               : {total_marks}")
print(f"Scholarship         : {scholarship}%")
print(f"Final Payable Amount: {payable_fee}")