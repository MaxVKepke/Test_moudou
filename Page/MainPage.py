from selenium.webdriver.common.by import By

from Page.BasePage import BasePage


class MainPage(BasePage):
    """Promo slider block"""
    current_promo_slide = (By.CSS_SELECTOR, 'div.slick-slide.slick-active')
    switch_slide_in_slider = (By.CSS_SELECTOR, 'ul.slick-dots li')

    """Categories block"""
    locator_category_block_str = 'section.categories.block-fillets'
    category_block = (By.CSS_SELECTOR, f'{locator_category_block_str}')

    categories_title = (By.CSS_SELECTOR, f'{locator_category_block_str} h2.categories-title')

    one_of_categories_card = (By.CSS_SELECTOR, f'{locator_category_block_str} a.category-link')
    name_categories = (By.CSS_SELECTOR, f'{locator_category_block_str} span.title')
    image_categories = (By.CSS_SELECTOR, f'{locator_category_block_str} img')

    right_button = (By.CSS_SELECTOR, f'{locator_category_block_str} button.slider-button.right')
    left_button = (By.CSS_SELECTOR, f'{locator_category_block_str} button.slider-button.left')

    """Offer of the week block"""
    offer_of_week_block_locator_str = ''
    offer_title_offer_of_week = (By.CSS_SELECTOR, f'{offer_of_week_block_locator_str} h2.slider-title')
    slider_button_left_offer_of_week = (By.CSS_SELECTOR, f'{offer_of_week_block_locator_str} button.slider-button.lef')
    slider_button_right_offer_of_week = (By.CSS_SELECTOR, f'{offer_of_week_block_locator_str} button.slider-button.right')
    one_of_card_offer_of_week = (By.CSS_SELECTOR, f'{offer_of_week_block_locator_str} div.product')
    add_to_wishlist_offer_of_week = (By.CSS_SELECTOR, f'{offer_of_week_block_locator_str} button.add-to-wishlist')
    one_of_image_offer_of_week = (By.CSS_SELECTOR, f'{offer_of_week_block_locator_str} img')
    product_name_offer_of_week = (By.CSS_SELECTOR, f'{offer_of_week_block_locator_str} a.product-name')
    product_price = (By.CSS_SELECTOR, f'{offer_of_week_block_locator_str} div.price.product-price')
    add_product_to_cart = (By.CSS_SELECTOR, f'{offer_of_week_block_locator_str} button.add-to-cart')
    watch_all_offer_of_week = (By.CSS_SELECTOR, f'{offer_of_week_block_locator_str} a[href*="/tovar-nedeli"]')

    """Goods of the month block"""
    goods_of_month_block_locator_str = ''
    goods_of_month_title = (By.CSS_SELECTOR, f'{goods_of_month_block_locator_str} h2.slider-title')
    slider_button_left_goods_of_month = (By.CSS_SELECTOR, f'{goods_of_month_block_locator_str} button.slider-button.lef')
    slider_button_right_goods_of_month = (By.CSS_SELECTOR, f'{goods_of_month_block_locator_str} button.slider-button.right')
    one_of_card_goods_of_month = (By.CSS_SELECTOR, f'{goods_of_month_block_locator_str} div.product')
    add_to_wishlist_goods_of_month = (By.CSS_SELECTOR, f'{goods_of_month_block_locator_str} button.add-to-wishlist')
    one_of_image_goods_of_month = (By.CSS_SELECTOR, f'{goods_of_month_block_locator_str} img')
    product_name_goods_of_month = (By.CSS_SELECTOR, f'{goods_of_month_block_locator_str} a.product-name')
    product_price_goods_of_month = (By.CSS_SELECTOR, f'{goods_of_month_block_locator_str} div.price.product-price')
    add_good_of_month_to_cart = (By.CSS_SELECTOR, f'{goods_of_month_block_locator_str} button.add-to-cart')
    watch_all_goods_of_month = (By.CSS_SELECTOR, f'{goods_of_month_block_locator_str} a[href*="/tovar-nedeli"]')

    """Viewed products"""
    viewed_products_block_locator_str = ''
    viewed_products_title = (By.CSS_SELECTOR, f'{viewed_products_block_locator_str} h2.slider-title')
    slider_button_left_viewed_products = (By.CSS_SELECTOR, f'{viewed_products_block_locator_str} button.slider-button.lef')
    slider_button_right_viewed_products = (By.CSS_SELECTOR, f'{viewed_products_block_locator_str} button.slider-button.right')
    one_of_card_viewed_products = (By.CSS_SELECTOR, f'{viewed_products_block_locator_str} div.product')
    add_to_wishlist_viewed_products = (By.CSS_SELECTOR, f'{viewed_products_block_locator_str} button.add-to-wishlist')
    one_of_image_viewed_products = (By.CSS_SELECTOR, f'{viewed_products_block_locator_str} img')
    product_name_viewed_products = (By.CSS_SELECTOR, f'{viewed_products_block_locator_str} a.product-name')
    product_price_viewed_products = (By.CSS_SELECTOR, f'{viewed_products_block_locator_str} div.price.product-price')
    add_viewed_products_to_cart = (By.CSS_SELECTOR, f'{viewed_products_block_locator_str} button.add-to-cart')
    watch_all_viewed_products = (By.CSS_SELECTOR, f'{viewed_products_block_locator_str} a[href*="/tovar-nedeli"]')

    def right_switch_categories(self, locator):
        if self.is_element_visibility(locator) is True:
            pass
        else:
            self.click(self.right_button)
            return self

