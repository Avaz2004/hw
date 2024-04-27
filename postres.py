import psycopg2
conn = psycopg2.connect(database="netology_db",user="postgres",password="1q2w3e4r ")
with cur.cursor() as cur:
    cur.execute("CREATE TABLE test (id SERIAL PRIMARY KEY);")
    conn.commit()
conn.close()