# import pytest
# from playwright.sync_api import expect
# from .pages.login_page import LoginPage
#
#
# @pytest.mark.ui
# def test_login_success(page):
#     login_page = LoginPage(page)
#
#     # Открываем сайт
#     login_page.open()
#
#     # Логинимся (готовые тестовые данные из Swag Labs)
#     login_page.login("standard_user", "secret_sauce")
#
#     # Проверяем, что мы на странице товаров
#     expect(page.locator('[data-test="title"]')).to_have_text("Products")