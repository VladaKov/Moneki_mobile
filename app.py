from flet import *
from pages.home import Home
from pages.profile import Profile
from pages.analytics import Analytics
from pages.bank_cards import Bank_cards
from pages.profile_changes import Profile_changes
from pages.registration import Registration
from pages.entrance import Entrance


def App(page: Page):
    s = True
    def route_change(e):
        page.views.clear()

        if page.route == "/":
            registration = Registration(page)
            page.views.append(
                View("/", [registration.view], padding = 0)
            )

        elif page.route == "/entrance":
            entrance = Entrance(page)
            page.views.append(
                View("/entrance", [entrance.view], padding = 0)
            )

        elif page.route == "/home":
            home = Home(page)
            page.views.append(
                View("/home", [home.view], padding = 0)
            )

        elif page.route == "/profile":
            profile = Profile(page)
            page.views.append(
                View("/profile", [profile.view], padding = 0)
            )

        elif page.route == "/analytics":
            analytics = Analytics(page)
            page.views.append(
                View("/analytics", [analytics.view], padding = 0)
            )

        elif page.route == "/bank_cards":
            bank_cards = Bank_cards(page)
            page.views.append(
                View("/bank_cards", [bank_cards.view], padding = 0)
            )

        elif page.route == "/profile_changes":
            profile_changes = Profile_changes(page)
            page.views.append(
                View("/profile_changes", [profile_changes.view], padding = 0)
            )

        page.update()

    page.on_route_change = route_change
    if s == True:
        page.go("/")
    else:
        page.go("/entrance")