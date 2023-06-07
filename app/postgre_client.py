import psycopg2
from datetime import datetime, timezone
import logging


def notifications(cur, notificationId):
    print('---------- Querying notifications- -----')

    notification_qry = f"""SELECT * from  notification where id={notificationId}"""

    cur.execute(notification_qry)

    rows = cur.fetchall()
    for row in rows:
        print(f"{row[0]}, {row[1]}")

    print('Updating notification')
    numAttendees = 3
    update_sql = "UPDATE notification SET status = %s, completed_date=%s  WHERE id = %s"
    cur.execute(update_sql, (f'Notified {numAttendees} attendees', datetime.now(timezone.utc), notificationId))


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
        conn.autocommit = True
    except Exception as e:
        print (f"I am unable to connect to the database:{str(e)}")

    cur = conn.cursor()
    notifications(cur, 8)
    attendees(cur)

if __name__ == "__main__":
   main()