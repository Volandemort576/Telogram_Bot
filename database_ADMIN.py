import sqlite3 as sql


def DataBase_a(get_password, what, data=None, id=None):
    password = '9090039885qwerty_'

    if get_password == password:
        with sql.connect('test.db') as conn:
            cursor = conn.cursor()

            sql_data = cursor.execute('SELECT * FROM test_table').fetchall()

            s = str()

            if what == 1:
                for key, val in sql_data:
                    s += f'{key}. {val}\n\r'
                s.strip()
                return f'id|city\n\r{s}'
            
            sql_data_exam = cursor.execute('SELECT city FROM test_table').fetchall()
    
            if what == 2:
                data = (data,)
                if data not in sql_data_exam:
                    cursor.execute('INSERT INTO test_table (city) VALUES (?)', data)
                    return 'Успех'
                else:
                    return 'Город уже существует'
            if what == 3:
                id = (id,)
                try:
                    cursor.execute('DELETE FROM test_table WHERE id=?', id)
                    return 'Всё ок!'
                except:
                    return 'Что-то пошло не так!'
    else:
        return 'неверный пароль'  
