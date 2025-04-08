from selenium.webdriver.common.by import By


class AuthLocators:
    # Меню и навигация
    MENU_BUTTON = (By.XPATH, "//div[@class='styles_menuButton__zn68y']/img")
    RECIPES_LINK = (By.XPATH, "//a[@href='/recipes']")
    SIGNIN_LINK = (By.XPATH, "//a[@href='/signin']")
    SIGNUP_BUTTON = (By.XPATH, "//a[@href='/signup']")

    # Форма авторизации
    FORM_TITLE = (By.XPATH, "//h1[@class='styles_title__2fhty']")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'style_button__1FFWl') and contains(text(), 'Войти')]")

    # Футер
    FOOTER_BRAND = (By.XPATH, "//a[@class='style_link__1kPh8 style_footer__brand__3KdCB']")