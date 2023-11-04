import psycopg2
from psycopg2 import Error

def insert_product_data(Title, Price, Color, Description, Category_id):

    try:
        
        connection = psycopg2.connect(user = 'postgres', password = 'postgres', host = 'localhost', port = 5432, database = 'sql')

        cursor = connection.cursor()

        cursor.execute("""INSERT INTO Product(Title, Price, Color, Description, Category_id)
        VALUES(%s, %s, %s, %s, %s);""", (Title, Price, Color, Description, Category_id))
        
        connection.commit()

        print("The mission is successfuly done!")

    except(Exception, Error) as error:

        print("Error", error)
        
    finally:

        if connection:

            cursor.close()

            connection.close()

            print("Closed")

