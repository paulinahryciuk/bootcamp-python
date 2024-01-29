import sqlite3

lista= []
try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    sql_connection.row_factory = sqlite3.Row
    cursor = sql_connection.cursor()
    print("Baza danych xostaal podlonczona")


    select = '''
        SELECT * FROM software;
        '''

    select = '''
    SELECT * FROM software;
    '''

    # for row in cursor.execute(select):
    #     print(row)
    #     lista.append(dict(row))
    #
    # print(lista)

    cursor .execute(select)
    rows = cursor.fetchall()
    for row in rows:
        print(dict(row))

    # cursor.execute(insert)
    # sql_connection.commit()

except sqlite3.Error as e:
    print("Blad bazy danych",e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zamknieta")