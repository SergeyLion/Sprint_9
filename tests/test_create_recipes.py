import time
import allure
from utilities.data_generator import DataGenerator
from data.data import AuthData as Ad
from pages.create_recipes_page import CreateRecipes
from pages.auth_page import AuthPage
from locators.recipe_card_locators import RecipeCardLocators as Rcdl
from locators.recipes_page_locators import RecipesPageLocators as Rl
from locators.recipe_creation_locators import RecipeCreationLocators as Rcl




@allure.feature("Рецепты")
@allure.story("Страница создание рецептов")
class TestCreateRecipes:

    @allure.title('Создание нового рецепта в Продуктовом помощнике')
    @allure.description('Создаем новый рецепт и проверяем успешность создания')
    def test_create_recipes(self, driver):
        create_recipes = CreateRecipes(driver)
        auth_page = AuthPage(driver)

        # Генерация тестовых данных
        comment = DataGenerator.create_random_comment()
        image_path = "data/tortilla_with_cheese.png"  # Относительный путь от корня проекта
        uid = DataGenerator.generator_uid()
        name_recipes = f"Телячья тортилья {uid}"

        with allure.step("Авторизация пользователя"):
            auth_page.open(Ad.URL_AUTH)
            auth_page.auth_login(Ad.AUTH_USERNAME, Ad.AUTH_PASSWORD)

        with allure.step("Создание нового рецепта"):
            create_recipes.click_element(Rl.CREATE_RECIPE_LINK)
            create_recipes.set_input(Rcl.RECIPE_NAME_INPUT, name_recipes)
            create_recipes.click_element(Rcl.TAG_DINNER)

            # Добавление ингредиентов
            ingredients = [
                ("телячий фарш", 500),
                ("тортильи", 6),
                ("сыр", 30)
            ]
            for name, amount in ingredients:
                create_recipes.add_ingredient(name, amount)

            create_recipes.set_input(Rcl.COOKING_TIME_INPUT, 15)
            create_recipes.set_input(Rcl.DESCRIPTION_TEXTAREA, comment)
            create_recipes.upload_image(Rcl.IMAGE_UPLOAD_INPUT, image_path)
            create_recipes.click_element(Rcl.SUBMIT_BUTTON)

        with allure.step("Проверка успешного создания рецепта"):
            title_recipes = create_recipes.find_element(Rcdl.RECIPE_TITLE)
            assert uid in title_recipes.text