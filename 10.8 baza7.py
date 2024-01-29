import sqlite3

try:
    sql_connection = sqlite3.connect('test.db')
    sql_connection.row_factory= sqlite3.Row
    cursor = sql_connection.cursor()
    print("Baza danych xostaal podlonczona")
    table_data = 'users'


    select = f'''SELECT * FROM {table_data};'''

    # table = ('users',)
    cursor.execute(select)
    rows = cursor.fetchall()
    for row in rows:
        print(dict(row))

except sqlite3.Error as e:
    print("Blad bazy danych",e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zamknieta")
