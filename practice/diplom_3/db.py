import psycopg2
import json
from pprint import pprint


def connect_database(dbname='netology_db', user='drg', password='DrGmac23'):
    conn = psycopg2.connect(f"dbname={dbname} user={user} password={password}")
    cur = conn.cursor()
    return cur, conn, dbname


def create_table(cur, conn):
    command = (
        """
        CREATE TABLE if not exists Person (
                id integer PRIMARY KEY NOT NULL,
                photos jsonb,
                chosen boolean default False,
                blacklist boolean default False
                );
        """
    )
    cur.execute(command)
    conn.commit()


def drop_table(cur, conn):
    cur.execute("drop Table Person")
    conn.commit()
    print("Table was dropped!")


def add_photos(person_key, person_value, cur, conn):
    cur.execute('select id from Person p where p.id = %s', (person_key, ))
    exist_person = cur.fetchall()
    if exist_person:
        print(f'Person with id {person_key} is already exist in Table Person!')
    else:
        cur.execute('insert into Person (id, photos) values (%s, %s)',
                    (person_key, json.dumps(person_value)))
        conn.commit()
        print(f'Person with id {person_key} was created in Table Person!')


def get_photos(person_key, cur):
    cur.execute('select photos from Person p where p.id = %s', (person_key, ))
    exist_person = cur.fetchall()
    if exist_person:
        return exist_person
    else:
        print(f'Person with id {person_key} is not exist in Table Person!')


def get_all_photos(cur):
    cur.execute('select photos from Person')
    pprint(cur.fetchall())


def get_all_persons(cur):
    cur.execute('select * from Person')
    pprint(cur.fetchall())


def get_person_by_id(person_key, cur):
    cur.execute('select id from Person p where p.id = %s', (person_key, ))
    exist_person = cur.fetchall()
    if exist_person:
        return True
    else:
        print(f'Person with id {person_key} is not exist in Table Person!')


def get_all_ids(cur):
    cur.execute('select id from Person p where p.blacklist = False')
    return cur.fetchall()


def make_id_chosen(person_key, cur, conn):
    cur.execute('update Person set chosen = True where id = %s', (person_key, ))
    conn.commit()


def put_id_to_blacklist(person_key, cur, conn):
    cur.execute('update Person set blacklist = True where id = %s', (person_key, ))
    conn.commit()


def del_all_photos(cur, conn):
    cur.execute('DELETE FROM Person')
    conn.commit()
    print(f'We have deleted all persons with photos from database!')


if __name__ == '__main__':
    pass


