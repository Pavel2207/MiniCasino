import sqlite3

a=sqlite3.connect('server.db') # создаем и даем название базе данних

sql=a.cursor()    #  курсор необходим для работи с базой данних

# создаем таблицу
sql.execute( '''CREATE TABLE IF NOT EXISTS users(
                    login TEXT,
                    password TEXT,
                    cash BIGINT
                    )''' )

a.commit()   #  подтверждаем создание таблици

# просим пользователя ввести логин и пароль
users_login=input('Login:')
users_password=input('Password:')

sql.execute(f'SELECT login FROM users WHERE login={users_login}') # проверяем таблицу

if sql.fetchone() is None:
    # если введеной записи нет в таблици
    sql.execute(f'INSERT INTO users VALUES (?,?,?)',(users_login , users_password ,0)) # записиваем даннние в таблицу

    a.commit() # подтверждаем запись в таблицу
    print('Зарегистрировано !')

else:
    print('Такая запись уже имеется !')

    # виводим данние таблици через цикл
    for i in sql.execute('SELECT * FROM users'):
        print(i)