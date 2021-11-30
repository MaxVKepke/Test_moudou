from selenium.webdriver.common.by import By

from Page.BasePage import BasePage


class DeliveryPage(BasePage):
    delivery_title = (By.CSS_SELECTOR, 'h2.cms-title')