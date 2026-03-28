import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    @allure.step('Обнаружение элемента страницы')
    def find_element(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    @staticmethod
    @allure.step('Форматирование локатора с подстановкой значения')
    def format_locator(locator, value):
        return locator[0], locator[1].format(value)

    @allure.step('Клик по элементу страницы')
    def click_to_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

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
        self.driver.execute_script('arguments[0].scrollIntoView();', self.driver.find_element(*locator))

    @allure.step('Переключение на новую вкладку')
    def switch_to_new_tab(self, tabs_count_before_click):
        self.wait.until(lambda driver: len(driver.window_handles) > tabs_count_before_click)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидание перехода на внешний сервис')
    def wait_for_external_url(self, domains, timeout=60):
        wait = WebDriverWait(self.driver, timeout)

        def _predicate(driver):
            current_url = (driver.current_url or '').lower()
            title = (driver.title or '').lower()
            if any(domain.lower() in current_url for domain in domains):
                return True
            if 'dzen' in title or 'дзен' in title:
                return True
            return len(driver.window_handles) > 1 and current_url not in ('', 'about:blank') and 'qa-scooter.praktikum-services.ru' not in current_url

        return wait.until(_predicate)
