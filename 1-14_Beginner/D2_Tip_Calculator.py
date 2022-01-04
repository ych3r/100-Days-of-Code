print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

if total_bill >= 0 and 0 <= percentage_tip <= 100:
    total_bill *= (1 + percentage_tip / 100)
    pay = round(total_bill / people, 2)
    print(f"Each person should pay: {pay}")
else:
    print("error")
