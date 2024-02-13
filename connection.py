from mysql.connector import Error
import mysql.connector as sqlcon

try:
    my_db= sqlcon.connect(host="localhost", \
                          user="root",\
                          passwd="Sakshi123",\
                          database="training")
    print("Successfully connected with the database")

    cursor=my_db.cursor()
    cursor.execute("DESC COURSE_DETAILS")

    tables=cursor.fetchmany(5)
    print(tables)

except Error as e:
    print(f"Error while connecting with the database: {e}")

