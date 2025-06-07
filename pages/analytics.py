from flet import *
from UI.bottom_navigation import build_bottom_navigation
from UI.added_cards import build_added_cards

class Analytics:
    def __init__(self, page: Page):
        self.page = page
        self.view = self.Analytics_build_ui(page)

    def Analytics_build_ui(self, page: Page):
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
                self.build_stack(page),
            ]),
        )
        return analytics_container

    def build_stack(self, page: Page):
        stack = Stack(
            controls = [
                self.build_row_added_cards(),
                build_bottom_navigation(page),
            ]
        )
        return stack

    def build_row_added_cards(self):
        return Container(
            build_added_cards(),
            margin = margin.only(left = 20, top = 100),
        )

