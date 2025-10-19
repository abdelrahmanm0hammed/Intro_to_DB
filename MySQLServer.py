import mysql.connector

try:
    # Establish a connection to the MySQL server (without specifying a database initially)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password"
    )

    mycursor = mydb.cursor()

    # Execute the CREATE DATABASE command
    alx_book_store = "alx_book_store"
    mycursor.execute(f"CREATE DATABASE {alx_book_store}")

    print(f"Database '{alx_book_store}' created successfully.")

except mysql.connector.Error as err:
    print(f"Error creating database: {err}")

finally:
    if 'mydb' in locals() and mydb.is_connected():
        mycursor.close()
        mydb.close()