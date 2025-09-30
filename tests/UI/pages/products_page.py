from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page

    # value ∈ {"az","za","lohi","hilo"}
    def sort(self, value: str):
        self.page.locator('[data-test="product-sort-container"]').select_option(value)

    # data_test_value: например "sauce-labs-backpack"
    def add_item(self, data_test_value: str):
        self.page.locator(f'[data-test="add-to-cart-{data_test_value}"]').click()

    def remove_item(self, data_test_value: str):
        self.page.locator(f'[data-test="remove-{data_test_value}"]').click()

    def open_cart(self):
        self.page.locator(".shopping_cart_link").click()

    def item_names(self) -> list[str]:
        return [el.inner_text() for el in self.page.locator('[data-test="inventory-item-name"]').all()]

    def item_prices(self) -> list[float]:
        raw = [el.inner_text() for el in self.page.locator('.inventory_item_price').all()]
        return [float(x.replace('$', '')) for x in raw]