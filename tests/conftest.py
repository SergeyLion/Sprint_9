import pytest
from selenium import webdriver
import allure
import tempfile



@pytest.fixture
def driver():
    """Фикстура для создания драйвера Chrome в headless-режиме."""
    with allure.step("Создаём драйвер Chrome в headless-режиме"):
        chrome_options = webdriver.ChromeOptions()  # создали объект для опций
        chrome_options.add_argument('--headless')  # добавили настройку
        chrome_options.add_argument('--no-sandbox')  # добавили настройку
        chrome_options.add_argument('--disable-dev-shm-usage')  # добавили настройку
        chrome_options.add_argument(f'--user-data-dir={tempfile.mkdtemp()}')
        driver = webdriver.Chrome(options=chrome_options)  # создали драйвер и передали в него настройки
        driver.set_window_size(1920, 1080)
        yield driver
        driver.quit()

