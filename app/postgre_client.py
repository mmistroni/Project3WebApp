import psycopg2

import logging

print('Running')
try:
    conn = psycopg2.connect("dbname='techconfdb' user='azureadmin@techconfdbserver' host='techconfdbserver.postgres.database.azure.com' password='M15tr0n1;'")
    print('Successfully connected to db ')
except Exception as e:
    print (f"I am unable to connect to the database:{str(e)}")

cur = conn.cursor()
cur.execute("""SELECT * from  notification""")

rows = cur.fetchall()
for row in rows:
    print(f"{row[0]}, {row[1]}")
