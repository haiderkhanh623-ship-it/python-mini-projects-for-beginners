"""✅ Mini System Task 5: Library Fine Calculator
Scenario:

Library fine rule:
First 5 days → No fine
After that → 10 rupees per extra day

You must store:
Student name
Days late
Fine per day (fixed 10)

Output:
Total fine

🎯 Think:
What type for days?
What calculation formula?
Edge case if days < 0?"""

print("-----Library Fine Calculator-----")
name = input("Enter your name: ")
days_late = int(input("Enter number of days late: "))

fine_per_day = 10

total_fine = fine_per_day*days_late

if days_late <= 0:
    print("No fine. Book returned on time.")
elif days_late <= 30:
    total_fine = days_late * fine_per_day
    print(f"Total Fine: Rs {total_fine}")
else:
    total_fine = days_late * fine_per_day
    print(f"Total Fine: Rs {total_fine}")
    print("Membership Blocked due to excessive delay.")