"""Mini System Task 3: Hostel Allocation System
Scenario:

Hostel allowed only if:
Student lives more than 50 km away
Age is 17 or above

You must store:
Name
Distance from college
Age

Output:
"Hostel Approved" or "Hostel Not Approved"

🎯 Think:
Distance should be what type?
Age validation needed?"""


print("-----Hostel Allocation System-----")
name = input("Enter your name:")
distance_from_college = int(input("Enter the distance from the college:"))
age = int(input("Enetr your age"))

if distance_from_college > 50 and age > 17:
    print("Hostel approved")
else:
    print("Hostel not approved")


