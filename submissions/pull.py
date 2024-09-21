import psycopg2


conn = psycopg2.connect(host="localhost",dbname="postgres", user="postgres",password="1234")
cur = conn.cursor()

cur.execute(
                "select * from candidates where id = '6e53dd4e-3e2b-43ce-85b2-c84bce12f62b'"
            ) 

list = cur.fetchall()
print(list)