import psycopg2 as pg


def insert_to_db(*args):
    conn = pg.connect('dbname=netology_db user=drg password=DrGmac23')
    cur = conn.cursor()
    cur.execute(('INSERT INTO users (id_user_vk, id_photo_vk, likes) VALUES (%s, %s, %s)'), args)
    conn.commit()
    conn.close()


def create_db():  # создает таблицы
    conn = pg.connect('dbname=netology_db user=drg password=DrGmac23')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Users ('
                'id_user_vk INT NOT NULL,'
                'id_photo_vk INT NOT NULL DEFAULT 0,'
                'likes INT NOT NULL DEFAULT 0);')
    conn.commit()
    pass


if __name__ == '__main__':
    create_db()