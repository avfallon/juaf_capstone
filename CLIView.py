# This file acts as the text-based view of the ZehnFunds administrative program
# Authors: Andrew Fallon and Jeffrey Umanzor
# Last Edited: 5/3/21

from Controller import *

class CLIView:
    def __init__(self):
        self.controller = Controller()
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
        password = input("Password of the account: ")

        self.controller.addAccount(name, email, password)

    def lookupAccount(self):
        print("Looking up acount")
        email = input("Enter the email you would like to search for: ")

        self.controller.lookupAccount(email)

    def sendEmails(self):
        print("Sending Emails")
        self.controller.sendEmails()

CLIView()