import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    # sql_connection = sqlite3.connect(':memory:')
    cursor = sql_connection.cursor()
    print("Baza danych xostaal podlonczona")


    insert = '''
    INSERT INTO software (id,name,price) VALUES(1,'Python',100);
    '''
    select = '''
    SELECT * FROM software;
    '''

    for row in cursor.execute(select):
        print(row)

    # cursor.execute(insert)
    # sql_connection.commit()

except sqlite3.Error as e:
    print("Blad bazy danych",e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zamknieta")