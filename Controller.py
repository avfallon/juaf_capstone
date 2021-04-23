from SQLModel import *

class Controller:

    def __init__(self):
        self.model = SQLModel()

        print("Enter either 1, 2, or 3 to access those functionalities")
        while True:
            response = input("1 - add new account\n2 - lookup account by email\n3 - send out update emails\n")

            if response == "1":
                self.addAccount()
                break
            elif response == "2":
                self.lookupAccount()
                break
            elif response == "3":
                self.sendEmails()
            else:
                print("Sorry, please enter your selection again with just the digit 1, 2, or 3")


    def addAccount(self):
        print("Adding account")
        name = input("Name of the account: ")
        email = input("Email of the account: ")
        username = input("Username of the account: ")
        password = input("Password of the account: ")
        if self.model.addAccount(name, email, username, password) == 0:
            print("Account created successfully")
        else:
            print("Error creating account")



    def lookupAccount(self):
        print("Looking up account")
        account_result = ""
        while account_result == "":
            print("Enter the email of the account you want to look up")
            email = input("Email: ")
            account_result = self.model.lookupAccount(email)
            if account_result != "":
                print(account_result)
            else:
                print("That email was not found, please try again")



    def sendEmails(self):
        print("Sending emails")
        if self.model.sendEmails() == 0:
            print("Emails sent successfully")
        else:
            print("Error sending emails")





Controller()