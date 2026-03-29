import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step('Обнаружение элемента страницы')
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @staticmethod
    @allure.step('Форматирование локатора с подстановкой значения')
    def format_locator(locator, value):
        return locator[0], locator[1].format(value)

    @allure.step('Клик по элементу страницы')
    def click_to_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Ввод текста в поле')
    def text_input_to_element(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Получение текста элемента')
    def get_text_from_element(self, locator):
        return self.find_element(locator).text

    @allure.step('Скролл страницы к необходимому элементу')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание URL, содержащего "{value}"')
    def wait_for_url_contains(self, value):
        return self.wait.until(EC.url_contains(value))

    @allure.step('Переключение на вкладку с индексом {tab_number}')
    def change_browser_tab(self, tab_number):
        self.driver.switch_to.window(self.driver.window_handles[tab_number])