print("BMI CALCULATOR")

#Determine the formula of BMI in google
#Collect inputs of data need for computation and save them in variable
height = float(input("Enter the height in merters e.g 1.65 \n"))
weight = int(input("Enter the weight in kilograms e.g 72\n"))

#Calculate the BMI using the variable inputs from the user
bmi = weight / (height ** 2)

#Print the computed BMI of the user
# print("Your BMI is " + str(bmi))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")    
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")    


