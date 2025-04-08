from selenium.webdriver.common.by import By


class RecipesPageLocators:
    # Меню и навигация
    MENU_BUTTON = (By.XPATH, "//div[@class='styles_menuButton__zn68y']/img")
    RECIPES_LINK = (By.XPATH, "//a[@href='/recipes' and @aria-current='page']")
    SUBSCRIPTIONS_LINK = (By.XPATH, "//a[@href='/subscriptions']")
    CREATE_RECIPE_LINK = (By.XPATH, "//a[@href='/recipes/create']")
    FAVORITES_LINK = (By.XPATH, "//a[@href='/favorites']")
    CART_LINK = (By.XPATH, "//a[@href='/cart']")
    CHANGE_PASSWORD_LINK = (By.XPATH, "//a[@href='/change-password']")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(@class, 'styles_menuLink__3a59I') and text()='Выход']")

    # Заголовок и фильтры
    PAGE_TITLE = (By.XPATH, "//h1[@class='styles_title__2fhty']")
    BREAKFAST_FILTER = (By.XPATH, "//button[contains(@class, 'styles_checkbox__1WBUC') and following-sibling::span[text()='Завтрак']]")
    LUNCH_FILTER = (By.XPATH, "//button[contains(@class, 'styles_checkbox__1WBUC') and following-sibling::span[text()='Обед']]")
    DINNER_FILTER = (By.XPATH, "//button[contains(@class, 'styles_checkbox__1WBUC') and following-sibling::span[text()='Ужин']]")

    # Карточки рецептов (общие локаторы для всех карточек)
    RECIPE_CARDS = (By.XPATH, "//div[@class='style_card__1Le2w']")
    RECIPE_IMAGE = (By.XPATH, ".//div[contains(@class, 'style_card__image__3xIhV')]")
    RECIPE_TITLE = (By.XPATH, ".//a[contains(@class, 'style_card__title__1iaT0')]")
    RECIPE_TAGS = (By.XPATH, ".//div[@class='styles_tag__3GiD4']")
    RECIPE_TIME = (By.XPATH, ".//div[@class='style_card__time__1OSq7']")
    RECIPE_AUTHOR = (By.XPATH, ".//div[@class='style_card__author__TN_1Q']/a")
    ADD_TO_CART_BUTTON = (By.XPATH, ".//button[contains(@class, 'style_card__add__2nn9l')]")
    FAVORITE_BUTTON = (By.XPATH, ".//button[contains(@class, 'style_button_style_none__3iQIz')]")

    # Пагинация
    PAGINATION = (By.XPATH, "//div[@class='styles_pagination__5PNtl']")
    PREV_PAGE = (By.XPATH, "//img[contains(@class, 'styles_arrowLeft__1uUAX')]")
    NEXT_PAGE = (By.XPATH, "//img[contains(@class, 'styles_arrowRight__358Cq')]")
    PAGE_NUMBER = (By.XPATH, "//div[contains(@class, 'styles_paginationItem__vduM0')]")

    # Футер
    FOOTER_BRAND = (By.XPATH, "//a[@class='style_link__1kPh8 style_footer__brand__3KdCB']")