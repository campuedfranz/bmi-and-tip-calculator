print("WELCOME TO TIP CALCULATOR")

#Get the total bill and save it to a variable
total_bill = float(input("What was the total bill? $"))

#Percentage tip available and let user choose
#Save the user input in a variable
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))

#How many peopel will split the bill and save the input to a variable
customer_count = int(input("How many people to split the bill?"))

#Compute the tip
tip = total_bill * (tip_percentage/100)

#Add the tip and the bill
bill_plus_tip = total_bill + tip

#Compute the share of each customer of bill and tip
share_of_each_customer = round(bill_plus_tip / customer_count,2)

#Print the share in console
print(f"Each customer should pay: ${share_of_each_customer}")