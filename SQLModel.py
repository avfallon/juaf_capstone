import subprocess
import json

class SQLModel:
    def __init__(self):
        answer = subprocess.check_output(["php", "-f", "php/query.php"]);
    
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
        #print("model sending emails")
        return subprocess.check_output(["php","-f","php/getEmailInfo.php"])


    def calculateFunds(self, email):
        subprocess.call(["php","-f","php/calculateFunds.php", email])


SQLModel()
