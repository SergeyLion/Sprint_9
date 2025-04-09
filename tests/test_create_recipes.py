import allure
from utilities.data_generator import DataGenerator
from data.data import AuthData as Ad
from pages.create_recipes_page import CreateRecipes
from pages.auth_page import AuthPage
from locators.recipe_card_locators import RecipeCardLocators as Rcdl
from locators.recipes_page_locators import RecipesPageLocators as Rl
from locators.recipe_creation_locators import RecipeCreationLocators as Rcl


@allure.feature("Рецепты")
@allure.story("Создание рецептов")
@allure.severity(allure.severity_level.CRITICAL)
class TestCreateRecipes:

    @allure.title('Создание нового рецепта')
    @allure.description('''
    Тест проверяет функционал создания нового рецепта:
    1. Авторизация пользователя
    2. Создание рецепта с уникальным названием
    3. Добавление ингредиентов
    4. Загрузка изображения
    5. Проверка успешного создания
    ''')
    @allure.tag("smoke", "recipes", "creation")
    def test_create_recipes(self, driver):
        create_recipes = CreateRecipes(driver)
        auth_page = AuthPage(driver)

        with allure.step("Подготовка тестовых данных"):
            comment = DataGenerator.create_random_comment()
            image_path = "data/tortilla_with_cheese.png"
            uid = DataGenerator.generator_uid()
            name_recipes = f"Телячья тортилья {uid}"
            allure.attach(name_recipes, "Уникальное название рецепта", allure.attachment_type.TEXT)
            allure.attach(comment, "Описание рецепта", allure.attachment_type.TEXT)

        with allure.step("Авторизация пользователя"):
            auth_page.open(Ad.URL_AUTH)
            auth_page.auth_login(Ad.AUTH_USERNAME, Ad.AUTH_PASSWORD)
            allure.attach(driver.get_screenshot_as_png(), name="После авторизации",
                          attachment_type=allure.attachment_type.PNG)

        with allure.step("Создание нового рецепта"):
            create_recipes.click_element(Rl.CREATE_RECIPE_LINK)

            with allure.step("Заполнение основных данных"):
                create_recipes.set_input(Rcl.RECIPE_NAME_INPUT, name_recipes)
                create_recipes.click_element(Rcl.TAG_DINNER)
                create_recipes.set_input(Rcl.COOKING_TIME_INPUT, 15)
                create_recipes.set_input(Rcl.DESCRIPTION_TEXTAREA, comment)
                allure.attach(driver.get_screenshot_as_png(), name="Форма заполнена",
                              attachment_type=allure.attachment_type.PNG)

            with allure.step("Добавление ингредиентов"):
                ingredients = [
                    ("телячий фарш   ", 500),
                    ("тортильи   ", 6),
                    ("сыр   ", 30)
                ]
                for name, amount in ingredients:
                    create_recipes.add_ingredient(name, amount)
                    allure.attach(f"{name} - {amount}г", f"Ингредиент добавлен",
                                  attachment_type=allure.attachment_type.TEXT)

            with allure.step("Загрузка изображения"):
                create_recipes.upload_image(Rcl.IMAGE_UPLOAD_INPUT, image_path)

            with allure.step("Отправка формы"):
                create_recipes.click_element(Rcl.SUBMIT_BUTTON)

        with allure.step("Проверка успешного создания"):
            title_recipes_text = create_recipes.get_element_text(Rcdl.RECIPE_TITLE)
            assert uid in title_recipes_text, (
                f"Ожидалось найти ID '{uid}' в названии рецепта, "
                f"но получено: '{title_recipes_text}'"
            )
            allure.attach(driver.get_screenshot_as_png(), name="Созданный рецепт",
                          attachment_type=allure.attachment_type.PNG)