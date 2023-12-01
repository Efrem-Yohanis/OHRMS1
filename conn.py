import psycopg2
try:
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        user='postgres',
        password='a/ur14623/10',
        database='OHRMS',
    )
    print("Connection successful!")
    conn.close()
except psycopg2.Error as e:
    print("Unable to connect to the database:", e)