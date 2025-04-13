import math

# Asking For Height and Weight and Calculating BMI
height=int(input("What is your height in inches?\n"))
if(height>0 and height<100):
    weight=int(input("What is your weight in pounds?\n"))
else:
    print("Please put your height as a positive integer less than 100")
    height=int(input("What is your height in inches?\n"))

if(weight>0 and weight<1000):
        BMI=(weight*703)/(height**2)
else:
    print("Please put your weight as a positive integer less than 1000")

# Printing BMI
print("Your BMI is %.2f"%+BMI)
