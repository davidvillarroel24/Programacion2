import sqlite3

conn = sqlite3.connect("sales_database.db")
cursor=conn.cursor()

cursor.execute("SELECT * FROM Clients")
rows = cursor.fetchall()
print(" - Tabla 'Clients' (5 Registros)" )
for row in rows:
    print (row)


cursor.execute("SELECT * FROM Clients WHERE city = 'New York'")
rows = cursor.fetchall()
print("\n - Tabla 'Clients' (Now York)" )
for row in rows:
    print (row)

    