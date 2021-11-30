from selenium.webdriver.common.by import By

from Page.BasePage import BasePage


class Header(BasePage):
    test_element = (By.CSS_SELECTOR, "div.FPdoLc input.RNmpXc")

    header = (By.CSS_SELECTOR, 'header.header')

    lang_switcher = (By.CSS_SELECTOR, 'div.lang_switcher')

    header_links = (By.CSS_SELECTOR, 'div.header-links')
    payment_link = (By.CSS_SELECTOR, 'div.header-links a[href*="/info/payment"]')
    delivery_link = (By.CSS_SELECTOR, 'div.header-links a[href*="/info/delivery"]')
    refund_link = (By.CSS_SELECTOR, 'div.header-links a[href*="/info/refund"]')

    phone = (By.CSS_SELECTOR, 'div.phone')
    support_contact_block = (By.CSS_SELECTOR, 'div.phone-tooltip')
    support_contact_title = (By.CSS_SELECTOR, 'span.service')
    support_phones = (By.CSS_SELECTOR, 'a.phone-tooltip-number')
    email_support = (By.CSS_SELECTOR, 'span.phone-tooltip-email-caption')

    logo = (By.CSS_SELECTOR, 'div.header-bottom a.custom-logo')

    catalog_button = (By.CSS_SELECTOR, 'button.catalog-button')
    sidebar_catalog = (By.CSS_SELECTOR, 'div.sidebar-menu__container')
    close_sidebar_button = (By.CSS_SELECTOR, 'button.icon-close')

    search_input = (By.CSS_SELECTOR, 'div.search-input input.search-input-field')
    one_of_matching_search_results = (By.CSS_SELECTOR, 'div.product-middle a.name')

    enter_button = (By.CSS_SELECTOR, 'div.header-actions div.account-icon')
    auth_sidebar = (By.CSS_SELECTOR, 'div.auth-sidebar')
    close_auth_sidebar = (By.CSS_SELECTOR, 'div.close-icon')

    wishlist_button = (By.CSS_SELECTOR, 'div.header-actions button.wishlist-icon')
    order_wishlist = (By.CSS_SELECTOR, 'div.wishlist')
    close_wishlist = (By.CSS_SELECTOR, 'div.wishlist svg.close-icon')

    basket_button = (By.CSS_SELECTOR, 'div.header-actions div.microcart-icon')
    basket_counter = (By.CSS_SELECTOR, 'button.cart-total')
    basket = (By.CSS_SELECTOR, 'div.cl-accent')
    close_basket = (By.CSS_SELECTOR, 'div.cl-accent button.btn')


