# Basic Login System 

'''
Create a basic login system in your python console. It should be able to ask the person for their username and password or to create an account, so if they dont have an account they can make one. To create an account ask for their email, username and 2 passwords and check if both passwords are the same. Store the information in a text file/database.  
'''
# ask user if they want to login or create an account
# ask user for username & password to login
# to create account ask for email, username, two passwords 
# validate to see if two password are correct
# store the data in a text file 

# --------------------------------------------------------------------------------


account = input("Do you want to create an account? (Y/N) \n").lower()

if account == "no":
 username = input("Username: ")
 password = input("Password: ")
 print("username: ", username.upper(), "password: ", password.upper()) 






 
 














