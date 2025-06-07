from flet import *

def build_bottom_navigation(page: Page):
    return Container(
        container_bottom_navigation(page),
        width = 430,
        height = 80,
        gradient = LinearGradient(
            colors = ['#220044', '#330066'],
            stops = [0.0, 1],
            begin = alignment.top_center,
            end = alignment.bottom_center
        ),
        margin = margin.only(left = 0, top = 852),
    )

def container_bottom_navigation(page: Page):
    return Container(
        content = Row(
            controls = [
                icon_home(page),
                icon_profile(page),
                icon_analytics(page),
                icon_bank_cards(page),
            ],
            alignment = MainAxisAlignment.CENTER,
            spacing = 50,
        )
    )

def icon_home(page: Page):
    return IconButton(
        icon = Icons.HOME_FILLED,
        icon_color = '#00F8D7' if page.route in ["/", "/home"] else '#FFFFFF',
        icon_size = 40,
        highlight_color = '#4A17BA',
        on_click = lambda e: e.page.go("/home")
    )

def icon_profile(page: Page):
    return IconButton(
        icon = Icons.PERSON,
        icon_color = '#00F8D7' if page.route in ["/profile_changes" ,"/profile"] else '#FFFFFF',
        icon_size = 40,
        highlight_color = '#4A17BA',
        on_click = lambda e: e.page.go("/profile")
    )

def icon_analytics(page: Page):
    return IconButton(
        icon = Icons.AUTO_GRAPH_ROUNDED,
        icon_color = '#00F8D7' if page.route == "/analytics" else '#FFFFFF',
        icon_size = 40,
        highlight_color = '#4A17BA',
        on_click = lambda e: e.page.go("/analytics"),
    )

def icon_bank_cards(page: Page):
    return IconButton(
        icon = Icons.ADD_CARD_OUTLINED,
        icon_color = '#00F8D7' if page.route == "/bank_cards" else '#FFFFFF',
        icon_size = 35,
        highlight_color = '#4A17BA',
        on_click = lambda e: e.page.go("/bank_cards"),
    )