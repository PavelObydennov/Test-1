# Pet Project: UI автотесты (Swag Labs) + DB

## Технологии
- Python 3.12
- pytest
- Playwright (Python)
- python-dotenv (ENV)
- psycopg2-binary (PostgreSQL)
- Маркировки: `ui`, `smoke`, `regression`, `db`

---

## Подготовка окружения

```bash
# 1) Создать и активировать venv (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip

# 2) Установить зависимости
pip install pytest playwright pytest-playwright python-dotenv psycopg2-binary
python -m playwright install          # (на Windows)
# на Linux/Mac: python -m playwright install --with-deps

Запуск тестов
Все тесты
pytest -q

По директории
pytest tests/ui -q         # только UI
pytest tests/db -q         # только DB

По файлу
pytest tests/ui/test_cart.py -q

По конкретному тесту
pytest tests/ui/test_cart.py::TestCart::test_add_to_cart -q

По маркировкам
pytest -m ui -q            # все UI-тесты
pytest -m smoke -q         # быстрые smoke
pytest -m regression -q    # регрессионные
pytest -m db -q            # тесты БД

С браузером (не headless)
pytest --headed -q

Структура проекта (актуальная)
tests/
  ui/
    pages/                 # Page Object классы
      login_page.py
      products_page.py
      cart_page.py
      checkout_page.py
      menu_page.py
    test_login.py          # тесты логина (позитив/негатив)
    test_cart.py           # тесты корзины
    test_checkout.py       # чекаут
    test_sorting.py        # сортировка
    test_product_details.py# карточка товара (опц.)
    test_menu.py           # logout/reset (опц.)
  db/
    test_db.py             # пример проверки БД
conftest.py                # фикстуры (auth_page, db_conn/db_cur и т.д.)
pytest.ini                 # конфигурация pytest (маркеры/путь к тестам)
resources/
  testdata/                # тестовые данные (если нужны)
.env                       # параметры окружения (не коммитить)

Маркировки

@pytest.mark.ui — все UI-тесты.
@pytest.mark.smoke — быстрые основные проверки (успешный логин, add-to-cart, успешный checkout, сортировка A→Z).
@pytest.mark.regression — расширенный набор (негативы логина, валидации checkout и пр.).
@pytest.mark.db — тесты, требующие подключения к БД.

Примечания

Авторизация в UI выполняется через фикстуру с storage_state (быстро и изолированно для каждого теста).

DB-фикстуры:

db_conn — соединение на сессию.
db_cur — курсор на тест с автоматическим SET search_path TO <DB_SCHEMA>, public.
Если БД иногда недоступна, можно мягко скипать тесты в фикстуре (pytest.skip(...) при OperationalError).