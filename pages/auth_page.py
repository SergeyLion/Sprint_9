import allure
from pages.base_page import BasePage
from locators.auth_page_locators import AuthLocators as Al



class AuthPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Авторизуемся на сайте "Продуктовый помощник" ')
    def auth_login(self, user_email, user_password):
        self.set_input(Al.EMAIL_INPUT , user_email)
        self.set_input(Al.PASSWORD_INPUT, user_password)
        self.click_element(Al.SUBMIT_BUTTON)

