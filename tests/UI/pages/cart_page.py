from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page

    def badge_text(self) -> str | None:
        badge = self.page.locator(".shopping_cart_badge")
        return badge.inner_text() if badge.is_visible() else None

    def remove_item(self, data_test_value: str):
        self.page.locator(f'[data-test="remove-{data_test_value}"]').click()

    def items_texts(self) -> list[str]:
        return [el.inner_text() for el in self.page.locator('[data-test="inventory-item-name"]').all()]

    def continue_shopping(self):
        self.page.locator('[data-test="continue-shopping"]').click()

    def checkout(self):
        self.page.locator('[data-test="checkout"]').click()