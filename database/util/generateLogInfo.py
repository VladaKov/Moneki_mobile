

# Метод генерирующий сообщение об ошибке
def generate_log_message(service_name, method, params, find_by, exp):
    return get_message(service_name, get_method_message(method), params, find_by) + " " + str(exp)

# Метод генерирует сообщение с информацией о сервисе, методе и параметрах
def get_message(service_name, method_message, params, find_by):
    if params is not None:
        return "Ошибка " + method_message + service_name + " " + str(params) + " = " + find_by
    else:
        return "Ошибка " + method_message + service_name

# Метод генерирует информацию о методе
def get_method_message(method):
    if method == "insert":
        return "добавления нового "
    elif method == "update":
        return "обновления "
    elif method == "delete":
        return "удаления "
    elif method == "select":
        return "поиска "
