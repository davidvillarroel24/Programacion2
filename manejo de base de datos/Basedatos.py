import sqlite3
from datetime import datetime

# Crear/conectar a la base de datos SQLite
conn = sqlite3.connect('sales_database.db')
cursor = conn.cursor()

# Crear tabla Clients
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clients (
    client_id INTEGER PRIMARY KEY,
    client_name TEXT NOT NULL,
    city TEXT NOT NULL
)
''')

# Crear tabla Orders
cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY,
    sale_id INTEGER,
    client_id INTEGER,
    city TEXT NOT NULL,
    amount REAL NOT NULL,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
)
''')

# Insertar datos en Clients
clients_data = [
    (101, 'John Doe', 'New York'),
    (102, 'Jane Smith', 'New York'),
    (103, 'Jim Beam', 'Los Angeles'),
    (104, 'Jill Jackson', 'Los Angeles'),
    (105, 'Jack Johnson', 'Chicago')
]

cursor.executemany('INSERT INTO Clients (client_id, client_name, city) VALUES (?, ?, ?)', clients_data)

# Insertar datos en Orders
orders_data = [
    (1, 1, 101, 'Los Angeles', 1000.00),
    (2, 2, 102, 'New York', 1500.50),
    (3, 3, 103, 'Chicago', 2000.00),
    (4, 4, 104, 'New York', 2500.75),
    (5, None, None, 'Los Angeles', 3000.00)
]

cursor.executemany('''
INSERT INTO Orders (order_id, sale_id, client_id, city, amount)
VALUES (?, ?, ?, ?, ?)
''', orders_data)

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("Base de datos 'sales_database.db' creada con:")
print("   - Tabla 'Clients' (5 registros)")
print("   - Tabla 'Orders' (5 registros)")