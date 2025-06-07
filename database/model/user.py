from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from init import initialize


# Модель таблицы users
class User(initialize.Initialize.get_base()):
    __tablename__ = "users"

    id = Column(Integer, initialize.Initialize.get_sequence()
                , primary_key=True
                , server_default=initialize.Initialize.get_sequence().next_value())
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    mail = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    telephon_number = Column(String, nullable=False)


    # Отношение к таблице tokens
    tokens = relationship('Token', back_populates='user')

    def __repr__(self):
        return f"User(id={self.id}, login='{self.login}', password='{self.password}', first_name='{self.first_name}', mail='{self.mail}', surname='{self.surname}', telephon_number'{self.telephon_number}')"

    def __init__(self, login, password, first_name, mail, surname, telephon_number):
        self.login = login
        self.password = password
        self.first_name = first_name
        self.mail = mail
        self.surname = surname
        self.telephon_number = telephon_number
