from mysql.connector import connect, Error
from getpass import getpass

with connect(
        host="localhost",
        user="root",
        password=getpass("Enter a password")
        ) as con:
        print(con)
        sql = "use dev1"
        with con.cursor() as cur:
                cur.execute(sql)
                print(list(cur))
        sql = "show tables"
        with con.cursor() as cur:
                cur.execute(sql)
                print(list(cur))
