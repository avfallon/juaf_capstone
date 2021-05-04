# This file executed php scripts to communicate with the ZehnFunds database in response to Controller function calls
# Authors: Andrew Fallon and Jeffrey Umanzor
# Last Edited: 5/3/21

import subprocess
import json

class SQLModel:
    def lookupAccount(self, email):
        self.calculateFunds(email)
        print("Model looking up account")
        return subprocess.check_output(["php","-f","php/lookupAccount.php", email])

        subprocess.call(["php","-f","php/lookupAccount.php", email])
        subprocess.call(["php","-f","php/lookupPassword.php", email])


    def addAccount(self, name, email, password):
        print("model adding account")
        result = subprocess.check_output(["php","-f","php/addAccount.php", name, email, password])

        print("SQLModel output: ", result)


    def getEmailInfo(self):
        print("model sending emails")
        #return subprocess.check_output(["php","-f","php/getEmailInfo.php"])

    def calculateFunds(self, email):
        subprocess.call(["php","-f","php/calculateFunds.php", email])

    def save_account(self, name, email, password):
        print("Saving account")
        print(name, email, password)

    def delete_account(self, email):
        print("Deleting Account")
        #subprocess.call(["php","-f","php/deleteAccount.php", email])



SQLModel()
