import psycopg2
from psycopg2 import Error

try:
    
    connection = psycopg2.connect(user = 'postgres', password = 'postgres', host = 'localhost', port = 5432, database = 'sql')

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE Category(
                   ID SERIAL PRIMARY KEY,
                   Title VARCHAR(100) NOT NULL,
                   Description TEXT NULL);""")
    
    connection.commit()

    print("The mission is successfuly done!")

except(Exception, Error) as error:

    print("Error", error)
    
finally:

    if connection:

        cursor.close()

        connection.close()

        print("Closed")

