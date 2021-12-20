import time

import pytest

from Page.Footer import Footer
from Page.MainPage import MainPage
from Test_suites.BaseTest import BaseTest


@pytest.mark.usefixtures('get_base_url')
class TestFooter(BaseTest):

    def test_footer(self):
        """ Test footer """
        footer_block = Footer()
        """----- test footer block located -----"""
        footer_block.scroll_page_into_element(footer_block.footer)
        footer_block.is_element_located(footer_block.footer)

        """----- test logo in footer -----"""
        footer_block.click(footer_block.logo)
        main_page = MainPage()
        footer_block.is_element_located(main_page.category_block)

        """----- test social link button on footer -----"""
        footer_block.check_social_icon(footer_block.instagram_link_button, "instagram")
        footer_block.check_social_icon(footer_block.facebook_link_button, "facebook")
        footer_block.check_social_icon(footer_block.youtube_link_button, "youtube")

        """----- test information_on_payment_methods on footer -----"""
        footer_block.is_element_located(footer_block.information_on_payment_methods)

        """----- test customers block in footer -----"""
        footer_block.check_work_item_in_some_menu(footer_block.footer, footer_block.refund, '/info/refund')
        footer_block.check_work_item_in_some_menu(footer_block.footer, footer_block.public_offer, '/info/public-offer')
        footer_block.check_work_item_in_some_menu(footer_block.footer, footer_block.vlasnuy_rahunok, '/info/vlasnuy-rahunok')
        footer_block.check_work_item_in_some_menu(footer_block.footer, footer_block.delivery, '/info/delivery')
        footer_block.check_work_item_in_some_menu(footer_block.footer, footer_block.about_us, '/info/about-us')
        footer_block.check_work_item_in_some_menu(footer_block.footer, footer_block.payment, '/info/payment')
        footer_block.check_work_item_in_some_menu(footer_block.footer, footer_block.contacts, '/info/contacts')

        """----- test contact block in footer -----"""
        footer_block.is_element_located(footer_block.contacts_block)
        footer_block.is_element_located(footer_block.title_contacts)
        footer_block.is_element_located(footer_block.support_contact)




