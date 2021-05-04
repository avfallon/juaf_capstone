# This is the controller of the ZehnFunds administrative program
# This communicates between the database (SQLModel) and the view of the program (CLIView or KivyView)
# Authors: Andrew Fallon and Jeffrey Umanzor
# Last Edited: 5/3/21

from SQLModel import *
import smtplib , ssl

class Controller:

    def __init__(self):
        # Instantiate objects for database access and email functionality
        self.model = SQLModel()

    # This method executes a call to the model that creates a new account with the input information
    def addAccount(self, name, email, password):
        # This is the actual call to the database
        return self.model.addAccount(name, email, password)



    # This function takes in the email of the account to find, calls the database to find it,
    # and returns the result
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
