import sqlite3

try:
    # sql_connection = sqlite3.connect('sqlite_python.db')
    sql_connection = sqlite3.connect(':memory:')
    cursor = sql_connection.cursor()
    print("Baza danych xostaal podlonczona")

except sqlite.Error as e:
    print("Blad bazy danych",e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zamknieta")

