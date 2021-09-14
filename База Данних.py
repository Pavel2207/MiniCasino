import sqlite3
from random import randint



a=sqlite3.connect('server.db') # создаем и даем название базе данних

sql=a.cursor()    #  курсор необходим для работи с базой данних

# создаем таблицу
sql.execute( '''CREATE TABLE IF NOT EXISTS users(
                    login TEXT,
                    password TEXT,
                    cash BIGINT
                    )''' )

a.commit()   #  подтверждаем создание таблици



# создаем функцию которая регистрирует пользователя в базе данних
def reg():
    users_login = input('Login:')
    users_password = input('Password:')

    sql.execute(f'SELECT login FROM users WHERE login="{users_login}"') # проверяем таблицу

    if sql.fetchone() is None:
        # если введеной записи нет в таблици
        sql.execute(f'INSERT INTO users VALUES (?,?,?)',(users_login , users_password ,0)) # записиваем даннние в таблицу

        a.commit() # подтверждаем запись в таблицу
        print('Зарегистрировано !')

    else:
        print('Такая запись уже имеется !')



def casino():
    users_login = input('Login:')
    users_password = input('Password:')
    x=randint(1,2)

    for i in sql.execute(f'SELECT cash FROM users WHERE login="{users_login}"'): # переменная что би плюсовать результат
        profit=i[0]

    sql.execute(f'SELECT login FROM users WHERE login="{users_login}"')

    if sql.fetchone() is None:
        print('Такого логина не существует . Зарегистрируйтесь ! ')
        reg()
    else:
        if x==1:
            sql.execute(f'UPDATE users SET cash={1000+profit} WHERE login="{users_login}" ' )
            a.commit()
            print('Ви виграли 1000!')
            for i in sql.execute(f'SELECT login, cash FROM users WHERE login="{users_login}" '):
                print(i)


        else:
            print('Ви ничего не виграли. Ваш акаунт будет удален.')
            sql.execute(f'DELETE FROM users WHERE login="{users_login}"')
            a.commit()




casino()
