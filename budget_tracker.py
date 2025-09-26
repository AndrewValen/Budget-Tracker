"""
Andrew Valenzuela
CSC101 Python
09/26/2025
This course is for students to learn the basics of Python and apply those to weekly projects
"""
# Gathering data for monthly tracker with inputs 
total_monthly_budget = float(input("Enter your monthly budget: "))
food_expenses = float(input("Enter your food expenses: "))
rent_expenses = float(input ("Enter your rent expense: "))
entertainment_expenses = float(input("Enter your entertainment expenses: "))
# Adding all the numbers into a print() 
total_expenses = food_expenses + rent_expenses + entertainment_expenses
print("Total monthly expenses: ", total_expenses)
#subtracting expenses from monthly budget to get remainder 
remaining_budget = total_monthly_budget - total_expenses
print("Remaining budget: ", remaining_budget)
#Total expenses and remaining budget have been formatted to only take 2 decimal places
print("--- Budget Summary ---")
print("Total Monthly Budget:", total_monthly_budget)
print("Total Expenses: {:.2f}".format(total_expenses))
print("Remaining Budget: {:.2f}". format(remaining_budget))

""" 
Q1: I found that using the .2f formatter helped Python know to only take 2 decimal places.
Initially I was confused about how to call it but after reading more about it, I was 
able to implement it correctly.
Q2: Using input() on its own will create a string but if you add int or float to it, then it knows that 
it is going to give you a number instead of a string. This is what I used for this project. 
Q3: It's important that the users input goes into an input function because you want to be able to 
reuse the value without retyping it. This way it is easer to read and call back to. Placing the input into 
variables also allows for easier understand of what number belongs to which variable. 
"""