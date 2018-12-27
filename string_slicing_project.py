#input email of user

email = input("enter your email ID ?")

#sachinkafle365@gmail.com

#slice name from the input email

username = email[:email.index("@"):]

domain = email[email.index("@") +1:email.index("."):]

#print the info of user

print("hey your name is {0} and your email domain is {1}".format(username,domain))