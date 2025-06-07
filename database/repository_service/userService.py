from init import initialize
from model.user import User
from util.generateLogInfo import generate_log_message, get_message, get_method_message


session = initialize.Initialize.get_session()

# Добавление нового пользователя
def insert_user(login, password, first_name, surname, mail, telephon_number):
    new_user = User(login, password, first_name, surname, mail, telephon_number)
    session.add(new_user)
    session.commit()
    return new_user


# Изменение пользователя
def update_user(modify_user):
    for field, value in get_dict_for_update(modify_user).items():
        if hasattr(modify_user, field):  # Проверяем, существует ли это поле в модели User
            setattr(modify_user, field, value)
    session.commit()
    return get_user_by_id(modify_user.id)


# Получение пользователя по его логину
def get_user_by_login(login):
    user = session.query(User).filter(User.login == login).one()
    return user

# Получение пользователя по его имени
def get_user_by_name(first_name):
    user = session.query(User).filter(User.first_name == first_name).one()
    return user


# Получение всех пользователей
def get_all_users():
    users = session.query(User).all()
    return users

# Получение пользователя по его id
def get_user_by_id(id):
    user = session.query(User).filter(User.id == id).one()
    return user


# Удаление пользователя
def delete_user(user):
    session.delete(user)
    session.commit()
    return True


# Создадим словарь с обновленной информацией по пользователю
def get_dict_for_update(modify_user):
    user_dict = dict()
    user_dict["login"] = modify_user.login
    user_dict["password"] = modify_user.password
    user_dict["first_name"] = modify_user.first_name
    user_dict["surname"] = modify_user.surname
    user_dict["mail"] = modify_user.mail
    user_dict["telephon_number"] = modify_user.telephon_number
    return user_dict