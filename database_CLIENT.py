import sqlite3 as sql


def DataBase_c():
    with sql.connect('test.db') as conn:
        cursor = conn.cursor()

        sql_data = cursor.execute('SELECT city FROM test_table').fetchall()

        lst = list()

        for iteam in sql_data:
            for key in iteam:
                lst.append(key)
        
        return lst
          