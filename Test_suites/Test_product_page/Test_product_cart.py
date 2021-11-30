import time

from Page.Header import Header
from Page.ProductPage import ProductPage
from Test_suites.BaseTest import BaseTest


class TestProductCart(BaseTest):
    def test_product_cart(self):
        rout_on_product_page = '/pazl-avenir-yedynorih-28-elementiv-pz195051-md-98243.html'
        self.add_rout_in_url_and_go_to_url(rout_on_product_page)

        product_page = ProductPage()

        """Test breadcrumbs """
        product_page.is_element_visible(product_page.breadcrumbs_desktop)
        # product_page.click(product_page.children_goods)

        product_page.wait_until_url_changes_after_click(product_page.children_goods)
        get_url_after_click_on_breadcrumbs = product_page.get_current_url()

        assert '/ditjachi-tovari' in get_url_after_click_on_breadcrumbs

        self.add_rout_in_url_and_go_to_url(rout_on_product_page)

        """ Test product cart"""
        product_page.is_element_visible(product_page.image_product)
        # product_page.is_element_visible(product_page.product_gallery)
        product_page.is_element_visible(product_page.name_product)
        product_page.is_element_visible(product_page.reviews_stars)
        product_page.click(product_page.reviews)
        product_page.is_element_visible(product_page.add_reviews_popup)

        close_reviews = product_page.close_reviews_button
        product_page.is_element_visible(close_reviews)
        product_page.click(close_reviews)

        product_page.is_element_visible(product_page.product_article)
        product_page.is_element_visible(product_page.character)
        product_page.is_element_visible(product_page.some_product_attribute)
        product_page.is_element_clickable(product_page.character)
        product_page.click(product_page.oll_character_button)
        product_page.is_element_visibility(product_page.oll_character)

        product_page.scroll_page_into_element(product_page.breadcrumbs_desktop)

        """ Test price block """
        product_page.is_element_visible(product_page.availability)

        product_page.is_element_visible(product_page.old_price)
        product_page.is_element_visible(product_page.discount)
        product_page.is_element_visible(product_page.price_hot)

        points = product_page.points
        product_page.is_element_visibility(points)

        product_page.click(points)
        product_page.is_element_visible(product_page.point_details_popup)

        add_to_basket_button = product_page.add_to_basket_button
        product_page.click(add_to_basket_button)
        product_page.check_is_element_invisible(product_page.add_to_basket_button)
        header_block = Header()
        value_in_basket_count = product_page.get_text(header_block.basket_counter)
        assert int(value_in_basket_count) == 1, \
            """Value on the basket in basket count"""

        """ Test delivery block """
        # product_page.is_element_visibility(product_page.delivery)
        # product_page.is_element_visibility(product_page.one_of_shipping)

        """ Test similar products """
        similar_products = product_page.similar_products
        product_page.is_element_visibility(similar_products)
        list_similar_products = product_page.check_are_all_elements_present(product_page.some_of_similar_products)
        assert len(list_similar_products) != 0, \
            """No similar product"""

        product_page.is_element_visibility(product_page.image_similar_products)
        product_page.is_element_visibility(product_page.name_similar_products)
        product_page.is_element_visibility(product_page.old_price_similar_products)
        product_page.is_element_visibility(product_page.price_similar_products)

        """ Test detail attribute products """

        product_page.is_element_visibility(product_page.reviews_products)
        product_page.click(product_page.add_reviews_button)
        close_reviews = product_page.close_reviews_button
        product_page.scroll_page_into_element(close_reviews)
        product_page.is_element_visibility(close_reviews)
        product_page.click(close_reviews)

        """ Test reviewed products """
        one_of_reviewed_product_cart = product_page.some_reviewed_product_cart
        product_page.scroll_page_into_element(one_of_reviewed_product_cart)
        product_page.is_element_visibility(one_of_reviewed_product_cart)
        product_page.is_element_visibility(product_page.some_image_reviewed_product)
        product_page.is_element_visibility(product_page.some_name_reviewed_product)
        product_page.is_element_visibility(product_page.some_old_price_reviewed_product)
        product_page.is_element_visibility(product_page.some_hot_price_reviewed_product)

        one_of_button_add_cart = product_page.some_button_add_cart
        product_page.scroll_page_into_element(one_of_button_add_cart)

        product_page.click(product_page.some_minus_count_on_basket)
        product_page.click(one_of_button_add_cart)
        product_page.is_element_visibility(product_page.counter_product_basket)


