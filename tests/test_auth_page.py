import allure
from data.data import AuthData as Ad
from locators.recipes_page_locators import RecipesPageLocators as Rl
from pages.auth_page import AuthPage


@allure.feature("Авторизация")
@allure.story("Страница авторизации пользователя")
@allure.severity(allure.severity_level.CRITICAL)
class TestAuth:

    @allure.title('Авторизация в Продуктовом помощнике')
    @allure.description('''
    Проверка успешной авторизации пользователя:
    1. Открываем страницу авторизации
    2. Вводим валидные учетные данные
    3. Проверяем отображение кнопки "Выход"
    ''')
    @allure.tag("smoke", "auth")
    def test_auth_login(self, driver):
        with allure.step("Инициализация страницы авторизации"):
            auth_page = AuthPage(driver)

        with allure.step("Открытие страницы авторизации"):
            auth_page.open(Ad.URL_AUTH)

        with allure.step("Ввод учетных данных и авторизация"):
            auth_page.auth_login(Ad.AUTH_USERNAME, Ad.AUTH_PASSWORD)

        with allure.step("Проверка успешной авторизации"):
            assert auth_page.check_is_displayed(Rl.LOGOUT_BUTTON), "Кнопка 'Выход' не отображается после авторизации"