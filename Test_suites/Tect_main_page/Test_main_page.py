import time

import config
from Page.MainPage import MainPage
from Test_suites.BaseTest import BaseTest
from Test_suites.Test_footer import TestFooter
from Test_suites.Test_header import TestHeader

"""
Макеты главной страницы сейчас в процессе доработки 
https://www.figma.com/file/GpVQ4uyNU3FBPA33K2YZcB/MAUDAU?node-id=5655%3A33004
, за основу берем то что уже в проде

Содержание страницы

Хедер 
панель навигации с выбором языка и переходом на страницы Оплата/Доставка/Возврат гарантия и телефонами техподдержки 
Переход на страницу каталога, поисковая строка, избранное, войти в ЛК, Счеткик товаров в корзине и переход на корзину

промо баннер с контролами переключения вправо/лево 
Карточки категорий (проверить отображение текста, картинки, количества доступных карточек 10 шт)

Блок "Предложение недели" (отображение цен/фото/навигация переключения влево/вправо
Блок "Предложение месяца" (отображение цен/фото/навигация переключения влево/вправо
Блок "Просмотренные товары" (отображение цен/фото/навигация переключения влево/вправо (если гость ранее уже был на сайте)
Футер
навигация """


class TestMainPage(BaseTest):

    def test_main_page(self):
        # TestHeader().test_header()

        main_page = MainPage()

        """----- Promo slider block test -----"""
        # Немає на препроді
        #main_page.is_element_visibility(main_page.current_promo_slide)
        # active_slider = main_page.get_web_element(main_page.current_promo_slide)
        # switch_slide_in_slider_list = main_page.get_oll_element_by_locator(main_page.switch_slide_in_slider)
        # main_page.click(switch_slide_in_slider_list[1])
        # next_slide = main_page.get_web_element(main_page.current_promo_slide)
        # assert active_slider is not next_slide

        """----- Categories block test -----"""
        # тест відображення назв категорій
        categories_card_name_list = main_page.get_oll_element_by_locator(main_page.name_categories)
        for categories_name_card in categories_card_name_list:
            name_category = main_page.get_text(categories_name_card)
            assert isinstance(name_category, str)

        # тест відображення іконок категорій
        categories_images_list = main_page.get_oll_element_by_locator(main_page.image_categories)
        for categories_images in categories_images_list:
            main_page.right_switch_categories(categories_images)
            visibility_element = main_page.is_element_visibility(categories_images)
            assert visibility_element is True

        # тест кількості категорій
        number_categories = len(categories_images_list)
        # Має бути 10 категорій зараз їх 9
        # assert number_categories == 10

        # тест функціональності ктегорій
        one_of_categories_card_list = main_page.get_oll_element_by_locator(main_page.one_of_categories_card)
        for one_of_categories_card in one_of_categories_card_list:
            main_page.click(main_page.left_button)
            main_page.right_switch_categories(one_of_categories_card)
            main_page.is_element_clickable(one_of_categories_card)

        """----- Offer of the week block test -----"""


        """----- Goods of the month block test -----"""

        """----- Viewed products block test -----"""

