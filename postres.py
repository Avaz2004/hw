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
        cur.execute("""
        INSERT INTO clinets_db(first_name, last_name, email) VALUES(first_name, last_name, email);
        """)

def add_phone(conn, client_id, phone):
    with conn.cursor as cur:
        cur.execute("""
        INSERT INTO phonenumbers(client_id, client_phonenumber) VALUES(client_id, phone);
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
    first_name_for_finding = input("Для поиска клиента,пожалуйста,введите его имя(Если не знаете то нажмите enter): ")
    last_name_for_finding = input("Для поиска клиента,пожалуйста,введите его фамилию(Если не знаете то нажмите enter): ")
    email_for_finding = input("Для поиска клиента,пожалуйста,введите его почту(Если не знаете то нажмите enter): ")
    phonenumber_for_finding = input("Для поиска клиента,пожалуйста,введите его телефон(Если не знаете то нажмите enter): ")

    with conn.cursor() as cur:
        if first_name_for_finding == "" and last_name_for_finding == "" and email_for_finding == "" and phonenumber_for_finding == "":
            print("Недостаточно информации для поиска клиента")
        else:
            cur.execute("""
            SELECT *
            FROM client_db AS ch5
            WHERE first_name = first_name_for_finding OR last_name = last_name_for_finding OR email = email_for_finding OR phonenumber = phonenumber_for_finding
            """)
        print(cur.fetchall())


if __name__ == "__main__":
    with psycopg2.connect(database="clients_db", user="postgres", password="postgres") as conn:
        with conn.cursor() as cur:
            create_db(cur)
            add_client(cur, "Richie", "Blackmore", "Deep_purple@gmail.com")
            add_client(cur, "James", "Dio", "DIO@gmail.com")
            add_client(cur, "Ozzy", "Ozbourne", "Black_sabbath@gmail.com")
            add_client(cur, "Kirk", "Hammett", "Metallica@gmail+.com")
            add_client(cur, "Freddy", "Mercury", "Queen@gmail.com")
            add_phone(cur, 1, "11111111")
            add_phone(cur, 2, "222222222")
            add_phone(cur, 3, "3333333333")
            add_phone(cur, 4, "44444444444")
            add_phone(cur, 5, "555555555555")
            change_client()
            delete_phone()
            delete_client()
            find_client()


conn.close()