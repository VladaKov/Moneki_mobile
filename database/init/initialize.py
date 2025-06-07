from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Sequence

class Initialize:
    # Скрываемые атрибуты: _base, _engine, _Session, _Sequence
    _base = declarative_base()  # Создаем декларативную базу (Base)
    _engine = create_engine("postgresql+psycopg2://postgres:wermut00@localhost:5432/test_db", echo=True)
    _Session = sessionmaker(bind=_engine)
    _Sequence = Sequence("main_sequence")

    @classmethod
    def get_base(cls):
        """
        Метод для получения декларативной базы SQLAlchemy
        """
        return cls._base

    @classmethod
    def get_session(cls):
        """
        Метод для получения сессии SQLAlchemy. Убедитесь, что initialize_database
        был вызван до этого.
        """
        if cls._Session is None:
            raise Exception("Database is not initialized. Call 'initialize_database' first.")
        return cls._Session()

    @classmethod
    def get_sequence(cls):
        """
        Метод для создания последовательности идентификаторов в базе данных
        """
        return cls._Sequence
