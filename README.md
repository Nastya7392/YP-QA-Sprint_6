# Sprint\_6

## Финальный проект 6 спринта

<hr>

## <h>Project: Яндекс.Самокат</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты и записать отчет:</h>

> pytest --alluredir=./allure-results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve ./allure-results



<hr>

<h3 align="left" style="color:yellow">Project files and description:</h3>

|Название файла|Содержание файла|
|-|-|
|allure-results.dir|Папка с отчетами Allure|
|locators|Директория с локаторами|
|main\_page\_locators.py|Локаторы главной страницы Я.Самокат|
|order\_form\_page\_one\_locators.py|Локаторы первой страницы формы заказа Самоката|
|order\_form\_page\_two\_locators.py|Локаторы второй страницы формы заказа Самоката|
|transition\_locators.py|Локаторы для перехода на веб-страницы|
|pages|Директория с page objects|
|main\_page.py|Главные методы работы с элементами на странице|
|main\_page\_check\_key\_questions\_section.py|Методы для проверки текста ответов на "Вопросы о важном"|
|order\_form\_page\_one.py|Методы для первой страницы оформления заказа|
|order\_form\_page\_two.py|Методы для второй страницы оформления заказа|
|transitions.py|Методы для редиректов|
|tests|Директория с тестами|
|conftest.py|Фикстуры|
|test\_first\_set\_of\_data.py|Тесты c первым набором данных|
|test\_key\_questions.py|Тесты на проверку текста в ответах раздела "Вопросы о важном"|
|test\_second\_set\_of\_data.py|Тесты со вторым набором данных|
|curl.py|Файл с url-ами|
|data.py|Файл с тестовыми данными|
|helpers.py|Хэлперы для тестов|
|README.md|README-файл|
|requirements.txt|Файл с зависимостями|



