import os

print("Login")

# Getting the username
user = input("What is your username: ")
print(f"Hello, {user}!")

# Setting up the password
password = input("Enter what you want as your password: ")

# Choosing between calculator or notepad
app = input("Would you like 'calc' or 'notepad'?: ")

# Confirming the choice and opening the selected application
if app.lower() == "calc":
    print("Opening Calculator...")
    os.system("calc")  # Opens Calculator on Windows
elif app.lower() == "notepad":
    print("Opening Notepad...")
    os.system("notepad")  # Opens Notepad on Windows
else:
    print("Invalid choice. Please choose 'calc' or 'notepad'.")

