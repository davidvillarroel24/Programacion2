import sqlite3

conn = sqlite3.connect("test30jul.db")
cursor=conn.cursor()

#cursor.execute("Insert into clientes values (130,'Maria','Alabama','2025-07-30','Premium')")
#cursor.execute("Select * from clientes")
#cursor.execute("Select * from clientes where categoria = 'Standard'")
#cursor.execute("select * from clientes join pedidos on clientes.cliente_id=pedidos.cliente_id where categoria='Premium' and estado='Entregado'")
#conn.commit()
cursor.execute("Select * from pedidos where ciudad like 's%'")

column_names = [description[0] for description in cursor.description]

rows = cursor.fetchall()

print(tuple(column_names))
for row in rows:
    print(row)

archivo=open("selectMOnto.cvs","w")    

print( tuple(column_names))
archivo.write(str(tuple(column_names)))
archivo.write("\n")

for row in rows:
    print (row)    
    archivo.write(str(row))
    archivo.write("\n")
