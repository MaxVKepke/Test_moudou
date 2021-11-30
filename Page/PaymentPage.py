from selenium.webdriver.common.by import By

from Page.BasePage import BasePage


class PaymentPage(BasePage):
    payment_title = (By.CSS_SELECTOR, 'h2.cms-title')