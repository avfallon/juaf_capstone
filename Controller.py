# This is the controller of the ZehnFunds administrative program
# This contains the text-based interface functionality for that program

from SQLModel import *
import smtplib , ssl

class Controller:

    def __init__(self):
        # Instantiate objects for database access and email functionality
        self.model = SQLModel()
        #self.smtpObj = smtplib.SMTP([host[, port[, local_hostname]]] )


    def cli(self):
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
    def lookupAccount(self, email):
        return self.model.lookupAccount(email)


    # This function calls the database function to lookup all emails and their funds in the DB,
    # and then uses SMTP protocol to send out those emails
    def sendEmails(self):
        print("Sending emails")
        sender = 'juaf2021@gmail.com'
        receivers = ['jumanzor31@gmail.com']

        message = """From: From Person <from@fromdomain.com>
        To: To Person <to@todomain.com>
        Subject: SMTP e-mail test

        This is a test e-mail message.
        """

        port = 465  # For SSL
        password = 'Leuven21'
        context = ssl.create_default_context()
        smtp_server = "smtp.gmail.com"

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login("juaf2021@gmail.com", password)
            # for( user :  )



            server.sendmail(sender, receivers, message)


	




Controller()
