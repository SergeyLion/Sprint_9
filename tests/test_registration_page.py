import allure
from data.data import AuthData as Ad
from pages.registration_page import RegistrationPage
from locators.auth_page_locators import AuthLocators as Al
from utilities.data_generator import DataGenerator



@allure.feature("Авторизация")
@allure.story("Страница регистрации пользователя")
class TestRegistration:

    @allure.title('Регистрация пользователя в Продуктовом помощнике')
    @allure.description('Проходим регистрацию, и проверяем отображение формы Авторизации')
    def test_registration_user(self, driver):

        registration_page = RegistrationPage(driver) # Создаем объект класса страницы Регистрация
        fake_user = DataGenerator.create_fake_user()
        registration_page.open(Ad.URL_AUTH) # Открываем страницу авторизации
        registration_page.click_element(Al.SIGNUP_BUTTON) # Переходим на страницу "Создать аккаунт"
        registration_page.register_new_user(fake_user) # Регистрируем нового пользователя
        #Проверяем отображение кнопки "Выйти"
        assert registration_page.check_is_displayed(Al.FORM_TITLE)