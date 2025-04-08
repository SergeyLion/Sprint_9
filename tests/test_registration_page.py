import allure
from data.data import AuthData as Ad
from pages.registration_page import RegistrationPage
from locators.auth_page_locators import AuthLocators as Al
from utilities.data_generator import DataGenerator


@allure.feature("Авторизация")
@allure.story("Страница регистрации пользователя")
@allure.severity(allure.severity_level.CRITICAL)
class TestRegistration:

    @allure.title('Регистрация нового пользователя в Продуктовом помощнике')
    @allure.description('''
    Проверка успешной регистрации пользователя:
    1. Открываем страницу авторизации
    2. Переходим на страницу регистрации
    3. Заполняем форму регистрации тестовыми данными
    4. Проверяем отображение формы авторизации
    ''')
    @allure.tag("regression", "registration")
    def test_registration_user(self, driver):
        with allure.step("Инициализация страницы регистрации"):
            registration_page = RegistrationPage(driver)

        with allure.step("Генерация тестовых данных пользователя"):
            fake_user = DataGenerator.create_fake_user()

        with allure.step("Открытие страницы авторизации"):
            registration_page.open(Ad.URL_AUTH)

        with allure.step("Переход на страницу регистрации"):
            registration_page.click_element(Al.SIGNUP_BUTTON)

        with allure.step("Заполнение формы регистрации"):
            registration_page.register_new_user(fake_user)

        with allure.step("Проверка успешной регистрации"):
            assert registration_page.check_is_displayed(
                Al.FORM_TITLE), "Форма авторизации не отображается после регистрации"