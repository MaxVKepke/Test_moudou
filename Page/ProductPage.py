from selenium.webdriver.common.by import By

from Page.BasePage import BasePage


class ProductPage(BasePage):
    breadcrumbs_desktop = (By.CSS_SELECTOR, 'div.breadcrumbs.desktop')
    children_goods = (By.CSS_SELECTOR, 'div.breadcrumbs.desktop a[href*="/category/ditjachi-tovari"]')

    """------ locator for product cart ------"""
    image_product = (By.CSS_SELECTOR, 'div.product-info img.product-image__thumb')
    product_gallery = (By.CSS_SELECTOR, 'div.nav-gallery img')

    name_product = (By.CSS_SELECTOR, 'h1.product-title')
    reviews_stars = (By.CSS_SELECTOR, 'div.reviews-starts-title')
    reviews = (By.CSS_SELECTOR, 'div.reviews-starts-title button.rating-btn')
    add_reviews_popup = (By.CSS_SELECTOR, 'section.modal')
    close_reviews_button = (By.CSS_SELECTOR, 'button.btn')

    product_article = (By.CSS_SELECTOR, 'div.article')

    character = (By.CSS_SELECTOR, 'div.product-title-characteristics')
    some_product_attribute = (By.CSS_SELECTOR, 'div.product-middle-info li.product-attribute')
    oll_character_button = (By.CSS_SELECTOR, 'button.scroll-characteristics-btn')

    """------ locator for price block ------"""
    availability = (By.CSS_SELECTOR, 'span.status')

    old_price = (By.CSS_SELECTOR, 'div.price--wrapper span.price_old')
    discount = (By.CSS_SELECTOR, 'div.price--wrapper span.discount-top')
    price_hot = (By.CSS_SELECTOR, 'div.price--wrapper span.price_hot')
    points = (By.CSS_SELECTOR, 'div.price--wrapper div.wrapper__content')
    point_details_popup = (By.CSS_SELECTOR, 'div.price--wrapper a[href="/info/vlasnuy-rahunok"]')

    add_to_basket_button = (By.CSS_SELECTOR, 'div.product-counter button.button-large.button-large')
    minus_products_in_basket = (By.CSS_SELECTOR, 'div.product-side-info button.btn-icon--minus')

    delivery = (By.CSS_SELECTOR, 'div.product-side-info div.product-shipping')
    one_of_shipping = (By.CSS_SELECTOR, 'div.product-side-info div.shipping')

    """------ locator for similar products block ------"""
    similar_products = (By.CSS_SELECTOR, 'div.similar-products-section')
    some_of_similar_products = (By.CSS_SELECTOR, 'a.no-underline.product-link')
    image_similar_products = (By.CSS_SELECTOR, 'div.list-item img.product-image__thumb')
    name_similar_products = (By.CSS_SELECTOR, 'div.product-price-block a')
    old_price_similar_products = (By.CSS_SELECTOR, 'div.product-price-block span.price_old')
    price_similar_products = (By.CSS_SELECTOR, 'div.product-price-block span.price_final')

    """------ detail attribute products ------"""
    about_product = (By.CSS_SELECTOR, 'div.product-about div.menu-item')


    oll_character = (By.CSS_SELECTOR, 'div.product-about__about-item ul.product__characteristics-list')

    reviews_products = (By.CSS_SELECTOR, 'div.reviews__no-reviews')
    add_reviews_button = (By.CSS_SELECTOR, 'button.reviews__add-btn')

    """------ reviewed products block ------"""
    some_reviewed_product_cart = (By.CSS_SELECTOR, 'div.sliderTrack div.product')
    some_image_reviewed_product = (By.CSS_SELECTOR, 'div.sliderTrack div.product img.product-image__thumb')
    some_name_reviewed_product = (By.CSS_SELECTOR, 'div.sliderTrack div.product a.product-name')
    some_old_price_reviewed_product = (By.CSS_SELECTOR, 'div.sliderTrack div.product span.price_old')
    some_hot_price_reviewed_product = (By.CSS_SELECTOR, 'div.sliderTrack div.product span.price_hot')
    some_minus_count_on_basket = (By.CSS_SELECTOR, 'div.sliderTrack div.product button.btn-icon--minus')
    some_button_add_cart = (By.CSS_SELECTOR, 'div.sliderTrack div.product button.add-to-cart')
    counter_product_basket = (By.CSS_SELECTOR, 'div.sliderTrack div.product div.counter')



