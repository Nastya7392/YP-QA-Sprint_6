import allure
import locators.redirect_page_locators as locators
from pages.base_page import BasePage


class RedirectPage(BasePage):

    @allure.step('Переходим на главную страницу через логотип "Самокат"')
    def go_to_main_page_by_scooter_logo(self):
        self.click_to_element(locators.SCOOTER_LOGO)

    @allure.step('Переход на Дзен через логотип "Яндекс"')
    def go_to_dzen_by_yandex_logo(self):
        current_tabs = len(self.driver.window_handles)
        self.click_to_element(locators.YANDEX_LOGO)
        self.wait.until(lambda driver: len(driver.window_handles) > current_tabs)
        self.change_browser_tab(-1)

    @allure.step('Ожидание загрузки страницы Дзена')
    def wait_dzen_page(self, domain):
        return self.wait_for_url_contains(domain)