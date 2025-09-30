import pytest
import testit
from .pages.products_page import ProductsPage

@pytest.mark.ui
@pytest.mark.regression
class TestSorting:

    @pytest.mark.smoke
    @testit.workItemIds(191)                # ID ручного кейса из Test IT
    @testit.externalId("UI-SORT-001")         # уникальный ID автотеста в Test IT
    @testit.displayName("Sort by Name A→Z")   # внутреннее имя автотеста
    @testit.title("Проверка сортировки A→Z")  # заголовок в карточке
    @testit.labels("ui", "sorting", "smoke")  # теги (опционально)
    def test_sort_by_name_az(self, auth_page):
        products = ProductsPage(auth_page)
        products.sort("az")
        names = products.item_names()
        assert names == sorted(names)

    # def test_sort_by_name_za(self, auth_page):
    #     products = ProductsPage(auth_page)
    #     products.sort("za")
    #     names = products.item_names()
    #     assert names == sorted(names, reverse=True)
    #
    # def test_sort_by_price_low_high(self, auth_page):
    #     products = ProductsPage(auth_page)
    #     products.sort("lohi")
    #     prices = products.item_prices()
    #     assert prices == sorted(prices)
    #
    # def test_sort_by_price_high_low(self, auth_page):
    #     products = ProductsPage(auth_page)
    #     products.sort("hilo")
    #     prices = products.item_prices()
    #     assert prices == sorted(prices, reverse=True)