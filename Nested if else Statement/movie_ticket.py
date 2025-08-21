'''Create a program that calculates the price of a movie ticket based on
the age of the customer. If the customer is under 12, the ticket costs $5; if
they are between 12 and 65, the ticket costs $10; otherwise, it's $7.'''


age = int(input("Enter Your Age : "))

if (age < 12):
    ticket_cost = "$5"
    print(ticket_cost)

else:
    if (age <= 65):
        ticket_cost = "$10"
        print(ticket_cost)
    else:
        ticket_cost = "$7"
        print(ticket_cost)
