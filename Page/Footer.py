from selenium.webdriver.common.by import By

from Page.BasePage import BasePage


class Footer(BasePage):
    locator_footer_str = 'div.footer'

    footer = (By.CSS_SELECTOR, f'{locator_footer_str}')

    info_block = (By.CSS_SELECTOR, 'div#footer_info')
    logo = (By.CSS_SELECTOR, f'{locator_footer_str} a[title="Головна сторінка"]')
    instagram_link_button = (By.CSS_SELECTOR, f'{locator_footer_str} a[href*="https://www.instagram.com/"]')
    facebook_link_button = (By.CSS_SELECTOR, f'{locator_footer_str} a[href*="https://www.facebook.com/"]')
    youtube_link_button = (By.CSS_SELECTOR, f'{locator_footer_str} a[href*="https://www.youtube.com/"]')
    information_on_payment_methods = (By.CSS_SELECTOR, f'{locator_footer_str} img.payments')

    customers_block = (By.CSS_SELECTOR, 'div#footer_customers')

    locator_desktop_version = 'div.desktop'

    refund = (By.CSS_SELECTOR, f'{locator_desktop_version} a[href*="/info/refund"]')
    public_offer = (By.CSS_SELECTOR, f'{locator_desktop_version} a[href*="/info/public-offer"]')
    vlasnuy_rahunok = (By.CSS_SELECTOR, f'{locator_desktop_version} a[href*="/info/vlasnuy-rahunok"]')
    delivery = (By.CSS_SELECTOR, f'{locator_desktop_version} a[href*="/info/delivery"]')
    about_us = (By.CSS_SELECTOR, f'{locator_desktop_version} a[href*="/info/about-us"]')
    payment = (By.CSS_SELECTOR, f'{locator_desktop_version} a[href*="/info/payment"]')
    contacts =(By.CSS_SELECTOR, f'{locator_desktop_version} a[href*="/info/contacts"]')

    locator_contacts_str = 'div#footer_contacts'
    contacts_block = (By.CSS_SELECTOR, f'{locator_contacts_str}')
    title_contacts = (By.CSS_SELECTOR, f'{locator_contacts_str} h4.mb16')
    support_contact = (By.CSS_SELECTOR, f'{locator_footer_str} {locator_desktop_version} div.column')

    def switch_page(self, number_page: int):
        self.driver.switch_to.window(self.driver.window_handles[number_page])

    def close_page(self):
        self.driver.close()

    def check_social_icon(self, locator_social_link_button, social_name):
        self.click(locator_social_link_button)

        self.switch_page(1)
        instagram_url = self.get_current_url()
        if social_name == "instagram":
            assert 'instagram.com/' in instagram_url

        if social_name == "facebook":
            assert 'facebook.com/maudau' in instagram_url

        if social_name == "youtube":
            assert 'youtube.com/channel/' in instagram_url

        self.close_page()
        self.switch_page(0)

        return self


