import psycopg2 as pg


# Работа с БД
def create_db():
    """
    Создает таблицу, если ее еще нет в БД
    """
    with pg.connect('dbname=netology_db user=netology_user password=user') as conn:
        with conn.cursor() as cur:
            cur.execute("""
            create table if not exists profile (
                id serial primary key,
                profile_id integer not null
            )
             """)
            print('База данных и таблицы созданы')


def pg_db_connect(option, users_list=None):
    """
    :param option: Режим вызова функции.
        insert - вставка значений в БД
        check - проверка наличия значенияв БД
    :param users_list: Список пользователей для проверки/вставки
    :return: возвращает список пользователей из БД
    """
    with pg.connect('dbname=netology_db user=netology_user password=user') as conn:
        if option == 'insert':
            with conn.cursor() as cur:
                for user in users_list:
                    cur.execute("""
                    insert into profile (profile_id) values (%s)
                    """, (user,))
        elif option == 'check':
            with conn.cursor() as cur:
                cur.execute("""
                select profile_id from profile;
                """)
                result = cur.fetchall()
            return result
