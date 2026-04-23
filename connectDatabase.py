import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS testdb")
cursor.execute("USE testdb")

create_table_query = """
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    course VARCHAR(100)
)
"""

cursor.execute(create_table_query)

print("Table created successfully!")

conn.commit()
cursor.close()
conn.close()