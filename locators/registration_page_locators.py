from selenium.webdriver.common.by import By


class RegistrationLocators:
    # Заголовок формы
    REGISTRATION_TITLE = (By.XPATH, "//h1[@class='styles_title__2fhty' and text()='Регистрация']")

    # Поля формы
    FIRST_NAME_INPUT = (By.XPATH, "//input[@name='first_name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@name='last_name']")
    USERNAME_INPUT = (By.XPATH, "//input[@name='username']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")

    # Кнопка отправки формы
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'styles_button__146Sy') and contains(text(), 'Создать аккаунт')]")
