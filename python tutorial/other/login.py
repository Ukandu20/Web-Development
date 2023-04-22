#Simple Signup/Login System
print("Create Account")
username = input("Username: ")
password = input("Password: ")

print("Your account has been created Succesfully!")
print("Login to your account")

username1 = input("Username: ")
password1 = input("Password: ")

#Check if password is correct


if username == username1 and password == password1:
    print("You have logged in Succesfully!")
else:
    print("Incorrect Username or Password")


