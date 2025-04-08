import allure
from pages.base_page import BasePage
from locators.registration_page_locators import RegistrationLocators as Rl




class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def register_new_user(self, user_data):
        self.set_input(Rl.FIRST_NAME_INPUT, user_data["first_name"])
        self.set_input(Rl.LAST_NAME_INPUT, user_data["last_name"])
        self.set_input(Rl.USERNAME_INPUT, user_data["user_name"])
        self.set_input(Rl.EMAIL_INPUT, user_data["email"])
        self.set_input(Rl.PASSWORD_INPUT, user_data["password"])
        self.click_element(Rl.SUBMIT_BUTTON) # Нажимаем на кнопку "Создать аккаунт" в форме регистрации




