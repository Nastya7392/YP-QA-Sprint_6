import allure
import src.data as data
import src.urls as urls
from pages.main_page import MainPage
from pages.redirect_page import RedirectPage


@allure.suite('Тесты переходов по ссылкам в верхнем меню')
class TestTransitionPage:

    @allure.title('Переход на главную страницу по логотипу "Самокат"')
    def test_transition_by_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_order_page()

        redirect_page = RedirectPage(driver)
        redirect_page.go_to_main_page_by_scooter_logo()

        assert data.scooter_header in main_page.get_main_header_text()

    @allure.title('Переход на страницу Дзена по логотипу "Яндекс"')
    def test_transition_by_yandex_logo(self, driver):
        redirect_page = RedirectPage(driver)
        redirect_page.go_to_dzen_by_yandex_logo()

        assert redirect_page.wait_dzen_page(urls.DZEN_DOMAIN)