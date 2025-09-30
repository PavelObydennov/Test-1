from playwright.sync_api import Page, expect

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def start(self):
        self.page.locator('[data-test="checkout"]').click()

    def fill_step_one(self, first: str, last: str, postal: str):
        self.page.locator('[data-test="firstName"]').fill(first)
        self.page.locator('[data-test="lastName"]').fill(last)
        self.page.locator('[data-test="postalCode"]').fill(postal)
        self.page.locator('[data-test="continue"]').click()

    def finish(self):
        self.page.locator('[data-test="finish"]').click()

    def expect_success(self):
        expect(self.page.locator('.complete-header')).to_have_text('Thank you for your order!')