from init import initialize
from model.token import Token

session = initialize.Initialize.get_session()

# Добавление нового токена
def insert_token(user, bank, token, refresh_token):
    new_token = Token(user.id, bank.id, token, refresh_token)
    session.add(new_token)
    session.commit()
    return new_token

# Получение токена по id пользователя
def get_token_by_user_id(user_id):
    return session.query(Token).filter(Token.user_id == user_id).first()

# Получение всех токенов
def get_all_tokens():
    return session.query(Token).all()

# Получение токена по его id
def get_token_by_id(id):
    return session.query(Token).filter(Token.id == id).first()