#Password for user to enter
Password = "raunak"

user_input = ("Type the password ")

while user_input != Password:
    if Password != user_input:
        input("You were wrong, try again") 
    else:
        print("You got the correct password")
        Password = user_input