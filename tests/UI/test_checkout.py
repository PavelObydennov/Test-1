import pytest
from playwright.sync_api import expect
from .pages.products_page import ProductsPage
from .pages.checkout_page import CheckoutPage

@pytest.mark.ui
@pytest.mark.regression
class TestCheckoutValidation:
    def _goto_step_one(self, page):
        products = ProductsPage(page)
        checkout = CheckoutPage(page)
        products.add_item("sauce-labs-backpack")
        products.open_cart()
        checkout.start()  # если у тебя метод назван иначе — используй свой
        return checkout

    def test_first_name_required(self, auth_page):
        checkout = self._goto_step_one(auth_page)
        checkout.fill_step_one("", "Doe", "12345")
        expect(auth_page.locator('[data-test="error"]')).to_contain_text("First Name is required")

    def test_last_name_required(self, auth_page):
        checkout = self._goto_step_one(auth_page)
        checkout.fill_step_one("John", "", "12345")
        expect(auth_page.locator('[data-test="error"]')).to_contain_text("Last Name is required")

    def test_postal_code_required(self, auth_page):
        checkout = self._goto_step_one(auth_page)
        checkout.fill_step_one("John", "Doe", "")
        expect(auth_page.locator('[data-test="error"]')).to_contain_text("Postal Code is required")