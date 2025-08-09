#para usar la base de datos en la nube instalar 
#pip install python-dotenv psycopg2-binary

import psycopg2
#import sqlite3

try:
    conn = psycopg2.connect(
        host="db.bsqnzzsmcdndqxxofvvd.supabase.co",
        database="postgres",  # Or your specific database name
        user="postgres",
        password="%*J99qv#q#faVkj",
        port="5432"  # Or the port specified by Supabase
    )
    print("Connected to Supabase!")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM global_freelancers WHERE country='Italy'")
    #cursor.execute("SELECT * FROM pedidos'")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as e :
    print("error ", e)

