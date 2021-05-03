import subprocess
import json

class SQLModel:

    def lookupAccount(self, email):
        print("Model looking up account")
        return subprocess.check_output(["php","-f","php/lookupAccount.php", email])


    def addAccount(self, name, email, username, password):
        print("model adding account")
        subprocess.call(["php","-f","php/addAccount.php", name, email, username, password])


    def getEmailInfo(self):
        print("model sending emails")
        subprocess.call(["php","-f","php/getEmailInfo.php"])
	# result = subprocess.run(
        #     ['php', 'php/query.php'],
        #     stdout=subprocess.PIPE,
        #     check=True
        # )
        # print(result.stdout)



SQLModel()
