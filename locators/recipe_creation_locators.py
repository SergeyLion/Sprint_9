from selenium.webdriver.common.by import By


class RecipeCreationLocators:
    # Заголовок формы
    FORM_TITLE = (By.XPATH, "//h1[@class='styles_title__2fhty' and text()='Создание рецепта']")

    # Основные поля
    RECIPE_NAME_INPUT = (By.XPATH, "//input[contains(@class, 'styles_inputField__3eqTj') and preceding-sibling::div[text()='Название рецепта']]")
    COOKING_TIME_INPUT = (By.XPATH, "//input[contains(@class, 'styles_inputField__3eqTj') and preceding-sibling::div[contains(text(), 'Время приготовления')]]")
    DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[contains(@class, 'styles_textareaField__1wfhC')]")

    # Теги рецепта
    TAG_BREAKFAST = (By.XPATH, "//button[contains(@class, 'styles_checkbox__1WBUC') and following-sibling::span[text()='Завтрак']]")
    TAG_LUNCH = (By.XPATH, "//button[contains(@class, 'styles_checkbox__1WBUC') and following-sibling::span[text()='Обед']]")
    TAG_DINNER = (By.XPATH, "//button[contains(@class, 'styles_checkbox__1WBUC') and following-sibling::span[text()='Ужин']]")

    # Ингредиенты
    INGREDIENT_INPUT = (By.XPATH, "//input[contains(@class, 'styles_ingredientsInput__1zzql')]")
    INGREDIENTS_DROPDOWN = (By.XPATH, "//div[contains(@class, 'styles_container__3ukwm')]/div") # Список ингредиентов
    INGREDIENT_DROPDOWN_ITEM = (By.XPATH, "//div[contains(@class, 'styles_container__3ukwm')]/div")
    INGREDIENT_AMOUNT_INPUT = (By.XPATH, "//input[contains(@class, 'styles_ingredientsAmountValue__2matT')]")
    ADD_INGREDIENT_BUTTON = (By.XPATH, "//div[contains(@class, 'styles_ingredientAdd__3fc32') and text()='Добавить ингредиент']")

    # Загрузка изображения
    IMAGE_UPLOAD_INPUT = (By.XPATH, "//input[@type='file' and contains(@class, 'styles_fileInput')]")
    IMAGE_UPLOAD_BUTTON = (By.XPATH, "//div[contains(@class, 'styles_button__xzu5F') and text()='Выбрать файл']")

    # Кнопка создания рецепта
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class, 'styles_button__f_Q9Z') and contains(text(), 'Создать рецепт')]")

    # Добавленные ингредиенты
    ADDED_INGREDIENTS = (By.XPATH, "//div[contains(@class, 'styles_ingredientsAdded__35vNf')]//div[contains(@class, 'styles_ingredientItem__')]")