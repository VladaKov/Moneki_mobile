from flet import *
from API.api_currencies import get_api_currencies

def build_container_currencies():
    build_container_currencies = Row(
        scroll = ScrollMode.AUTO,
        controls = [
            container_currency('USD', 'Images\Flags\Dollar_US.png', 'Доллар США'),
            container_currency('EUR', 'Images\Flags\Euro.png', 'Евро'),
            container_currency('GBP', 'Images\Flags\Pound.png', 'Фунт'),
            container_currency('CNY', 'Images\Flags\Yuan.png', 'Юань'),
            container_currency('CHF', 'Images\Flags\Franc.png', 'Франк'),
            container_currency('CAD', 'Images\Flags\Canadian_Dollar.png', 'Доллар Канады'),
            container_currency('JPY', 'Images\Flags\Yen.png', 'Иена'),
        ]
    )
    return build_container_currencies

def container_currency(name_Val, image_path, name):
    return Container(
        width = 178,
        height = 126,
        border_radius = 20,
        gradient = LinearGradient(
            colors = ['#330066', '#220044'],
            stops = [0.0, 1],
            begin = alignment.top_center,
            end = alignment.bottom_center
        ),
        content = Column([
            Stack(
                controls = [
                    text_currency(name_Val),
                    text_name_currency(name),
                    row_currencies_text_icon(name_Val),
                    image_currency(image_path),
                ]
            )
        ])
    )

def text_currency(name_Val):
    return Container(
        Text(
            value = name_Val,
            size = 23,
            weight = FontWeight.W_500,
            color = '#FFFFFF',
            font_family = "Arial",
        ),
        margin = margin.only(left = 95, top = 8),
    )

def text_name_currency(name):
    return Container(
        Text(
            value = name,
            size = 16,
            weight = FontWeight.W_300,
            color = '#9D9FE7',
            font_family = "Arial",
        ),
        margin = margin.only(left = 95, top = 35),
    )

def row_currencies_text_icon(name_Val):
    return Container(
        margin = margin.only(left = 25, top = 90),
        content = Row(
            controls = [
                text_price_currency(name_Val),
                icon_rub()
            ]
        )
    )

def text_price_currency(name_Val):
    return Container(
        Text(
            value = get_api_currencies(name_Val),
            size = 20,
            weight = FontWeight.W_300,
            color = '#FFFFFF',
            font_family = "Arial",
        )
    )

def icon_rub():
    return Container(
        Icon(
            name = Icons.CURRENCY_RUBLE_ROUNDED,
            color = '#FFFFFF',
            size = 20
        ),
    )

def image_currency(image_path):
    return Container(
        Image(
            src = image_path,
            width = 55,
            height = 40,
        ),
        margin = margin.only(left = 25, top = 14),
    )
