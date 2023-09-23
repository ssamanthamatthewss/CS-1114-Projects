# CS-1114-Projects  


[cs1114 hw1 readme.pdf](https://github.com/ssamanthamatthewss/CS-1114-Projects/files/12707454/cs1114.hw1.readme.pdf)

"""
Author: [Samantha Matthews]
Assignment / Part: HW1 - Q1 (etc.)
Date due: 2022-09-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

user_name = input("Please enter your name: ")
user_age = input("Please enter your age: ")
user_welcome_message = print(user_name, ",", user_age, "," "is taking CS-UY 1114")
print(user_welcome_message)


"""
Author: [Samantha Matthews]
Assignment / Part: HW1 - Q2 (etc.)
Date due: 2022-09-22, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""
current_population = 330109174
current_year = 2022
user_year = int(input("Please enter a year greater than 2022: "))

new_birth = (((((user_year - current_year) * 365) * 24) * 60) * 60) // 9
new_death = (((((user_year - current_year) * 365) * 24) * 60) * 60) // 18
new_immigrant = (((((user_year - current_year) * 365) * 24) * 60) * 60) // 40
new_emigration = (((((user_year - current_year) * 365) * 24) * 60) * 60) // 60

print("The approximated population is", (current_population + new_birth + new_immigrant) - new_death - new_emigration)


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
