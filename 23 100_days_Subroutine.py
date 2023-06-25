# Adding a username and password.
username = 'admin'
password = 'adm1n'
# Defining the login function whith a while loop and nested if statements.
def login():
    while True:
        login = input("Enter Your Username: ")
        login_password = input("Enter Your Password: ")
        if login == username and login_password == password:
            print("Login Succesfull.")
            break
        elif login != username and login_password == password:
            print("We didn't find that username sorry. Please retry.")
            continue
        elif login == username and login_password != password:
            print("Password Incorrct. Please retry")
        else:
            print("Invalid username or password. Try again")
            continue
# Calling the function.
login()
print(f"Welcome {username}!")
