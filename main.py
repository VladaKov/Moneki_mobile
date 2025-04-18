from flet import *
from pages.home import Home



def main(page: Page):
    Home(page)

    page.update()

    col1 = '#05041B'#задний фон самого приложения
    col2 = '#220044'#задний фон самого приложения, еще томная часть в курсах валют

    col3 = '#330066'#кнопки, иконки
    col4 = '#480090'#кнопки, иконки
    col5 = '#4A17BA'#кнопки, иконки

    col6 = '#9D9FE7'#текст

    col7 = '#800FDC'#
    col8 = '#B508FF'#

    col9 = '#00F8D7'#

app(target = main)