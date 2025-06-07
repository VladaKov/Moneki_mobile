from flet import *
from UI.login_buttons import build_buttons_for_entering_password

class Entrance:
    def __init__(self, page: Page):
        self.page = page
        self.view = self.Entrance_build_ui()

    def Entrance_build_ui(self):
        entrance_container = Container(
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
        return entrance_container

    def build_stack(self):
        stack = Stack(
            controls = [
                build_buttons_for_entering_password(75, 287, '#2B6064'),
            ]
        )
        return stack
