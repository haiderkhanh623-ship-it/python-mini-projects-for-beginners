"""You already calculated BMI before.

Now classify:

BMI < 18.5 → Underweight
18.5–24.9 → Normal
25–29.9 → Overweight
30+ → Obese

🎯 Think:

What type should height and weight be?
How many conditions needed?"""

print("-----BMI Health Classification-----")
height = float(input("Enter the height:"))
weight = float(input("Enter the weight"))

bmi = weight/height**2

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
     print("overweight")
else:
    print("obese")