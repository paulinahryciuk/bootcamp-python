import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    # sql_connection = sqlite3.connect(':memory:')
    cursor = sql_connection.cursor()
    print("Baza danych xostaal podlonczona")

    query = '''
    CREATE TABLE SqliteDB_developers(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL
    );'''

    # cursor.execute(query)
    # sql_connection.commit()


    with open('tables.sql','r') as file:
        sql_script = file.read()

    cursor.executescript(sql_script)
    
except sqlite3.Error as e:
    print("Blad bazy danych",e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zamknieta")


