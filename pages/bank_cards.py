from flet import *
from UI.bottom_navigation import build_bottom_navigation
from UI.button_name_bank import bild_button_scrol

class Bank_cards:
    def __init__(self, page: Page):
        self.page = page
        self.view = self.Bank_cards_build_ui(page)

    def Bank_cards_build_ui(self, page: Page):
        bank_cards_container = Container(
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
        return bank_cards_container

    def build_stack(self, page: Page):
        stack = Stack(
            controls = [
                self.build_scrol_added_cards(),
                build_bottom_navigation(page),
            ]
        )
        return stack

    def build_scrol_added_cards(self):
        return Container(
            bild_button_scrol(),
            margin = margin.only(left = 20, top = 75)
        )
