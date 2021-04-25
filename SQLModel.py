import mysql
import json

class SQLModel:
    def __init__(self, username, password, host, database):
        self.mydb = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=database,
        )
        self.db = database
        self.cursor = self.mydb.cursor()
        self.user_info = "user_info"
        self.login_info = "login_info"
        self.purchase_table = "purchase_table"
        # Key for this table is the recipe name, all recipe names must be unique
        self.key = "account_email"

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
