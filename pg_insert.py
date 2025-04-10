import psycopg2

try:
    conn = psycopg2.connect(user="postgres",
                            password="adiyat19",
                            host="localhost",
                            port="5432",
                            database="postgres")
    cur = conn.cursor()

    query = """INSERT INTO cake_flavours (cake_type, tasty_meter)
        VALUES (%s, %s);"""

    record = ('Red Velvet', 'Awesome')

    cur.execute(query, record)
    conn.commit()
    count = cur.rowcount
    print(count, "record has been Inserted successfully")

except (Exception, psycopg2.Error) as error:
    print("Error while Inserting record :-(", error)

finally:
    if (conn):
        cur.close()
        conn.close()
        print("Postgres connection has been closed")
