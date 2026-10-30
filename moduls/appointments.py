from moduls.clients import *
from moduls.services import *

def add_appointments(con,client_id,service_id,appt_datetime,status):
    cur = con.cursor()

    cur.execute(
        """INSERT INTO appointments
               (client, service, dataandtime ,status)
           VALUES (%s, %s, %s, %s)""",
        (client_id, service_id, appt_datetime,status),
    )
    con.commit()

def delete_appointments(con,client_id,service_id,appt_datetime):
    cur = con.cursor()
    cur.execute(
        """DELETE FROM appointments WHERE client=%s AND service=%s AND dataandtime=%s""",
        (client_id, service_id, appt_datetime),
    )
    con.commit()

def writh_appointments(con):
    cur = con.cursor()
    cur.execute(
        """SELECT * FROM appointments"""
    )
    my_appointments = cur.fetchall()
    for x in my_appointments:
        print(x)

def appointments_by_name(con,client_id):
    cur = con.cursor()
    cur.execute( """SELECT * FROM appointments WHERE client=%s""",client_id)
    my_appointments = cur.fetchall()
    for x in my_appointments:
        print(x)

def appointments_by_date(con,appt_datetime):
    cur = con.cursor()
    cur.execute(
        """SELECT * FROM appointments WHERE dataandtime=%s""",appt_datetime
    )
    my_appointments = cur.fetchall()
    for x in my_appointments:
        print(x)