'''Write a Python program to calculate the compound interest for a
given principal, rate of interest, and time period. Ask everything from the
user.'''

principal_amt = int(input("Enter Pricipal amount :"))
rate_of_interest = float(input("Enter Rate of Interest :"))
n_interest_compounded_per_year = int(input("Enter value for n :"))
t_times_in_year = int(input("Enter time in year :"))

compound_interest = principal_amt * \
    (1+(rate_of_interest/n_interest_compounded_per_year)
     )**(n_interest_compounded_per_year*t_times_in_year)
print(f"Total compound Interest :{compound_interest}")
