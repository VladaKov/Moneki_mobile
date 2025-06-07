from init import initialize
from model.bank import Bank

session = initialize.Initialize.get_session()

# Добавление нового токена
def insert_bank(bank_name, bic):
    new_bank = Bank(bank_name, bic)
    session.add(new_bank)
    session.commit()
    return new_bank

# Поиск банка по названию
def get_bank_by_name(bank_name):
    return session.query(Bank).filter(Bank.bank_name == bank_name).first()

# Поиск банка по БИК
def get_bank_by_bic(bic):
    return session.query(Bank).filter(Bank.bic == bic).first()

# Поиск банка по id
def get_bank_by_id(id):
    return session.query(Bank).filter(Bank.id == id).first()

# Поиск всех банков
def get_all_banks():
    return session.query(Bank).all()

