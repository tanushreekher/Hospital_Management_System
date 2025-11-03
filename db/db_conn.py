import mysql.connector
def connection():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "NewPassword@123",
        database = "Hospital_Management_System"
    )
    return conn
