from flet import *
import math
from UI.bottom_navigation import build_bottom_navigation

class ProfileData:
    _instance = None
    data = {
        "first_name": "",
        "surname": "",
        "email": "",
        "telephone": ""
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

class Profile_changes:
    def __init__(self, page: Page):
        self.page = page
        self.profile_data = ProfileData()
        self.view = self.Profile_changes_build_ui(page)

    def Profile_changes_build_ui(self, page: Page):
        profile_changes_container = Container(
            width = 430,
            height = 932,
            border_radius = 30,
            gradient = LinearGradient(
                colors = ['#05041B', '#320A5C'],
                stops = [0.47, 0.9],
                begin = alignment.top_center,
                end = alignment.bottom_center
            ),
            content = Column([
                self.build_stack(page),
            ]),
        )
        return profile_changes_container

    def build_stack(self, page: Page):
        stack = Stack(
            controls = [
                self.build_information_window_change(),
                self.build_change_profile_container(),
                build_bottom_navigation(page),
            ]
        )
        return stack

    def build_information_window_change(self):
        return Container(
            width = 430,
            height = 430,
            border_radius = 30,
            gradient = SweepGradient(
                center = Offset(0.0, 0.0),
                start_angle = 1,
                end_angle = math.pi * 2,
                colors = ['#05041B', '#280D6A', '#4A17BA', '#9D9FE7', '#9D9FE7', '#4A17BA', '#05041B'],
            ),
            content = Stack(
                controls = [
                    self.text_profile(),
                    self.image_avatar(),
                    self.text_full_name(),
                    self.text_mail(),
                    self.text_telephone(),
                ]
            )
        )

    def text_profile(self):
        return Container(
            Text(
                value = 'Профиль',
                size = 32,
                weight = FontWeight.W_800,
                color = '#00F8D7',
                font_family = "Arial",
            ),
            margin = margin.only(left = 25, top = 70),
        )

    def image_avatar(self):
        return Container(
            content = Image(
                src = 'Images\catAvatar.png',
                width = 127,
                height = 127,
            ),
            margin = margin.only(left = 145, top = 150),
        )

    def text_full_name(self):
        return Container(
            width = 430,
            height = 60,
            top = 280,
            content = Row(
                alignment = MainAxisAlignment.SPACE_EVENLY,
                controls = [
                    Text(
                        value = 'Ивлеева Наталья',
                        size = 26,
                        weight = FontWeight.W_700,
                        color = '#FFFFFF',
                        font_family = "Arial",
                    ),
                ]
            )
        )

    def text_mail(self):
        return Container(
            Text(
                value = 'Evii.@mail.com',
                size = 20,
                weight = FontWeight.W_500,
                color = '#9D9FE7',
                font_family = "Arial",
            ),
            margin = margin.only(left = 140, top = 340),
        )

    def text_telephone(self):
        return Container(
            Text(
                value = '+7 (923) 456-78-90',
                size = 20,
                weight = FontWeight.W_500,
                color = '#9D9FE7',
                font_family = "Arial",
            ),
            margin = margin.only(left = 122, top = 380),
        )

    def build_change_profile_container(self):
        return Container(
            width=430,
            height=435,
            border_radius=30,
            gradient=LinearGradient(
                colors=['#320A5C', '#05041B'],
                stops=[0.47, 0.9],
                begin=alignment.top_center,
                end=alignment.bottom_center
            ),
            margin=margin.only(left=0, top=445),
            content=Column(
                controls=[
                    self.textField_container_first_name(),
                    self.textField_container_surname(),
                    self.textField_container_email(),
                    self.textField_container_telephone_number(),
                    self.button_change_profile(),
                ]
            )
        )

    def textField_container_first_name(self):
        def on_change(e):
            self.profile_data.data["first_name"] = e.control.value

        return Container(
            content=TextField(
                on_change=on_change,
                bgcolor='#3F0B90',
                color='#9D9FE7',
                border_color='#3F0B90',
                multiline=True,
                border_radius=20,
                label="Имя",
                autofill_hints=AutofillHint.NAME,
            ),
            margin=margin.only(left=10, top=20),
            width=410,
        )

    def textField_container_surname(self):
        def on_change(e):
            self.profile_data.data["surname"] = e.control.value

        return Container(
            content=TextField(
                on_change=on_change,
                bgcolor='#3F0B90',
                color='#9D9FE7',
                border_color='#3F0B90',
                multiline=True,
                border_radius=20,
                label="Фамилия",
                autofill_hints=AutofillHint.NAME,
            ),
            margin=margin.only(left=10, top=8),
            width=410,
        )

    def textField_container_email(self):
        def on_change(e):
            self.profile_data.data["email"] = e.control.value

        return Container(
            content=TextField(
                on_change=on_change,
                bgcolor='#3F0B90',
                color='#9D9FE7',
                border_color='#3F0B90',
                multiline=True,
                border_radius=20,
                label="Email",
                autofill_hints=[AutofillHint.EMAIL],
            ),
            margin=margin.only(left=10, top=8),
            width=410,
        )

    def textField_container_telephone_number(self):
        def on_change(e):
            self.profile_data.data["telephone"] = e.control.value

        return Container(
            content=TextField(
                on_change=on_change,
                bgcolor='#3F0B90',
                color='#9D9FE7',
                border_color='#3F0B90',
                multiline=True,
                border_radius=20,
                label="Номер телефона",
                autofill_hints=[AutofillHint.TELEPHONE_NUMBER],
            ),
            margin=margin.only(left=10, top=8),
            width=410,
        )

    def button_change_profile(self):
        def on_click(e):
            self.page.snack_bar = SnackBar(
                Text("Данные успешно сохранены!"),
                bgcolor="green",
            )
            self.page.snack_bar.open = True
            self.page.update()

        return Container(
            content=ElevatedButton(
                text="Сохранить изменения",
                bgcolor='#9D9FE7',
                color='#3F0B90',
                on_click=on_click,
                style=ButtonStyle(text_style=TextStyle(
                    size=20,
                    weight=FontWeight.W_500,
                    font_family="Arial",
                )),
            ),
            margin=margin.only(left=115, top=20),
        )

