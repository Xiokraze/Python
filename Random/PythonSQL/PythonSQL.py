import sqlite3


def createTable(con):
    c = con.cursor()
    c.execute("CREATE TABLE friends (firstName TEXT, lastName TEXT, age INTEGER)")
    return

def insertOne(con):
    c = con.cursor()

    #insertQuery = '''INSERT INTO friends VALUES ('Joshua', 'Worthington', 31)'''    
    #c.execute(insertQuery)

    #fname = "Joshua"
    #insertQuery = f"INSERT INTO friends (firstName) VALUES ('{fname}')"
    #c.execute(insertQuery)

    #fname = "Joshua"
    #insertQuery = f"INSERT INTO friends (firstName) VALUES (?)"
    #c.execute(insertQuery, (fname,))

    data = ("Joshua", "Worthington", 31)
    query = "INSERT INTO friends VALUES (?,?,?)"
    c.execute(query, data)
    return

def insertBulk(con):
    people = [
	    ("Roald","Amundsen", 5),
	    ("Rosa", "Parks", 8),
	    ("Henry", "Hudson", 7),
	    ("Neil","Armstrong", 7),
	    ("Daniel", "Boone", 3)]
    c = con.cursor()

    #Method 1
    c.executemany("INSERT INTO friends VALUES (?,?,?)", people)

    #Method 2
    average = 0
    for person in people:
        c.execute("INSERT INTO friends VALUES (?,?,?)", person)
        average += person[2]
    print(average / len(people))
    return

def selectStuff(con):
    c = con.cursor()
    data = c.execute("SELECT * FROM friends")

    # Print all 1
    #for result in data:
    #    print(result)

    # Print all 2
    #print(data.fetchall())
    
    # Print specific 1
    #data = c.execute("SELECT * FROM friends WHERE firstName IS 'Joshua'")
    #print(data.fetchall())

    # Print specific 2
    #data = c.execute("SELECT * FROM friends WHERE age > 0 ORDER BY age")
    #print(data)
    #print(data.fetchall())
    return

def main():
    connection = sqlite3.connect("friends.db")
    #createTable(connection)
    #insertOne(connection)
    #insertBulk(connection)
    #selectStuff(connection)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    main()