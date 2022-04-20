height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
#define bmi function
BMI= weight/(height**2)
print (f"Your BMI is {BMI}")
# def bmi(h,w):
#     bmi = w / (h/100)**2
#     return bmi
if BMI < 20:
    print ("You are underweight")
elif BMI < 25:
    print ("You are normal")
elif BMI < 30:
    print ("You are overweight")
else:
    print ("You are obese")
# print (bmi(height,weight))
# print (bmi(1.8,80))
