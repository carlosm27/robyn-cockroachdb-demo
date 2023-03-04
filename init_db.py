import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')



def get_db_connection():
    conn = psycopg2.connect(
       DATABASE_URL
    )
    return conn

# Open a cursor to perform database operations
conn = get_db_connection()
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO books (title, author)'
            'VALUES (%s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens')
            )


conn.commit()

cur.close()
conn.close()