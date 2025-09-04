# logical operators = used on conditional statements
# and = checks two or more conditions if true
# or = checks if at least one conditions is true
# not = true if condition is false
# condional expression = a one line shortcut for if else statment (ternary operator)
# print or assign one or two values based on condion
# x if condition else y
user_name = input("Enter your name: ")
if len(user_name) > 12:
    print("you're name is greater than 12")
else:
    print("WELOME! {user_name}")
