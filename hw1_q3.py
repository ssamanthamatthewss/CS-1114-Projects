"""
Author: [Samantha Matthews]
Assignment / Part: HW1 - Q3 (etc.)
Date due: 2022-09-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
print("Please enter number of coins:")
user_input_quarters = int(input("# of quarters:"))
user_input_dimes = int(input("# of dimes: "))
user_input_nickels = int(input("# of nickels: "))
user_input_pennies = int(input("# of pennies: "))

total_in_cents = (user_input_quarters * 25) + (user_input_dimes *10) + (user_input_nickels * 5) + (user_input_pennies * 1)
total_dollars = total_in_cents // 100
total_remaining_cents = total_in_cents % 100
final_output = print("Your total is", total_dollars, "dollar(s) and", total_remaining_cents, "cent(s)"  )
