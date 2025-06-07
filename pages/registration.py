from flet import *
from UI.login_buttons import build_buttons_for_entering_password
from database.source.filling_the_database import add_User

class RegistrationData:
    _instance = None
    data = {
        "login": "",
        "first_name": "",
        "surname": "",
        "email": "",
        "telephone": ""
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class Registration:
    def __init__(self, page: Page):
        self.page = page
        self.registration_data = RegistrationData()
        self.view = self.Registration_build_ui()

    def Registration_build_ui(self):
        registration_container = Container(
            width = 430,
            height = 932,
            border_radius = 30,
            gradient = LinearGradient(
                colors = ['#2B6064', '#71DEC5'],
                begin = alignment.top_center,
                end = alignment.bottom_center
            ),
            content = Column([
                self.build_stack(),
            ]),
        )
        return registration_container

    def build_stack(self):
        stack = Stack(
            controls = [
                self.build_container(),
                self.button_registration(),
            ]
        )
        return stack

    def build_container(self):
        return Container(
            width = 357,
            height = 740,
            border_radius = 30,
            bgcolor = '#2B6064',
            content = Column([
                build_buttons_for_entering_password(38, 26, '#3EA392'),
                self.text_container_telephone_number_registration(),
                self.textField_container_login_registration(),
                self.textField_container_name_registration(),
                self.textField_container_surname_registration(),
                self.textField_container_email_registration(),
                self.textField_container_telephone_number_registration(),
            ]),
            margin = margin.only(left = 37, top = 60),
        )

    def text_container_telephone_number_registration(self):
        return Container(
            content = Text(
                value = ""
            ),
            margin = margin.only(left = 18, top = 20),
            width = 320,
            height = 30,
            border_radius = 20,
            bgcolor = '#3EA392'
        )

    def textField_container_login_registration(self):
        def on_change(e):
            self.profile_data.data["login"] = e.control.value

        return Container(
            content = TextField(
                on_change = on_change,
                bgcolor = '#745BD0',
                color = '#330066',
                multiline = True,
                border_radius = 20,
                content_padding = padding.all(8),
                border_color = '#745BD0',
                label = "Login",
                autofill_hints = AutofillHint.NAME,
            ),
            margin = margin.only(left = 18, top = 0),
            width = 320,
            height = 40,
        )

    def textField_container_name_registration(self):
        def on_change(e):
            self.profile_data.data["first_name"] = e.control.value

        return Container(
            content = TextField(
                on_change = on_change,
                bgcolor = '#745BD0',
                color = '#330066',
                multiline = True,
                border_radius = 20,
                content_padding = padding.all(8),
                border_color = '#745BD0',
                label = "Имя",
                autofill_hints = AutofillHint.NAME,
            ),
            margin = margin.only(left = 18, top = 0),
            width = 320,
            height = 40,
        )

    def textField_container_surname_registration(self):
        def on_change(e):
            self.profile_data.data["surname"] = e.control.value

        return Container(
            content = TextField(
                on_change = on_change,
                bgcolor = '#745BD0',
                color = '#330066',
                multiline = True,
                border_radius = 20,
                content_padding = padding.all(8),
                border_color = '#745BD0',
                label = "Фамилия",
                autofill_hints = AutofillHint.NAME,
            ),
            margin = margin.only(left = 18, top = 0),
            width = 320,
            height = 40,
        )

    def textField_container_email_registration(self):
        def on_change(e):
            self.profile_data.data["email"] = e.control.value

        return Container(
            content = TextField(
                on_change = on_change,
                bgcolor = '#745BD0',
                color = '#330066',
                multiline = True,
                border_radius = 20,
                content_padding = padding.all(8),
                border_color = '#745BD0',
                label = "Email",
                autofill_hints = [AutofillHint.EMAIL],
            ),
            margin = margin.only(left = 18, top = 0),
            width = 320,
            height = 40,
        )

    def textField_container_telephone_number_registration(self):
        def on_change(e):
            self.profile_data.data["telephone"] = e.control.value

        return Container(
            content = TextField(
                on_change = on_change,
                bgcolor = '#745BD0',
                color = '#330066',
                multiline = True,
                border_radius = 20,
                content_padding = padding.all(8),
                border_color = '#745BD0',
                border_width = 3,
                label = "Номер телефона",
                autofill_hints = [AutofillHint.TELEPHONE_NUMBER],
            ),
            margin = margin.only(left = 18, top = 0),
            width = 320,
            height = 40,
        )

    def button_registration(self):
        def on_click(e):
            add_User(),
            self.page.go("/home")

            # self.page.snack_bar.open = True
            # self.page.update()

        return Container(
            content = ElevatedButton(
                text = "Сохранить данные",
                bgcolor = '#3EA392',
                color = "#FFFFFF",
                on_click = on_click,
                style = ButtonStyle(
                    text_style = TextStyle(
                        size = 25,
                        weight = FontWeight.W_700,
                        font_family = "Arial",
                    ),
                )
            ),
            margin = margin.only(left = 63, top = 815),
            width = 305,
            height = 50,
        )