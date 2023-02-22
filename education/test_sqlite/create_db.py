import sqlite3 as sql
import os
import sys

print(os.path.abspath(__file__))
print(os.path.dirname(__file__))
print(os.getcwd())
data_dir_path = os.path.join(os.path.dirname(__file__), 'data')
database_path = os.path.join(data_dir_path, 'testsqlite.db')
print(database_path)
if os.path.exists(data_dir_path):
    print('data is exists')
else:
    os.mkdir(data_dir_path, mode=0o777)
    sys.path.append(data_dir_path)

con = sql.connect(database_path)


with con:
    data = con.execute("select count(*) from sqlite_master where type='table' and name = 'users'")
    for row in data:
        if row[0] == 0:
            print(row)
            with con:
                con.execute("""CREATE TABLE users (user_id INTEGER PRIMARY KEY
                    , process_date INTEGER
                    , process_dtime INTEGER
                    , password_hash VARCHAR(100));
                """)
        else:
            with con:
                print('database is exist')
                data = con.execute("SELECT * FROM users")
                for row in data:
                    print(row)

current_dir = os.getcwd()
users_scheme_path = os.path.join(current_dir, 'schemas', 'users.sql')
with open(users_scheme_path) as f:
    con.executescript(f.read())

cur = con.cursor()

cur.execute("INSERT INTO users (user_email, user_name) VALUES (?, ?)",
            ('keka@mail.ru', 'Keka')
            )

cur.execute("INSERT INTO comments (title, content, user_id) VALUES (?, ?, ?)",
            ('kek', 'lol cheburek', 1)
            )

cur.execute("INSERT INTO comments (title, content, user_id) VALUES (?, ?, ?)",
            ('kek2', 'lol bez chebureka', 1)
            )

con.commit()
con.close()
