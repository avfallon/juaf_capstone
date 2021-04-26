# This is the controller of the ZehnFunds administrative program
# This contains the text-based interface functionality for that program

from SQLModel import *
import smtplib

class Controller:

    def __init__(self):
        # Instantiate objects for database access and email functionality
        self.model = SQLModel()
        #self.smtpObj = smtplib.SMTP([host[, port[, local_hostname]]] )


        print("Enter either 1, 2, 3, or 4 to access those functionalities")

        # This loop continues until the user enters 'exit'
        while True:
            response = input("1 - add new account\n2 - lookup account by email\n3 - send out update emails\n4 - exit the program\n")

            if response == "1":
                self.addAccount()

            elif response == "2":
                self.lookupAccount()

            elif response == "3":
                self.sendEmails()

            elif response == "4":
                break

            else:
                print("Sorry, please enter your selection again with just the digit 1, 2, 3, or 4")


    def addAccount(self):
        print("Adding account")
        name = input("Name of the account: ")
        email = input("Email of the account: ")
        username = input("Username of the account: ")
        password = input("Password of the account: ")

        # This is the actual call to the database
        if self.model.addAccount(name, email, username, password) == 0:
            print("Account created successfully")
        else:
            print("Error creating account")



    # This function takes in the email of the account to find, calls the database to find it,
    # and prints the result
    def lookupAccount(self):
        print("Looking up account")
        print("Enter the email of the account you want to look up")
        email = input("Email: ")

        account_result = self.model.lookupAccount(email)
        if len(account_result) != 0:
            print("That account was found successfully")
            print(account_result)
        else:
            print("That email was not found, returning to main program")


    # This function calls the database function to lookup all emails and their funds in the DB,
    # and then uses SMTP protocol to send out those emails
    def sendEmails(self):
        print("Sending emails")
        self.model.getEmailInfo()
	




Controller()
