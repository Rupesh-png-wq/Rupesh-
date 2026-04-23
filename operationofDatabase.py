import mysql.connector

try:
    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="testdb"
    )

    cursor = conn.cursor()
    print("Connected to database!")

    # INSERT Operation
    insert_query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    values = ("Rahul", 20, "BCA")

    cursor.execute(insert_query, values)
    print("Record inserted!")

    # UPDATE Operation
    update_query = "UPDATE students SET age = %s WHERE name = %s"
    cursor.execute(update_query, (21, "Rahul"))
    print("Record updated!")

    # DELETE Operation
    delete_query = "DELETE FROM students WHERE name = %s"
    cursor.execute(delete_query, ("Rahul",))
    print("Record deleted!")

    # SELECT Operation
    select_query = "SELECT * FROM students"
    cursor.execute(select_query)

    records = cursor.fetchall()
    print("\nStudent Records:")
    for row in records:
        print(row)