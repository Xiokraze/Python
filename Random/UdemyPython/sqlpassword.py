import sqlite3
conn = sqlite3.connect("users.db")

# query = "CREATE TABLE users (username TEXT, password TEXT)"
u = input("please enter your username...")
p = input("please enter your password...")
c = conn.cursor()

# THE BAD WAY!
# query = f"SELECT * FROM users WHERE username='{u}' AND password = '{p}'"

# THE MUCH SAFER WAY
query = f"SELECT * FROM users WHERE username=? AND password =?"
c.execute(query,(u,p))

result = c.fetchone()
if(result):
	print("WELCOME BACK")
else:
	print("FAILED LOGIN")

conn.commit()
conn.close()

