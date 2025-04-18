from flet import *

class Home:
    def __init__(self, page: Page):
        self.page = page
        self.Home_build_ui()

    def Home_build_ui(self):
        self.page.title = "Home"
        self.page.bgcolor = '#008993'
        self.page.add(
            Container(
                width = 430,
                height = 932,
                border_radius = 30,
                gradient = LinearGradient(
                        colors = ['#05041B', '#320A5C'],
                        stops=[0.47, 0.9],
                        begin = alignment.top_center,
                        end = alignment.bottom_center
                ),
                content = Column([
                            Stack(
                                controls = [
                                    Text( # Текст MONEKI
                                        value = "MONEKI",
                                        size = 40,
                                        weight = "bold",
                                        color = '#00F8D7',
                                        top = 75,
                                        left = 40,
                                    ),
                                    Container( #Кнопка прехода на аналитику
                                        width = 400,
                                        height = 260,
                                        border_radius = 30,
                                        gradient = LinearGradient(
                                                colors = ['#4A17BA', '#800FDC', '#B508FF'],
                                                stops = [0.25, 0.77, 1],
                                                begin = alignment.top_center,
                                                end = alignment.bottom_center
                                        ),
                                        margin = margin.only(left = 15, top = 170),
                                        content = Column([
                                            Container(
                                                content = Row(
                                                            controls = [
                                                                Text(
                                                                    value = "Смотреть аналитику",
                                                                    size = 25,
                                                                    weight = "bold",
                                                                    color = '#FFFFFF',
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
                                                margin = margin.only(left = 25, top = 188),
                                                on_click = lambda e: print("Работает"),
                                            ),
                                        ]),
                                    ),
                                    Container(# Картинка кота
                                        Image(# 1,875
                                            src = 'Images\Cat.png',
                                            width = 202,
                                            height = 380,
                                        ),
                                        margin = margin.only(left = 200, top = 0),
                                    ),
                                    Container(
                                        margin = margin.only(left = 15, top = 470),
                                        content = Row(
                                            scroll = ScrollMode.AUTO,
                                            controls = [
                                                Container(
                                                    width = 178,
                                                    height = 126,
                                                    border_radius = 20,
                                                    gradient = LinearGradient(
                                                                    colors = ['#330066', '#220044'],
                                                                    stops = [0.0, 1],
                                                                    begin = alignment.top_center,
                                                                    end = alignment.bottom_center
                                                    ),
                                                ),
                                                Container(
                                                    width = 178,
                                                    height = 126,
                                                    border_radius = 20,
                                                    gradient = LinearGradient(
                                                                    colors = ['#330066', '#220044'],
                                                                    stops = [0.0, 1],
                                                                    begin = alignment.top_center,
                                                                    end = alignment.bottom_center
                                                    ),
                                                ),
                                                Container(
                                                    width = 178,
                                                    height = 126,
                                                    border_radius = 20,
                                                    gradient = LinearGradient(
                                                                    colors = ['#330066', '#220044'],
                                                                    stops = [0.0, 1],
                                                                    begin = alignment.top_center,
                                                                    end = alignment.bottom_center
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                    Container(
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
                                                            highlight_color = '#4A17BA'
                                                        ),
                                                        IconButton(
                                                            icon = Icons.PERSON,
                                                            icon_color = '#FFFFFF',
                                                            icon_size = 40,
                                                            highlight_color = '#4A17BA'
                                                        ),
                                                        IconButton(
                                                            icon = Icons.AUTO_GRAPH_ROUNDED,
                                                            icon_color = '#FFFFFF',
                                                            icon_size = 40,
                                                            highlight_color = '#4A17BA'
                                                        ),
                                                        IconButton(
                                                            icon = Icons.ADD_TO_PHOTOS_ROUNDED,
                                                            icon_color = '#FFFFFF',
                                                            icon_size = 35,
                                                            highlight_color = '#4A17BA'
                                                        ),
                                                    ],
                                                    alignment = MainAxisAlignment.CENTER,
                                                    spacing = 50
                                                    ),
                                                ),
                                    ),
                                ]
                            ),#заканчиватся стек
                ]),
            ),
        ),



