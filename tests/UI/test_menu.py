import pytest
from playwright.sync_api import expect
from .pages.menu_page import MenuPage
from .pages.products_page import ProductsPage

@pytest.mark.ui
@pytest.mark.regression
class TestMenu:
    def test_reset_app_state_clears_cart(self, auth_page):
        products = ProductsPage(auth_page)
        menu = MenuPage(auth_page)

        products.add_item("sauce-labs-backpack")
        expect(auth_page.locator(".shopping_cart_badge")).to_have_text("1")

        menu.reset_app_state()
        expect(auth_page.locator(".shopping_cart_badge")).not_to_be_visible()

