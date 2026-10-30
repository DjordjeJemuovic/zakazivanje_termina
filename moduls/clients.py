from moduls.temp_data import *
from moduls.db import connection
import pymysql
import re

def inesrt_clients (con):
    klijenti = [
        (fake_client_name(), fake_client_last_name(), fake_phone_number())
        for _ in range(10)
    ]
    cur = con.cursor()
    cur.executemany(
        "INSERT INTO clients (first_name, last_name, phone) VALUES (%s, %s, %s)",
        klijenti,
    )
    con.commit()

def add_clients (con,name,last_name,phone_number):
    cur = con.cursor()
    cur.execute("INSERT INTO clients (first_name, last_name, phone) VALUES (%s, %s, %s)",(name,last_name,phone_number))
    con.commit()

def show_clients (con):
    cur = con.cursor()
    cur.execute("SELECT * FROM clients")
    con.commit()
    cliens = cur.fetchall()
    for client in cliens:
        print(client)

def find_client_by_first_name(con, name):
    cur = con.cursor()
    cur.execute("SELECT * FROM clients WHERE first_name = %s", (name,))
    return cur.fetchall()

def validation_for_phone(number):
    pattern = r"^\d{3}/\d{3}-\d{3}$"

    if re.fullmatch(pattern, number):
        return True
    return False