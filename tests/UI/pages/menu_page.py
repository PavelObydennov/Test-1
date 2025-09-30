from playwright.sync_api import Page, expect

class MenuPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.locator("#react-burger-menu-btn").click()
        expect(self.page.locator("#reset_sidebar_link")).to_be_visible()

    def close(self):
        self.page.locator("#react-burger-cross-btn").click()

    def reset_app_state(self):
        self.open()
        self.page.locator("#reset_sidebar_link").click()
        # после ресета значок корзины должен исчезнуть
        expect(self.page.locator(".shopping_cart_badge")).not_to_be_visible()
        self.close()

    def logout(self):
        self.open()
        self.page.locator("#logout_sidebar_link").click()