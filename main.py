#If the bill was £150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60


#Code below this line 👇

print("Welcome to the tip calculator!")
Bill = float(input("What was the total bill? £"))
Tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 0r 15? "))
Slip_bill_people = int(input("How many people to split the bill? "))

percentage = (Tip_percentage/100) * Bill 
percentage_1 = percentage + Bill
Final_bill = percentage_1 / Slip_bill_people 
final_amount = round(Final_bill, 2)
final_amount = "{:.2f}".format(Final_bill)
print(f"Each person should pay: £{final_amount}")



