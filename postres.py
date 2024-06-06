import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS clients_db(
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(40) NOT NULL,
        last_name VARCHAR(40) NOT NULL,
        email VARCHAR(40) NOT NULL)
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS phonenumbers(
        id_phonenumber SERIAL PRIMARY KEY,
        client_id INTEGER NOT NULL REFERENCES clients_db(id),
        client_phonenumber VARCHAR(20) UNIQUE);
        """)
   

def add_client(conn, first_name, last_name, email, phones=None):
    with conn.cursor as cur:
        fs = input("Введите свое имя: ")
        ls = input("Введите свою фамилию: ")
        e = input("Введите свою почту: ")
        cur.execute("""
        INSERT INTO clinets_db(first_name, last_name, email) VALUES(fs, ls, e);
        """)

def add_phone(conn, client_id, phone):
    with conn.cursor as cur:
        ci = input("Введите id клиента: ")
        cp = input("Введите номер телефона клиента: ")
        cur.execute("""
        INSERT INTO phonenumbers(client_id, client_phonenumber) VALUES(ci, cp);
        """)

def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    print("first_name - изменить имя, last_name - изменить фамилию, email - изменить почту, phone - изменить номер телефона , stop - закончить изменение")
    command = input("Введите команду: ")
    while True:
        if command == first_name:
            id_for_change_first_name = input("Введите id клиента,чье имя будет изменено: ")
            new_first_name = input("Введите новое имя клиента: ")
            with conn.cursor as cur:
                cur.execute("""
                UPDATE clients_db SET first_name = new_first_name WHERE id = id_for_change_first_name;
                """)
        elif command == last_name:
            id_for_change_last_name = input("Введите id клиента,чья фамилия будет изменена: ")
            new_last_name = input("Введите новою фамилию клиента: ")
            with conn.cursor as cur:
                cur.execute("""
                UPDATE clients_db SET last_name = new_last_name WHERE id = id_for_change_last_name;
                """)
        elif command == email:
            id_for_change_email = input("Введите id клиента,чья почта будет изменена: ")
            new_email = input("Введите новую почту клиента: ")
            with conn.cursor as cur:
                cur.execute("""
                UPDATE clients_db SET email = new_email WHERE id = id_for_change_email;
                """)
        elif command == phone:
            id_for_change_phone = input("Введите id клиента,чей номер телефона будет изменен: ")
            new_phone = input("Введите новый номер телефона клиента: ")
            with conn.cursor as cur:
                cur.execute("""
                UPDATE phonenumbers SET client_phonenumber = new_phone WHERE client_id = id_for_change_phone;
                """)
        elif command == stop:
            break
        else:
            print("Неизвестная команда")

def delete_phone(conn, client_id, phone):
    id_for_deleting_phonenumber = input("Введите id клиента,чей номер телефона будет удален: ")
    phonenumber_for_deleting = input("Введите номер телефона который хотите удалить: ")
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM phonenumbers WHERE client_id = id_for_deleting_phonenumber AND client_phonenumber = phonenumber_for_deleting;
        """)

def delete_client(conn, client_id):
    id_for_deleting_client = input("Введите id клиента которого хотите удалить: ")
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM phonenumbers WHERE client_id = id_for_deleting_client
        """)
        cur.execute("""
        DELETE FROM clients_db WHERE id = id_for_deleting_client
        """)

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    print("Для поиска информации о клиенте, пожалуйста, введите команду, где:\n "
          "1 - найти по имени; 2 - найти по фамилии; 3 - найти по e-mail; 4 - найти по номеру телефона")
    while True:
        with conn.cursor() as cur:
            input_command_for_finding = int(input("Введите команду для поиска информации о клиенте: "))
            if input_command_for_finding == 1:
                input_name_for_finding = input("Введите имя для поиска информации о клиенте: ")
                cur.execute("""
                SELECT id, client_name, client_surname, client_email, client_phonenumber
                FROM clients_Homework5 AS ch5
                LEFT JOIN client_phonenumbers AS cp ON cp.id_phonenumber = ch5.id
                WHERE client_name=%s
                """)
                print(cur.fetchall())
                break
            elif input_command_for_finding == 2:
                input_surname_for_finding = input("Введите фамилию для поиска информации о клиенте: ")
                cur.execute("""
                SELECT id, client_name, client_surname, client_email, client_phonenumber
                FROM clients_Homework5 AS ch5
                LEFT JOIN client_phonenumbers AS cp ON cp.id_phonenumber = ch5.id
                WHERE client_surname=%s
                """)
                print(cur.fetchall())
                break
            elif input_command_for_finding == 3:
                input_email_for_finding = input("Введите email для поиска информации о клиенте: ")
                cur.execute("""
                SELECT id, client_name, client_surname, client_email, client_phonenumber
                FROM clients_Homework5 AS ch5
                LEFT JOIN client_phonenumbers AS cp ON cp.id_phonenumber = ch5.id
                WHERE client_email=%s
                """)
                print(cur.fetchall())
                break
            elif input_command_for_finding == 4:
                input_phonenumber_for_finding = input("Введите номер телефона для поиска информации о клиенте: ")
                cur.execute("""
                SELECT id, client_name, client_surname, client_email, client_phonenumber
                FROM clients_Homework5 AS ch5
                LEFT JOIN client_phonenumbers AS cp ON cp.id_phonenumber = ch5.id
                WHERE client_phonenumber=%s
                """)
                print(cur.fetchall())
                break
            else:
                print("К сожалению, Вы ввели неправильную команду, пожалуйста, повторите ввод")


with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
    pass  # вызывайте функции здесь

conn.close()