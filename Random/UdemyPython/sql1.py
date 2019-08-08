import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()
# execute some sql
 c.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")
# insert_query = '''INSERT INTO friends 
# 					VALUES ('Merriwether', 'Lewis', 7)'''

# BAD! DO NOT DO THIS!
# form_first = "Dana"
# query = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"

# BETTER WAY!
# form_first = "Mary-Todd"
# query = f"INSERT INTO friends (first_name) VALUES (?)"
# c.execute(query, (form_first,))

data = ("Steve", "Irwin", 9)
query = "INSERT INTO friends VALUES (?,?,?)"
c.execute(query, data)
# commit changes
conn.commit()
conn.close()



