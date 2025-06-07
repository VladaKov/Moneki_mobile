from flet import *
import math
# from UI.container_currencies import build_container_currencies
from UI.bottom_navigation import build_bottom_navigation

class Home:
    def __init__(self, page: Page):
        self.page = page
        self.view = self.Home_build_ui(page)

    def Home_build_ui(self, page: Page):
        home_container = Container(
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
        return home_container

    def build_stack(self, page: Page):
        stack = Stack(
            controls = [
                self.build_text_mokeki(),
                self.build_stack_of_coins_image(),
                self.build_button_analytics(),
                self.build_cat_image(),
                self.build_text_vyluty(),
                # self.build_row_vyluty(),
                build_bottom_navigation(page),
            ]
        )
        return stack

    def build_text_mokeki(self):
        return Container(
            Text(
                value = "MONEKI",
                size = 39,
                weight = FontWeight.W_800,
                color = '#00F8D7',
                font_family = "Arial",
            ),
            margin = margin.only(left = 20, top = 68),
        )

    def build_button_analytics(self):
        return Container(
            width = 400,
            height = 260,
            border_radius = 30,
            gradient = SweepGradient(
                center = Offset(0.0, 0.0),
                start_angle = 1,
                end_angle = math.pi * 2,
                colors = ['#9D9FE7', '#71DEC5', '#745BD0', '#4A17BA', '#4A17BA', '#745BD0', '#9D9FE7'],
            ),
            margin = margin.only(left = 15, top = 180),
            content = Column([
                Stack(
                    controls = [
                        self.text_Good(),
                        self.text_afternoon(),
                        self.text_icon_analytics(),
                    ]
                ),
            ]),
        )


    def text_Good(self):
        return Container(
            Text(
                value = "Добрый",
                size = 40,
                weight = FontWeight.W_600,
                color = '#FFFFFF',
                font_family = "Arial",
            ),
            margin = margin.only(left = 35, top = 45),
        )

    def text_afternoon(self):
        return Container(
            Text(
                value = "день !",
                size = 40,
                weight = FontWeight.W_600,
                color = '#FFFFFF',
                font_family = "Arial",
            ),
            margin = margin.only(left = 85, top = 95),
        )

    def text_icon_analytics(self):
        return Container(
            content = Row(
                controls = [
                    self.text_analytics(),
                    self.icon_analytics_arrow(),
                ],
                alignment = MainAxisAlignment.CENTER,
                spacing = 10
            ),
            gradient = LinearGradient(
                colors = ['#330066', '#4A17BA'],
                stops = [0.25, 0.77],
                begin = alignment.top_left,
                end = alignment.bottom_right
            ),
            shadow = BoxShadow(
                spread_radius = 1,
                blur_radius = 5,
                color = '#320A5C',
                offset = Offset(0, 4),
            ),
            ink = True,
            width = 340,
            height = 60,
            border_radius = 20,
            margin = margin.only(left = 25, top = 180),
            on_click = lambda e: e.page.go("/analytics"),
        )

    def text_analytics(self):
        return Text(
            value = "Смотреть аналитику",
            size = 25,
            weight = FontWeight.W_500,
            color = '#FFFFFF',
            font_family = "Arial",
        )

    def icon_analytics_arrow(self):
        return Icon(
            name = Icons.ARROW_FORWARD_ROUNDED,
            color = '#FFFFFF',
            size = 30,
        )

    def build_cat_image(self):
        return Container(
            Image(
                src = 'Images/Cat.png',
                width = 202,
                height = 380,
            ),
            margin = margin.only(left = 205, top = 0),
        )

    def build_text_vyluty(self):
        return Container(
            Text(
                value = "Курс валют",
                size = 20,
                color = '#9D9FE7',
                font_family = "Arial",
            ),
            margin = margin.only(left = 30, top = 470),
        )

    # def build_row_vyluty(self):
    #     return Container(
    #         build_container_currencies(),
    #         margin = margin.only(left = 15, top = 510),
    #     )

    def build_stack_of_coins_image(self):
        return Container(
            Image(
                src = 'Images\stack_of_coins.png',
                width = 513,
                height = 513,
            ),
            margin = margin.only(left = -15, top = 480),
        )
