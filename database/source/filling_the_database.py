from flet import *
from database.repository_service import userService
from pages.registration import RegistrationData


registration = RegistrationData()

all_data = registration.data


login = registration.data["login"]
name = registration.data["first_name"]
email = registration.data["email"]

def add_User():
    # user1 = userService.insert_user( {registration.data["login"]}
    #                                 , {registration.data["first_name"]}
    #                                 , {registration.data["surname"]}
    #                                 , {registration.data["email"]}
    #                                 , {registration.data["telephone"]}),
    print(login)
