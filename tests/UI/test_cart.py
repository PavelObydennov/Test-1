import pytest
from playwright.sync_api import expect


@pytest.mark.ui
@pytest.mark.regression
class TestCart:

    # Добавление товара в корзину
    @pytest.mark.smoke
    def test_add_to_cart(self, auth_page):
        # Добавляем конкретный товар
        auth_page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
        # Открытие корзины
        auth_page.locator('[data-test="shopping-cart-link"]').click()
        # Проверяем, что в корзине есть добавленный товар
        expect(auth_page.locator(".shopping_cart_badge")).to_have_text("1")
    @pytest.mark.smoke
    # Удаление товара из корзины
    def test_remove_from_cart(self, auth_page):
        # Добавляем конкретный товар
        auth_page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
        # Открытие корзины
        auth_page.locator('[data-test="shopping-cart-link"]').click()
        # Удаляем конкретный товар
        auth_page.locator('[data-test="remove-sauce-labs-bike-light"]').click()
        # Проверяем, что в корзине нет товаров
        expect(auth_page.locator(".shopping_cart_badge")).not_to_be_visible()

    # Добавление нескольких (разных) товаров в корзину
    def test_cart_multiple_items(self, auth_page):
        # Добавление в корзину 3-х товаров
        auth_page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
        auth_page.locator('[data-test="add-to-cart-sauce-labs-fleece-jacket"]').click()
        auth_page.locator('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
        # Открытие корзины
        auth_page.locator('[data-test="shopping-cart-link"]').click()
        # Проверяем, что в корзинге лежат все добавленные товары
        expect(auth_page.locator('[data-test="item-0-title-link"]')).to_have_text('Sauce Labs Bike Light')
        expect(auth_page.locator('[data-test="item-5-title-link"]')).to_have_text('Sauce Labs Fleece Jacket')
        expect(auth_page.locator('[data-test="item-3-title-link"]')).to_have_text('Test.allTheThings() T-Shirt (Red)')


    # Корзина сохраняется после перехода на другую страницу
    # def test_cart_persists_after_navigation(self, auth_page):
    #     auth_page.locator()