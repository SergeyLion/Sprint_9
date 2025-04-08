import allure
from data.data import AuthData as Ad
from locators.recipes_page_locators import RecipesPageLocators as Rl
from pages.auth_page import AuthPage



@allure.feature("Авторизация")
@allure.story("Страница авторизации пользователя")
class TestAuth:

    @allure.title('Авторизация в Продуктовом помощнике')
    @allure.description('Проходим авторизацию, и проверяем видимость кнопки "Выход"')
    def test_auth_login(self, driver):

        auth_page = AuthPage(driver) # Создаем объект класса страницы Авторизации
        auth_page.open(Ad.URL_AUTH) # Открываем страницу авторизации
        auth_page.auth_login(Ad.AUTH_USERNAME, Ad.AUTH_PASSWORD) #Авторизуемся в Продуктовом помощнике
        #Проверяем отображение кнопки "Выйти"
        assert auth_page.check_is_displayed(Rl.LOGOUT_BUTTON)


