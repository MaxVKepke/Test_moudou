from selenium.webdriver.common.by import By

from Page.BasePage import BasePage


class ReturnAndWarrantyPage(BasePage):
    return_and_warranty_title = (By.CSS_SELECTOR, 'h2.cms-title')