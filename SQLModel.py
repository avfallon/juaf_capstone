import subprocess
import json

class SQLModel:
    def __init__(self):
        subprocess.call(["php", "-f", "php/query.php", "1"])

    def lookupAccount(self, email):
        print("Model looking up account")


    def addAccount(self, name, email, username, password):
        print("model adding account")
        subprocess.call(["php","-f","php/addAccount.php", name, email, username, password])


    def getEmailInfo(self):
        print("model sending emails")
        # result = subprocess.run(
        #     ['php', 'php/query.php'],
        #     stdout=subprocess.PIPE,
        #     check=True
        # )
        print(result.stdout)



SQLModel()
