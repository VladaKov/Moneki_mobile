from flet import *

class Home:
    def __init__(self, page: Page):
        self.page = page
        self.view = self.Home_build_ui()

    def Home_build_ui(self):
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
                self.build_stack(),
            ]),
        )
        return home_container

    def build_stack(self):
        stack = Stack(
            controls = [
                self.build_text_mokeki(),
                self.build_button(),
                self.build_cat_image(),
                self.build_text_vyluty(),
                self.build_row_vyluty(),
                self.build_text_expenses(),
                self.build_row_expenses(),
                self.build_bottom_navigation(),
            ]
        )
        return stack

    def build_text_mokeki(self):
        return Container(
            Text(
                value = "MONEKI",
                size = 37,
                weight = FontWeight.W_800,
                color = '#00F8D7',
                font_family = "Arial",
            ),
            margin = margin.only(left = 40, top = 65),
        )

    def build_button(self):
        return Container(
            width = 400,
            height = 260,
            border_radius = 30,
            gradient = LinearGradient(
                colors = ['#4A17BA', '#800FDC', '#B508FF'],
                stops = [0.25, 0.77, 1],
                begin = alignment.top_center,
                end = alignment.bottom_center
            ),
            margin = margin.only(left = 15, top = 180),
            content = Column([
                Stack(
                    controls = [
                        Container(
                    Text(
                        value = "В кошельке",
                        size = 24,
                        weight = FontWeight.W_400,
                        color = '#FFFFFF',
                        font_family = "Arial",
                    ),
                    margin = margin.only(left = 35, top = 50),
                ),
                Container(
                    content = Row(
                        controls = [
                            Text(
                                value = "Смотреть аналитику",
                                size = 25,
                                weight = FontWeight.W_700,
                                color = '#FFFFFF',
                                font_family = "Arial",
                            ),
                            Icon(
                                name = Icons.ARROW_FORWARD_ROUNDED,
                                color = '#FFFFFF',
                                size = 30,
                            ),
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
                    on_click = lambda e: e.page.go("/profile"),
                ),
                    ]
                )
            ]),
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

    def build_row_vyluty(self):
        return Container(
            margin = margin.only(left = 15, top = 510),
            content = Row(
                scroll = ScrollMode.AUTO,
                controls = [
                    *[Container(
                        width = 178,
                        height = 126,
                        border_radius = 20,
                        gradient = LinearGradient(
                            colors = ['#330066', '#220044'],
                            stops = [0.0, 1],
                            begin = alignment.top_center,
                            end = alignment.bottom_center
                        ),
                    )for _ in range(5)],
                ]
            )
        )

    def build_text_expenses(self):
        return Container(
            Text(
                value = "Последние траты",
                size = 20,
                color = '#9D9FE7',
                font_family = "Arial",
            ),
            margin = margin.only(left = 30, top = 650),
        )

    def build_row_expenses(self):
        return Container(
            height = 200,
            width = 400,
            margin = margin.only(left = 15, top = 690),
            content = ListView(
                on_scroll = ScrollMode.AUTO,
                spacing = 10,
                controls = [
                    *[Container(
                        width = 400,
                        height = 80,
                        border_radius = 20,
                        gradient = LinearGradient(
                            colors = ['#480090', '#330066'],
                            stops = [0.0, 1],
                            begin = alignment.top_left,
                            end = alignment.bottom_right
                        ),
                    )for _ in range(5)],
                ]
            ),
        )

    def build_bottom_navigation(self):
        return Container(
            width = 430,
            height = 80,
            gradient = LinearGradient(
                colors = ['#220044', '#330066'],
                stops = [0.0, 1],
                begin = alignment.top_center,
                end = alignment.bottom_center
            ),
            margin = margin.only(left = 0, top = 848),
            content = Container(
                content = Row(
                    controls = [
                        IconButton(
                            icon = Icons.HOME_FILLED,
                            icon_color = '#00F8D7',
                            icon_size = 40,
                            highlight_color = '#4A17BA',
                            on_click = lambda e: e.page.go("/home")
                        ),
                        IconButton(
                            icon = Icons.PERSON,
                            icon_color = '#FFFFFF',
                            icon_size = 40,
                            highlight_color = '#4A17BA',
                            on_click = lambda e: e.page.go("/profile")
                        ),
                        IconButton(
                            icon = Icons.AUTO_GRAPH_ROUNDED,
                            icon_color = '#FFFFFF',
                            icon_size = 40,
                            highlight_color = '#4A17BA',
                            on_click = lambda e: e.page.go("/analytics"),
                        ),
                        IconButton(
                            icon = Icons.ADD_TO_PHOTOS_ROUNDED,
                            icon_color = '#FFFFFF',
                            icon_size = 35,
                            highlight_color = '#4A17BA',
                            on_click = lambda e: e.page.go("/bank_cards"),
                        ),
                    ],
                    alignment = MainAxisAlignment.CENTER,
                    spacing = 50
                ),
            ),
        )