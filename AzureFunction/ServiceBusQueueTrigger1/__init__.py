import logging

import azure.functions as func
import os
import psycopg2
from datetime import datetime, timezone


def _get_db_connection():
    try:
        dbconn = os.environ['PostgreConnection']
        logging.info(f'Connecting to :{dbconn}')
        
        conn = psycopg2.connect("dbname='techconfdb' user='azureadmin@techconfdbserver' host='techconfdbserver.postgres.database.azure.com' password='M15tr0n1;'")
        logging.info('Successfully connected to db ')
        conn.autocommit = True
        cur = conn.cursor()
        return cur
    except Exception as e:
        raise Exception (f"I am unable to connect to the database:{str(e)}")

def _get_attendees(cur):
    logging.info('Querying attendees..')
    
    attendee_qry = "SELECT first_name, email from attendee"
    cur.execute(attendee_qry)
    rows = cur.fetchall()
    return [(row[0], row[1]) for row in rows]
    
def _update_notification(cur, notificationId, numAttendees):
    update_sql = "UPDATE notification SET status = %s, completed_date=%s  WHERE id = %s"
    cur.execute(update_sql, (f'Notified {numAttendees} attendees', datetime.now(timezone.utc), notificationId))


def _do_work(notification_id: int):
    cursor = _get_db_connection()
    attendees = _get_attendees(cursor)
    _update_notification(cursor, notification_id, len(attendees))
    logging.info(f'Notification table successfully updated for id@{notification_id} with {len(attendees)}')
    
    

def main(msg: func.ServiceBusMessage):
    logging.info(f"Python ServiceBus queue trigger processed message: {msg.get_body().decode('utf-8')}")
    notification_id = msg.get_body().decode('utf-8')
    logging.info(f'Obtained notification {notification_id} from message')
    print(f'Obtained notification {notification_id} from message')
    try:
        logging.info(f"sendiGRID API key should be:{os.environ['SendGridKey']}")
    except Exception as e:
        logging.info(f'Could not get sendgridkey:{e}')
    try:
        logging.info(f"POSTGRECONNECTION should be:{os.environ['PostgreConnection']}")
    except Exception as e:
        logging.info(f'Could not get Postgre:{e}')
    _do_work(int(notification_id))
        