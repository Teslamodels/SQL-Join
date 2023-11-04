import psycopg2
from psycopg2 import Error

try:
    
    connection = psycopg2.connect(user = 'postgres', password = 'postgres', host = 'localhost', port = 5432, database = 'sql')

    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE Product(
                   ID SERIAL PRIMARY KEY,
                   Title VARCHAR(100) NOT NULL,
                   Price NUMERIC NOT NULL,
                   Color VARCHAR(100) NULL,
                   Description TEXT NULL,
                   Category_id INTEGER NOT NULL);""")
    
    connection.commit()

    print("The mission is successfuly done!")

except(Exception, Error) as error:

    print("Error", error)
    
finally:

    if connection:

        cursor.close()

        connection.close()

        print("Closed")

