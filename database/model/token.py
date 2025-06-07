from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from init import Initialize


# Модель таблицы users
class Token(Initialize.Initialize.get_base()):
    __tablename__ = "tokens"

    id = Column(Integer, Initialize.Initialize.get_sequence()
                , primary_key=True
                , server_default=Initialize.Initialize.get_sequence().next_value())
    user_id = Column(Integer, ForeignKey('users.id'))
    # Обратная связь с пользователем.
    user = relationship('User', back_populates='tokens')
    bank_id = Column(Integer, ForeignKey('banks.id'))
    # Обратная связь с банком.
    bank = relationship('Bank', back_populates='tokens')
    token = Column(String, nullable=False)
    refresh_token = Column(String, nullable=False)




    def __repr__(self):
        return f"Token(id={self.id}, user_id={self.user_id}, bank_id={self.bank_id}, token='{self.token}', refresh_token='{self.refresh_token}')"

    def __init__(self, user_id, bank_id, token, refresh_token):
        self.user_id = user_id
        self.bank_id = bank_id
        self.token = token
        self.refresh_token = refresh_token