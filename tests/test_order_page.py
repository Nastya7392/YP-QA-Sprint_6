import pytest
import allure
import src.data as data
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.suite('Тесты страницы заказа аренды сервиса "Яндекс Самокат"')
class TestOrderPage:
    @allure.title('Создание заказа с разными точками входа и наборами данных')
    @pytest.mark.parametrize(
        'entry_point, user_info, rent_info',
        [
            ('header', data.user_info_1, data.rent_info_1),
            ('content', data.user_info_2, data.rent_info_2),
        ],
    )
    def test_make_order(self, driver, entry_point, user_info, rent_info):
        main_page = MainPage(driver)
        if entry_point == 'header':
            main_page.open_user_info_form_by_header_button()
        else:
            main_page.open_user_info_form_by_content_button()

        order_page = OrderPage(driver)
        order_page.wait_user_info_form()
        order_page.fill_user_info_form(user_info)
        assert order_page.get_rent_info_header().text == data.order_form_rent_info_header_text

        order_page.fill_rent_info_form(rent_info)
        order_page.click_order_finish_button()
        order_page.confirm_rent()
        assert data.order_form_finish_header_text in order_page.get_order_info_header().text
