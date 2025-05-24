from flet import *
import math
from UI.bottom_navigation import build_bottom_navigation
from UI.added_cards import build_added_cards

class Profile:
    def __init__(self, page: Page):
        self.page = page
        self.view = self.Profile_build_ui(page)

    def Profile_build_ui(self, page: Page):
        profile_container = Container(
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
        return profile_container

    def build_stack(self, page: Page):
        stack = Stack(
            controls = [
                self.build_information_window(),
                self.build_text_active_cards(),
                self.build_row_added_cards(),
                self.build_button_change_profile(),
                build_bottom_navigation(page),
            ]
        )
        return stack


    def build_information_window(self):
        return Container(
            width = 430,
            height = 430,
            border_radius = 30,
            gradient = SweepGradient(
                center = Offset(0.0, 0.0),
                start_angle = 1,
                end_angle = math.pi * 2,
                colors = ['#9D9FE7', '#4A17BA', '#280D6A', '#05041B', '#05041B', '#280D6A', '#9D9FE7'],
            ),
            content = Stack(
                controls = [
                    self.text_profile(),
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
            margin = margin.only(left = 20, top = 90),
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
                weight = FontWeight.W_600,
                color = '#05041B',
                font_family = "Arial",
            ),
            margin = margin.only(left = 140, top = 340),
        )

    def text_telephone(self):
        return Container(
            Text(
                value = '+7 (923) 456-78-90',
                size = 20,
                weight = FontWeight.W_600,
                color = '#05041B',
                font_family = "Arial",
            ),
            margin = margin.only(left = 122, top = 380),
        )

    def build_text_active_cards(self):
        return Container(
            Text(
                value = 'Активные карты',
                size = 20,
                color = '#9D9FE7',
                font_family = "Arial",
            ),
            margin = margin.only(left = 25, top = 455),
        )

    def build_row_added_cards(self):
        return Container(
            build_added_cards(),
            margin = margin.only(left = 20, top = 510),
        )

    def build_button_change_profile(self):
        return Container(
            content = Row(
                controls = [
                    self.icon_change_profile(),
                    self.text_change_profile(),
                    self.icon_change_profile_arrow(),
                ],
                alignment = MainAxisAlignment.CENTER,
                spacing = 10
            ),
            gradient = LinearGradient(
                colors = ['#4A17BA', '#330066'],
                stops = [0.25, 0.77],
                begin = alignment.top_left,
                end = alignment.bottom_right
            ),
            shadow = BoxShadow(
                spread_radius = 1,
                blur_radius = 5,
                color = '#220044',
                offset = Offset(0, 4),
            ),
            ink = True,
            width = 412,
            height = 80,
            border_radius = 20,
            margin = margin.only(left = 10, top = 730),
            on_click = lambda e: e.page.go("/profile_changes"),
        )

    def icon_change_profile(self):
        return Icon(
            name = Icons.AUTO_FIX_HIGH,
            color = '#9D9FE7',
            size = 35,
        )

    def text_change_profile(self):
        return Text(
            value = "Изменить профиль",
            size = 25,
            weight = FontWeight.W_500,
            color = '#9D9FE7',
            font_family = "Arial",
        )

    def icon_change_profile_arrow(self):
        return Icon(
            name = Icons.ARROW_FORWARD_ROUNDED,
            color = '#9D9FE7',
            size = 30,
        )

