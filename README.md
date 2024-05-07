# Diplom_3
Third task of diploma on "Python QA automation" course

Structure:
Diplom_3/
├-locators - Наборы локаторов
│  ├-base_page_locators.py - Локаторы header
│  ├-feed_page_locators.py - Локаторы страницы Лента заказов
│  ├-login_account_page_locators.py - Локаторы страниц Логин и Аккаунт
│  └-main_page_locators.py - Локаторы главной страницы
├-pages - Наборы методов страниц
│  ├-base_page.py - Базовые методы
│  ├-feed_page.py - Методы страницы Лента заказов
│  ├-login_account_page.py - Методы страниц Аккаунт и Логин
│  └-main_page.py - Методы главной страницы
├-tests - Наборы проверок по страницам
│  ├-test_feed_page.py - Проверки страницы Лента заказов
│  ├-test_login_account_page.py - Проверки сстраниц Логин и Аккаунт
│  └-test_main_page.py - Проверки главной страницы
├-data.py - Ccылки на страницы тестируемого ресурса
├-allure_results - Отчёты о тестах
├-conftest.py - Фикстуры
├-README.md - Этот файл
└-requirements.txt - Внешние зависимости

Для запуска проекта понадобятся IDE для Python и библиотеки, перечисленные в файле requirements.txt
