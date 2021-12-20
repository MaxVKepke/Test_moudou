from selenium.webdriver.common.by import By

from Page.BasePage import BasePage
import re

from Page.Header import Header


class StuffPage(BasePage):
    count_stuff = (By.CSS_SELECTOR, 'span.products-count')

    product_page = (By.CSS_SELECTOR, 'div.product-listing div.product')

    pagination = (By.CSS_SELECTOR, 'ul.flex.pagination-list li')

    def get_value_from_count_stuff(self):
        text_from_count = self.get_text(self.count_stuff)
        pat = '\d+'
        value = re.search(pat, text_from_count)
        number = int(value.group(0))
        return number

    def save_value_in_stuff_count_end_compare_number_ua_end_ru_loc(self):
        header_block = Header()

        self.is_element_visibility(self.count_stuff)
        number_stuff_in_count_ua_loc = self.get_value_from_count_stuff()

        header_block.click(header_block.ru_localization_button)
        self.is_element_visibility(self.count_stuff)
        number_stuff_in_count_ru_loc = self.get_value_from_count_stuff()

        assert number_stuff_in_count_ua_loc == number_stuff_in_count_ru_loc

    def compare_number_of_goods_in_categories(self):
        stuff_page = StuffPage()
        # 1. отримати list товарів на першій сторінці пагінації
        products_list_on_one_page = self.get_oll_element_by_locator(stuff_page.product_page)

        # 2. порахувати кількість(len list) товарів на першій сторінці пагінації
        oll_product_on_one_page_ru = len(products_list_on_one_page)
        number_of_product_on_one_page_ru = int(oll_product_on_one_page_ru)

        # 3. отримати кількість сторінок пагінації - 1 сторінка
        list_pagination_page_ru = self.get_oll_element_by_locator(stuff_page.pagination)
        last_element_pagination_ru = list_pagination_page_ru[-1]
        oll_number_pagination_ru = last_element_pagination_ru.text
        number_pagination_minus_one_ru = (int(oll_number_pagination_ru) - 1)

        # 4. отримати list товарів на останій сторінці пагінації
        list_pagination_page_ru = self.get_oll_element_by_locator(stuff_page.pagination)
        stuff_page.click(list_pagination_page_ru[-1])
        list_products_on_lost_pagination_page_ru = self.get_oll_element_by_locator(stuff_page.product_page)

        # 5. порахувати кількість(len list) товарів на останій сторінці пагінації
        oll_products_on_last_page_ru = len(list_products_on_lost_pagination_page_ru)
        number_products_on_last_page_ru = (int(oll_products_on_last_page_ru))

        # 6. порахувати кількість товарів на всіх сторінках пагінації, крім останьої
        number_products_on_oll_pagination_page_except_last_page_ru = number_of_product_on_one_page_ru * number_pagination_minus_one_ru

        # 7. до кількості товарів з кроку 6 додати товари з останьої сторінки
        oll_number_product = number_products_on_oll_pagination_page_except_last_page_ru + number_products_on_last_page_ru

        return oll_number_product