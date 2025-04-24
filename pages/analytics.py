from flet import *

class Analytics:
    def __init__(self, page: Page):
        self.page = page
        self.view = self.Analytics_build_ui()

    def Analytics_build_ui(self):
        analytics_container = Container(
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
        return analytics_container

    def build_stack(self):
        stack = Stack(
            controls = [
                self.build_bottom_navigation(),
            ]
        )
        return stack

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
                            icon_color = '#FFFFFF',
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
                            icon_color = '#00F8D7',
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