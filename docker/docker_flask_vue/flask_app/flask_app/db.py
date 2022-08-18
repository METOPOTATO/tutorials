import mysql.connector

def create_table():

    mydb = mysql.connector.connect(
    host="mysql_flask_app",
    user="linh",
    password="1234",
    database="db_test"
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")