import subprocess


class SQLModel:
    def __init__(self):
        # main_table, referencing_table, key

        result = subprocess.run(
            ['php', 'php/query.php'],
            stdout=subprocess.PIPE,
            check=True
        )
        print(result.stdout)

        # value = 992.23
        # os.system("php /path/to/your/file.php %s" % (value))

    def test(self):
        print("test")

    def updateDB(self):
        print("updating database")

    def adminAddAccount(self):
        print("adding account")

    def adminEditAccount(self, account_id):
        print("editing account")

    def sendEmails(self):
        print("sending emails")


SQLModel()