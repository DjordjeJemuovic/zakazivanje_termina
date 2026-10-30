from faker import Faker
faker = Faker()


#fake data for clients first name, last name and phone number
def fake_client_name():
    return faker.first_name()
def fake_client_last_name():
    return faker.last_name()
def fake_phone_number():
    return faker.phone_number()



#fake data for servces
def fake_company_name():
    return faker.company()

def fake_price():
    return faker.random_int(min=100, max=5000)
def fake_duration():
    return faker.random_int(min=15, max=100)

