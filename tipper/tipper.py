bill_amount = float(input("Please enter the bill amount. "))
while(bill_amount != 0):
    percent_amount = int(input("Do you want to tip 15 or 20%? ")) / 100

    if(percent_amount == .15 or percent_amount == .2):
        tip_amount = percent_amount * bill_amount
        total = bill_amount + tip_amount
        print("\nThe tip amount is ${:,.2f}.".format(tip_amount))
        print("The total is ${:,.2f}.\n".format(total))
    else:
        print("Please enter a valid tip percentage.\n")

    bill_amount = float(input("Please enter the bill amount. "))


