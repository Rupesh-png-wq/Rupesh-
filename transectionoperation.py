import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="testdb"
    )

    cursor = conn.cursor()
    # First operation
    cursor.execute("INSERT INTO students (name, age, course) VALUES (%s, %s, %s)",
                   ("Amit", 22, "BCA"))

    cursor.execute("INSERT INTO students (name, age, wrong_column) VALUES (%s, %s, %s)",
                   ("Ravi", 23, "BBA"))

    conn.commit()
    print("Transaction committed successfully!")

except mysql.connector.Error as err:
    print("Error:", err)

    # Undo all changes
    conn.rollback()
    print("Transaction rolled back!")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()