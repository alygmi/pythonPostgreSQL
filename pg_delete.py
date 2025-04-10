import psycopg2


def deletecake(cake_id):
    try:
        conn = psycopg2.connect(user="postgres",
                                password="adiyat19",
                                host="localhost",
                                port="5432",
                                database="postgres")
        cur = conn.cursor()
        # view record before deleting
        print("Cake records")
        select = """SELECT * FROM cake_flavours
                                where cake_id = %s;"""
        cur.execute(select, (cake_id, ))
        record = cur.fetchone()
        print(record)

        # Delete the frigging cake
        delete = """Delete FROM cake_flavours
                    where cake_id = %s"""
        cur.execute(delete, (cake_id, ))
        conn.commit()
        count = cur.rowcount
        print(count, "cake has been successfully deleted")

    except (Exception, psycopg2.Error) as error:
        print("Error encountered while deleting cake :-(", error)
    finally:
        # Closing DB conn
        if (conn):
            cur.close()
            conn.close()
            print("Postgres connection has been closed")


cake_id = 2
deletecake(cake_id)
