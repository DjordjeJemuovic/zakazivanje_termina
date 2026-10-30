from moduls.temp_data import *
from moduls.db import connection
import pymysql

def insert_sevices (con):
    usluge = [
        (fake_company_name(), fake_price(), fake_duration())
        for _ in range(5)
    ]
    cur = con.cursor()
    cur.executemany(
        "INSERT INTO services (name, price, duration) VALUES (%s, %s, %s)",
        usluge
    )
    con.commit()

def show_services (con):
    cur = con.cursor()
    cur.execute("SELECT * FROM services")
    services = cur.fetchall()
    for service in services:
        print(service)

