def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    first_name_for_finding = input("Для поиска клиента,пожалуйста,введите его имя(Если не знаете то нажмите enter): ")
    last_name_for_finding = input("Для поиска клиента,пожалуйста,введите его фамилию(Если не знаете то нажмите enter): ")
    email_for_finding = input("Для поиска клиента,пожалуйста,введите его почту(Если не знаете то нажмите enter): ")
    phonenumber_for_finding = input("Для поиска клиента,пожалуйста,введите его телефон(Если не знаете то нажмите enter): ")


    while True:
        with conn.cursor() as cur:
            if first_name_for_finding == "" and last_name_for_finding == "" and email_for_finding == "" and phonenumber_for_finding == "":
                print("Недостаточно информации для поиска клиента")
                break
            else:
                cur.execute("""
                SELECT *
                FROM client_db AS ch5
                WHERE first_name = first_name_for_finding OR last_name = last_name_for_finding OR email = email_for_finding OR phonenumber = phonenumber_for_finding
                """)
                print(cur.fetchall())