from flet import *

def build_buttons_for_entering_password(left_num, Top_num, Color_num):
    return Container(
        content = Column(
            controls = [
                Container(
                    content = Row(
                        controls = [
                            num('1', Color_num),
                            num('2', Color_num),
                            num('3', Color_num),
                        ],
                        spacing = 23
                    ),
                    margin = margin.only(top = 13),
                ),
                Container(
                    content = Row(
                        controls = [
                            num('4', Color_num),
                            num('5', Color_num),
                            num('6', Color_num),
                        ],
                        spacing = 23
                    ),
                    margin = margin.only(top = 13),
                ),
                Container(
                    content = Row(
                        controls = [
                            num('7', Color_num),
                            num('8', Color_num),
                            num('9', Color_num),
                        ],
                        spacing = 23
                    ),
                    margin = margin.only(top = 13),
                ),
                Container(
                    content = Row(
                        controls = [
                            num('0', Color_num),
                            button_delete(Color_num),
                        ],
                        spacing = 23
                    ),
                    margin = margin.only(left = 98, top = 13),
                )
            ]
        ),
        margin = margin.only(left = left_num, top = Top_num),
    )

def num(text_num, Color_num):
    return Container(
        bgcolor = Color_num,
        width = 75,
        height = 75,
        border_radius = 15,
        content = Row(
            controls = [
                text_number(text_num)
            ],
            alignment = MainAxisAlignment.CENTER,
        ),
        shadow = BoxShadow(
            spread_radius = 1,
            blur_radius = 5,
            color = '#143032',
            offset = Offset(0, 4),
        ),
        ink = True,
        on_click = lambda e: e.page,
    )

def text_number(text_num):
    return Container(
        content = Text(
            value = text_num,
            color = '#FFFFFF',
            size = 36,
            weight = FontWeight.W_800,
            font_family = "Arial"
        ),
    )

def button_delete(Color_num):
    return Container(
        bgcolor = Color_num,
        width = 75,
        height = 50,
        border_radius = 15,
        content = Row(
            controls = [
                icon_del()
            ],
            alignment = MainAxisAlignment.CENTER,
        ),
        shadow = BoxShadow(
            spread_radius = 1,
            blur_radius = 5,
            color = '#143032',
            offset = Offset(0, 4),
        ),
        ink = True,
        on_click = lambda e: e.page,
    )


def icon_del():
    return Icon(
        name = Icons.DISABLED_BY_DEFAULT,
        color = "#FFFFFF",
        size = 36,
    )
