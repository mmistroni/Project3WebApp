import psycopg2

import logging


def notifications(cur):
    print('---------- Querying notifications- -----')

    notification_qry = """SELECT * from  notification"""

    cur.execute(notification_qry)

    rows = cur.fetchall()
    for row in rows:
        print(f"{row[0]}, {row[1]}")


def attendees(cur):
    print('----- Querying attendees ----')
    attendee_qry = "SELECT first_name, email from attendee"
    cur.execute(attendee_qry)

    rows = cur.fetchall()
    for row in rows:
        print(f"{row[0]}, {row[1]}")


def main():
    print('Running')
    try:
        conn = psycopg2.connect("dbname='techconfdb' user='azureadmin@techconfdbserver' host='techconfdbserver.postgres.database.azure.com' password='M15tr0n1;'")
        print('Successfully connected to db ')
    except Exception as e:
        print (f"I am unable to connect to the database:{str(e)}")

    cur = conn.cursor()
    notifications(cur)
    attendees(cur)

if __name__ == "__main__":
   main()