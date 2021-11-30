from selenium.webdriver.common.by import By

from Page.BasePage import BasePage


class Footer(BasePage):
    footer = (By.CSS_SELECTOR, 'div.footer')