# Sprint_9

## Описание
Этот проект представляет собой набор тестов для сайта "Продуктовый помощник":
- Авторизация
- Регистрация
- Создание рецепта
  

## Инструкция по настройке и запуску тестов:

   
1. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt

2. **Запуск тестов:**

   2.1. Запуск тестов PMS:
   ```bash
   pytest tests/ -n auto
   ```
   
3. **Открыть отчет allure:**

   3.1. Для Windows:
   ```bash
   allure serve .\reports\allure_results
   ```
   
   3.2. Для macOS/ubuntu/linux:
   ```bash
   allure serve reports/allure_results/
   ```
   