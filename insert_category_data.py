import psycopg2
from psycopg2 import Error

def insert_category_data(Title, Description):

    try:
        
        connection = psycopg2.connect(user = 'postgres', password = 'postgres', host = 'localhost', port = 5432, database = 'sql')

        cursor = connection.cursor()

        cursor.execute("""INSERT INTO Category(Title, Description)
        VALUES(%s, %s);""", (Title, Description))
        
        connection.commit()

        print("The mission is successfuly done!")

    except(Exception, Error) as error:

        print("Error", error)
        
    finally:

        if connection:

            cursor.close()

            connection.close()

            print("Closed")

