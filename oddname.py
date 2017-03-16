"""
Ask user for their name and print every second letter.
"""

# Prompt user for name
user_name = input("Enter name: ")

# Ensure name is not blank
while user_name == "":
    print("Please do not leave blank.")
    user_name = input("Enter name: ")

# Print out every second character
print_string = user_name[0:len(user_name):2] # every second letter from first to last letter
print(print_string)
