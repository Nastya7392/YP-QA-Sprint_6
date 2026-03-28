import allure
import locators.redirect_page_locators as locators
from pages.base_page import BasePage


class RedirectPage(BasePage):
    @allure.step('Переход на главную страницу через логотип "Самокат"')
    def go_to_main_page_by_scooter_logo(self):
        self.click_to_element(locators.SCOOTER_LOGO)

    @allure.step('Переход на внешний сервис через логотип "Яндекс"')
    def go_to_dzen_by_yandex_logo(self):
        tabs_count = len(self.driver.window_handles)
        self.click_to_element(locators.YANDEX_LOGO)
        self.switch_to_new_tab(tabs_count)

    @allure.step('Ожидание открытия внешней страницы')
    def wait_dzen_page(self, domains):
        return self.wait_for_external_url(domains)
