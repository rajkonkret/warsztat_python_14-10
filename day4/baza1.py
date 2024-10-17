import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_db.db')
    cursor = sql_connection.cursor()
    print("Baza danych zostałą podłączona")
except sqlite3.Error as e:
    print("Bład podłaczenia bazy danych")
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamknięta")
