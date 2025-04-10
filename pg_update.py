import psycopg2

try:
    conn = psycopg2.connect(user="postgres",
                            password="adiyat19",
                            host="localhost",
                            port="5432",
                            database="postgres")
    cur = conn.cursor()
    cake_id = 2
    cake_type = 'jeruk'

    # Get record as it is pre edit
    print("Table Records")
    select = """SELECT * FROM cake_flavours
                            where cake_id = %s;"""

    cur.execute(select, (cake_id, ))
    record = cur.fetchone()
    print(record)

    # Update the record
    update = """Update cake_flavours set cake_type = %s where cake_id = %s"""
    cur.execute(update, (cake_type, cake_id))
    conn.commit()
    count = cur.rowcount
    print(count, "Record Updated successfully ")

    # Print Updated Record
    newselect = """SELECT * FROM cake_flavours where cake_id = %s"""
    cur.execute(newselect, (cake_id,))
    record = cur.fetchone()
    print(record)

    # Execute
    # cur.execute(query, record)
    conn.commit()
    count = cur.rowcount
    print(count, "Record Inserted successfully!")
except (Exception, psycopg2.Error) as error:
    print("Error while Inserting record :-(", error)

finally:
    if (conn):
        cur.close()
        conn.close()
        print("Postgres connection has been closed")
