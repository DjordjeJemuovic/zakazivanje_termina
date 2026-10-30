from random import choice
from moduls.clients import add_clients, show_clients, find_client_by_first_name, validation_for_phone
from moduls.appointments import add_appointments, delete_appointments, writh_appointments, appointments_by_name, \
    appointments_by_date
from moduls.db import connection
from datetime import datetime


from moduls.services import show_services

options = {
    1:"Dodaj klijenta",
    2:"Lista klijenata",
    3:"Zakazi termin",
    4:"Otkazi termin",
    5:"Raspored za dan",
    6:"Termini jednog klijenta",
    7:"Izlaz"
}

start_work = 9 #radno vreme pocinje u 9h
end_work = 17 # kraj radnog vremena je 17h
while choice!=7:
    print(options)
    choice = int(input("Izaberite jednu od ponudjenih opcija:"))
    if choice==1:
        name = input("Unesite ime klijenta:")
        last_name = input("Unesite prezime klijenta:")
        phone = input("Unesite broj telefona klijenta:")
        if validation_for_phone(phone):
            matches = find_client_by_first_name(connection, name)
            if matches:
                print("Klijent vec postoji u bazi")
            else:
                add_clients(connection, name, last_name, phone)
                print("Uspesno ste uneli novog lijenta!")
        else:
            print("Broj telefona nije ispravno unet, mora biti u formatu 000/000-000.")

    if choice==2:
        show_clients(connection)
    if choice==3:
        show_clients(connection)
        client_id = int(input("Unesite ID klijenta za kod zakazujete termin:"))
        show_services(connection)
        service_id = int(input("Unesite ID usluge koja se zakazuje"))
        datum = input("Datum (GGGG-MM-DD): ")
        vreme = input("Vreme (HH:MM): ")
        dt = datetime.strptime(f"{datum} {vreme}", "%Y-%m-%d %H:%M")
        if dt.hour < start_work or dt.hour > end_work:
            print("Nase radno vreme je od 9 do 17 casova. Molimo zakazite svoj termin u tom vremenu")
        else:
            new_id = add_appointments(connection, client_id, service_id, dt,"added")
    if choice==4:
        print("-----Ovo su zakazani terminu------")
        writh_appointments(connection)

        client_id = int(input("Unesite ID klijenta kog zelis da obrisemo:"))
        service_id = int(input("Unesi ID usluge koju je koristio:"))
        datum = input("Datum (GGGG-MM-DD): ")
        vreme = input("Vreme (HH:MM): ")
        dt = datetime.strptime(f"{datum} {vreme}", "%Y-%m-%d %H:%M")
        delete_appointments(connection, client_id, service_id,dt)
    if choice==5:
        print("Zakazi terminu")
        writh_appointments(connection)
        datum = input("Datum (GGGG-MM-DD): ")
        vreme = input("Vreme (HH:MM): ")
        dt = datetime.strptime(f"{datum} {vreme}", "%Y-%m-%d %H:%M")
        appointments = appointments_by_date(connection, dt)
    if choice==6:
        print("Zakazane usluge")
        writh_appointments(connection)
        client_id = int(input("Unesite ID korinika za kog zelite da vidite sve termine"))
        appointments_by_name(connection, client_id)
    else:
        print("Molimo vas izaberite jednu od ponudjenih opcija")
