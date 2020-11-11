# Basic Login System 

'''
Create a basic login system in your python console. It should be able to ask the person for their username and password or to create an account, so if they dont have an account they can make one. To create an account ask for their email, username and 2 passwords and check if both passwords are the same. Store the information in a text file/database.  
'''
# ask user if they want to login or create an account
# ask user for username & password to login
# to create account ask for email, username, two passwords 
# validate to see if two password are correct
# store the data in a text file 

# --------------------------------------------------------------------------------------------


account = input("Do you want to create an account? (Y/N) \n")

if account == "N" or account == "n":
 username = input("Username: ")
 password = input("Password: ")

 print("")

 print("username: " + username.upper() + "\npassword: " + password.upper())  




if account == "Y" or account == "y":
 create_username = input("Username: ")
 create_email = input("Email: ")
 if "@" not in create_email:
   create_email = input("Please enter a valid email address: ")
 create_password = input("Password: ")

 print("")


 print("username: " + create_username.upper() + "\nemail: " + create_email.upper() + "\npassword: " + create_password.upper()) 






 
 














