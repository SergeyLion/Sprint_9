from selenium.webdriver.common.by import By


class RecipeCardLocators:
    # Заголовок рецепта
    RECIPE_TITLE = (By.XPATH, "//h1[contains(@class, 'styles_single-card')]")
