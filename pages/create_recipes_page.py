import time
from time import sleep

import allure
from pages.base_page import BasePage
from locators.recipe_creation_locators import RecipeCreationLocators as Rcl



class CreateRecipes(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Добавляем ингредиенты ')
    def add_ingredient(self, name_ingredient, amount):
        self.set_input(Rcl.INGREDIENT_INPUT, name_ingredient)
        self.click_element_js(Rcl.INGREDIENTS_DROPDOWN)
        self.set_input(Rcl.INGREDIENT_AMOUNT_INPUT, amount)
        self.click_element(Rcl.ADD_INGREDIENT_BUTTON)




