import pytest
import os
import psycopg2
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, expect
from tests.UI.pages.login_page import LoginPage

load_dotenv()

SWAG_URL = "https://www.saucedemo.com/"
AUTH_STATE = "auth.json"



@pytest.fixture(scope="session")
def pw_browser(request):
    headed = bool(getattr(request.config, "getoption", lambda *a, **k: False)("--headed"))
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed)
        yield browser
        browser.close()

@pytest.fixture(scope="session", autouse=True)
def prepare_auth_state(pw_browser):
    """
    1 раз за сессию логинимся и сохраняем storage_state в файл.
    """
    username = os.getenv("WEB_LOGIN")
    password = os.getenv("WEB_PASSWORD")

    if not username or not password:
        pytest.fail("Не заданы WEB_LOGIN/WEB_PASSWORD в .env или в окружении")

    context = pw_browser.new_context()
    page = context.new_page()
    lp = LoginPage(page)
    lp.open()
    lp.login(username, password)
    expect(page.locator('[data-test="title"]')).to_have_text("Products")
    context.storage_state(path=AUTH_STATE)
    context.close()

@pytest.fixture()
def auth_page(pw_browser):
    """
    Для КАЖДОГО теста создаём новый контекст/страницу с готовой авторизацией.
    """
    context = pw_browser.new_context(storage_state=AUTH_STATE)
    page = context.new_page()
    page.goto(f"{SWAG_URL}inventory.html")
    yield page
    context.close()

# ДЛЯ БД
# грузим .env один раз на сессию
load_dotenv(override=False)

def _db_params():
    return dict(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "5432")),
        dbname=os.getenv("DB_NAME", "postgres"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", ""),
    )

@pytest.fixture(scope="session")
def db_conn():
    """Подключение к Postgres на всю сессию."""
    params = _db_params()
    conn = psycopg2.connect(**params)
    conn.autocommit = True  # чтобы не ловить висящие транзакции в простых селектах
    yield conn
    conn.close()

@pytest.fixture()
def db_cur(db_conn):
    """Курсор на тест + установка search_path из ENV (DB_SCHEMA, public)."""
    schema = os.getenv("DB_SCHEMA", "public")
    cur = db_conn.cursor()
    cur.execute("SET search_path TO %s, public", (schema,))
    try:
        yield cur
    finally:
        cur.close()