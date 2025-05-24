from flet import *
import math

def build_added_cards():
    build_added_cards = Row(
        scroll = ScrollMode.AUTO,
        controls = [
            container_cards("1234 5678 9012 3456", "Мир"),
            container_cards("4563 2342 8756 4323", "Visa")
        ]
    )
    return build_added_cards

def container_cards(number_cards, name_cards):
    return Container(
        width = 314,
        height = 185,
        border_radius = 35,
        gradient = SweepGradient(
            center = Offset(0.6, -0.2),
            start_angle = 0,
            end_angle = math.pi * 2,
            colors = ['#021C25', '#9D9FE7', '#71DEC5', '#2B6064', '#163A40' ,'#021C25'],
            stops = [0.12, 0.36, 0.60, 0.89 ,0.95, 1],
        ),
        content = Column([
            Stack(
                controls = [
                    text_name_cards(name_cards),
                    text_number_cards(number_cards),
                ]
            )
        ])
    )

def text_name_cards(name_cards):
    return Container(
        Text(
            value = name_cards,
            size = 32,
            weight = FontWeight.W_800,
            color = '#021C25',
            font_family = "Arial",
        ),
        margin = margin.only(left = 200, top = 15),
    )

def text_number_cards(number_cards):
    return Container(
        Text(
            value = number_cards,
            size = 26,
            weight = FontWeight.W_400,
            color = '#021C25',
            font_family = "Be Vietnam",
        ),
        margin = margin.only(left = 23, top = 135),
    )
