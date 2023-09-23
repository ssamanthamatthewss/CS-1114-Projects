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
