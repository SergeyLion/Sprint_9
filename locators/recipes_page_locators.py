from selenium.webdriver.common.by import By


class RecipesPageLocators:
    #Навигация
    RECIPES_LINK = (By.XPATH, "//a[@href='/recipes' and @aria-current='page']")
    SUBSCRIPTIONS_LINK = (By.XPATH, "//a[@href='/subscriptions']")
    CREATE_RECIPE_LINK = (By.XPATH, "//a[@href='/recipes/create']")
    FAVORITES_LINK = (By.XPATH, "//a[@href='/favorites']")
    CART_LINK = (By.XPATH, "//a[@href='/cart']")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(@class, 'styles_menuLink') and text()='Выход']")
