import psycopg2
from psycopg2 import Error

def select_product():
    try:
        connection = psycopg2.connect(user = 'postgres', password = 'postgres', host = 'localhost', port = 5432, database = 'data')
        cursor = connection.cursor()

        cursor.execute("""SELECT Product.id, Product.title, Product.category_id, Category.id, Category.title FROM Product INNER JOIN Category ON Product.category_id = Category.id;""")

        data = cursor.fetchall()

        return data
    
    except(Exception, Error) as error:
        print("Error", error)
    
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Closed")

print(select_product())