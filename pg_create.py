import psycopg2
try:
    conn = psycopg2.connect(user="postgres",
                            password="adiyat19",
                            host="localhost",
                            port="5432",
                            database="postgres")

    cur = conn.cursor()

    # tempat query
    create = '''
        CREATE TABLE cake_flavours (
                cake_id serial not null,
                cake_type varchar(30),
                tasty_meter varchar(30),
                primary key (cake_id)
                );
    '''

    cur.execute(create)

    conn.commit()
    print("Table was created successfully!")
except (Exception, psycopg2.Error) as error:
    print("Error encountered while creating Table :-(", error)
finally:
    if (conn):
        cur.close()
        conn.close()
        print("postgres connection has been closed!")
