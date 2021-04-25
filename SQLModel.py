import subprocess
import json

class SQLModel:
    def __init__(self):
        subprocess.call(["php", "-f", "query.php", "1"])

    def lookupAccount(self, email):
        print("Model looking up account")
        self.cursor.execute("SELECT * FROM %s WHERE %s = '%s';"
                            % (self.user_info, self.key, email))
        return self.cursor.fetchall()


    def addAccount(self, name, email, username, password):
        print("model adding account")


    def getEmailInfo(self):
        print("model sending emails")
        # result = subprocess.run(
        #     ['php', 'php/query.php'],
        #     stdout=subprocess.PIPE,
        #     check=True
        # )
        print(result.stdout)



SQLModel()
