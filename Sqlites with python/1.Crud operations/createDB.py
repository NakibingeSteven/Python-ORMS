import sqlite3

# Creating the Db
conn = sqlite3.connect("stevedb.db")

# print connections to db
print(f"Connections are {conn.total_changes}")

# create a cursor
cursor = conn.cursor()

# exceute the cursor
cursor.execute("CREATE TABLE food (name TEXT, kind TEXT , number INTEGER)")

# Inserting the values
query1 = "INSERT INTO food (name,kind,number) VALUES ('CAKE','Desert', 8)"
query2 = "INSERT INTO food (name,kind,number) VALUES ('CAKE2','Desert', 8)"
query2 = "INSERT INTO food (name,kind,number) VALUES ('CAKE3','Desert', 8)"
query3 = "INSERT INTO food (name,kind,number) VALUES ('CAKE4','Desert', 8)"
cursor.execute(query1)
cursor.execute(query2)
cursor.execute(query3)
cursor.execute(query4)

# Commit the changes and close the connection
conn.commit()

# reading from db
query = cursor.execute("SELECT * FROM food")
rows = query.fetchall()
print(rows)


conn.close()
