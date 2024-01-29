import sqlite3
data = [
    (5, 'Rust',899),
    (6, 'Angular',1899),
    (7, 'JS',99),
]
try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    # sql_connection = sqlite3.connect(':memory:')
    cursor = sql_connection.cursor()
    print("Baza danych xostaal podlonczona")

    insert = '''
    INSERT INTO software (id, name, price) VALUES (?,?,?);
    '''

    # cursor.execute(insert, (4,'Scala',5600))
    # sql_connection.commit()

    cursor.executemany(insert,data)
    sql_connection.commit()

except sqlite.Error as e:
    print("Blad bazy danych",e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zamknieta")