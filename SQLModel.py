import mysql.connector
import os
import subprocess


class SQLModel:
    def __init__(self, username, password, host, database):
        # main_table, referencing_table, key

        result = subprocess.run(
            ['php', 'query.php'],
            stdout=subprocess.PIPE,
            check=True
        )
        print(result.stdout)

        # value = 992.23
        # os.system("php /path/to/your/file.php %s" % (value))

    def test(self):
        print("test")


SQLModel("avfallon", "1757355", "cs-database.cs.loyola.edu", "avfallon")