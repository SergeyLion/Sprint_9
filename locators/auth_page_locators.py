from selenium.webdriver.common.by import By


class AuthLocators:
    # Навигация
    RECIPES_LINK = (By.XPATH, "//a[@href='/recipes']")
    SIGNIN_LINK = (By.XPATH, "//a[@href='/signin']")
    SIGNUP_BUTTON = (By.XPATH, "//a[@href='/signup']")

    # Форма авторизации
    FORM_TITLE = (By.XPATH, "//h1[contains(@class, 'styles_title')]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'style_button') and contains(text(), 'Войти')]")
