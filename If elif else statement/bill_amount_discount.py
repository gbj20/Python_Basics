'''Write a program to calculate bill. Ask the final amount from the user.
You have to give discount and print the final bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount
Print the discount and the final amount to be paid.
'''
amount = int(input("Enter Final Amount:"))

if (amount >= 50000):
    amount = amount - (amount*30)/100
    print("You got 30% Discount!!", "\nYour final bill is", amount)
elif (amount >= 40000 and amount <= 49999):
    amount = amount - (amount*25)/100
    print("You got 25% Discount!!", "\nYour final bill is", amount)
elif (amount >= 30000 and amount <= 39999):
    amount = amount - (amount*20)/100
    print("You got 20% Discount!!", "\nYour final bill is", amount)
elif (amount > 10000 and amount < 29999):
    amount = amount - (amount*10)/100
    print("You got 10% Discount!!", "\nYour final bill is", amount)
else:
    print("No Discount for", amount)
