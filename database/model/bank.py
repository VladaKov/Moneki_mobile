from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from init import initialize


# Модель таблицы banks
class Bank(initialize.Initialize.get_base()):
    __tablename__ = "banks"

    id = Column(Integer, initialize.Initialize.get_sequence()
                , primary_key=True
                , server_default=initialize.Initialize.get_sequence().next_value())
    bank_name = Column(String, nullable=False)
    bic = Column(String, nullable=False)

    # Обратная связь с пользователем.
    tokens = relationship("Token", back_populates="bank")

    def __repr__(self):
        return f"Bank(id={self.id}, bank_name='{self.bank_name}', bic='{self.bic}')"

    def __init__(self, bank_name, bic):
        self.bank_name = bank_name
        self.bic = bic