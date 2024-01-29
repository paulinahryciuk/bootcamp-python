import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    # sql_connection = sqlite3.connect(':memory:')
    cursor = sql_connection.cursor()
    print("Baza danych xostaal podlonczona")


    delete = '''
    DELETE FROM software WHERE id = 1;
    '''

    # cursor.execute(delete)
    # sql_connection.commit()

    update = '''
    UPDATE software SET price=200 WHERE id = 7;'''

    cursor.execute(update)
    sql_connection.commit()


except sqlite3.Error as e:
    print("Blad bazy danych",e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zamknieta")