from flet import *

def bild_button_scrol():
    return Container(
        height = 782,
        width = 390,
        content = Column(
            spacing = 20,
            controls = [
                build_button_name_bank("Альфа банк", "#E00404", "#76001B", '#FFFFFF'),
                build_button_name_bank("МКБ", '#E0043E', '#270A4F', '#FFFFFF'),
                build_button_name_bank("ВТБ", "#185C8D", "#002958", '#FFFFFF'),
                build_button_name_bank("Газпромбанк", "#19468A", "#080132", '#FFFFFF'),
                build_button_name_bank("Зенит банк", "#0CB79A", "#00545F", '#05041B'),
                build_button_name_bank("Сбер банк", '#62BE1D', "#3EA37B", '#FFFFFF'),
                build_button_name_bank("T-Банк", '#F7ED3B', '#FFB031', '#05041B'),
            ]
        ),
    )

def build_button_name_bank(Name_bank, color1, color2, Color_Text):
    return Container(
        content = Column(
            controls = [
                text_button_name_bank(Name_bank, Color_Text),
            ]
        ),
        gradient = LinearGradient(
            colors = [color1, color2],
            begin = alignment.top_left,
            end = alignment.bottom_right
        ),
        shadow = BoxShadow(
            spread_radius = 1,
            blur_radius = 5,
            color = '#05041B',
            offset = Offset(0, 4),
        ),
        ink = True,
        width = 390,
        height = 65,
        border_radius = 20,
        # on_click = True,
    )

def text_button_name_bank(Name_bank, Color_Text):
    return Container(
        content = Text(
            value = Name_bank,
                size = 25,
                weight = FontWeight.W_600,
                color = Color_Text,
                font_family = "Arial",
            ),
            margin = margin.only(left = 25, top = 20),
        )
