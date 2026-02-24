user = input("Enter username: ")
password = input("Enter password: ")

if user == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")