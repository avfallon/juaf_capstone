# This is the controller of the ZehnFunds administrative program
# It communicates between the database (SQLModel) and the view (CLIView or KivyView)
# Authors: Andrew Fallon and Jeffrey Umanzor
# Last Edited: 5/3/21

from SQLModel import *
import smtplib , ssl

class Controller:

    def __init__(self):
        # Instantiate objects for database access and email functionality
        self.model = SQLModel()


    def addAccount(self, name, email, password):
        # This is the actual call to the database
        return self.model.addAccount(name, email, password)



    # This function takes in the email of the account to find, calls the database to find it,
    # and returns the result
    def lookupAccount(self, email):
        print(self.model.lookupAccount(email))

    # Save account
    def save_account(self, name, email, password):
        self.model.save_account(name, email, password)

    # Delete account
    def delete_account(self, email):
        self.model.delete_account(email)

    # This function calls the database function to lookup all emails and their funds in the DB,
    # and then uses SMTP protocol to send out those emails
    def sendEmails(self):
        #print("Sending emails")
        sender = 'juaf2021@gmail.com'
        receivers = ['juaf2021@gmail.com']

#        message = """From: From Person <from@fromdomain.com>
#        To: To Person <to@todomain.com>
#        Subject: SMTP e-mail test
#
#        This is a test e-mail message.
#        """

        port = 465  # For SSL
        password = 'Leuven21'
        context = ssl.create_default_context()

        smtp_server = "smtp.gmail.com"
        
        #emails = self.model.getEmailInfo().strip().decode('ascii')
        emails=""
        print(emails)
                
        emails2 = emails.split("|||")
        
        print(emails2)
        print(len(emails2))
        
        #emails3 = emails2.split("-")
        
        print(emails2[0].split("-"))
        
        count = 1 
        
        #print("\n---" + emails + "\n---")
#
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login("juaf2021@gmail.com", password)
            for i in emails2:
                  if( count < len(emails2) ):
                    user , funds = i.split("-")
                    print(user , funds)
#                    message = """From: ZehnFunds <juaf2021@gmail.com>
#                            To: ZehnFunds Member  <juaf2021@gmail.com>
#                            Subject: Reminder of points.
#                            
#                            This is a reminder of the points you have in your account! You have over 100 points! Redeem Now!
#                            """
                    message = """From: From ZehnFunds <juaf2021@gmail.com>
                    To: To ZehnFunds Member 
                    Subject: Funds Reminder
            
                    This is a reminder that you have points to spend!
                    """ 
                    server.sendmail(sender, receivers, message)
                    count += 1
            #server.sendmail(sender, receivers, message)


	




Controller()
