import time

from Page.DeliveryPage import DeliveryPage
from Page.Header import Header
from Page.PaymentPage import PaymentPage
from Page.ReturnAandWarrantyPage import ReturnAndWarrantyPage
from Test_suites.BaseTest import BaseTest


class TestHeader(BaseTest):
    def test_header(self):

        """--------- Test navigation_panel in header ---------"""
        header_block = Header()
        navigation_panel_locator = header_block.header_links
        navigation_panel = header_block.check_is_element_present(navigation_panel_locator)
        assert navigation_panel is True, \
            "Navigation bar on header not found"

        url_on_page = ""
        header_block.click(header_block.payment_link)
        header_block.is_element_visible(PaymentPage().payment_title)
        payment_page_url = header_block.get_current_url()
        assert '/payment' in payment_page_url, \
            "Current url don't have /payment"
        self.add_rout_in_url_and_go_to_url(url_on_page)

        header_block.click(header_block.delivery_link)
        header_block.is_element_visible(DeliveryPage.delivery_title)
        refund_page_url = header_block.get_current_url()
        assert '/delivery' in refund_page_url, \
            "Current url don't have /delivery"
        self.add_rout_in_url_and_go_to_url(url_on_page)

        header_block.click(header_block.refund_link)
        header_block.is_element_visible(ReturnAndWarrantyPage.return_and_warranty_title)
        delivery_page_url = header_block.get_current_url()
        assert '/refund' in delivery_page_url, \
            "Current url don't have /refund"
        self.add_rout_in_url_and_go_to_url(url_on_page)

        """--------- Test support contacts in header ---------"""
        contacts_panel = header_block.phone
        header_block.move_cursor_on_element(contacts_panel)
        header_block.is_element_visible(header_block.support_contact_block)

        header_block.is_element_visible(header_block.support_contact_title)
        header_block.is_element_visible(header_block.support_phones)
        header_block.is_element_visible(header_block.email_support)

        """--------- Test header main block ---------"""
        current_ur = header_block.get_current_url()
        if current_ur == 'https://pre-prod.maudau.com.ua/':
            self.add_rout_in_url_and_go_to_url('/pazl-avenir-yedynorih-28-elementiv-pz195051-md-98243.html')
        main_logo = header_block.logo
        header_block.check_is_element_present(main_logo),
        header_block.is_element_visible(main_logo)
        # header_block.click(main_logo)
        header_block.wait_until_url_changes_after_click(main_logo)
        # header_block.is_element_visible(main_logo)
        url_after_click_on_logo = header_block.get_current_url()

        assert url_after_click_on_logo == 'https://pre-prod.maudau.com.ua/', \
            """Wrong url after click on logo"""
        self.add_rout_in_url_and_go_to_url(url_on_page)

        catalog_button = header_block.catalog_button
        header_block.click(catalog_button)
        header_block.is_element_visible(header_block.sidebar_catalog)
        header_block.click(header_block.close_sidebar_button)

        search_input = header_block.search_input
        search_text = 'Ром'
        header_block.write_text_in_input(search_input, search_text)
        matching_search_results = header_block.one_of_matching_search_results
        text_in_matching = header_block.get_text(matching_search_results)
        assert search_text in text_in_matching, \
            """Text in the element does not matching the search"""

        header_block.click(header_block.enter_button)
        header_block.is_element_visible(header_block.auth_sidebar)
        close_auth_sidebar = header_block.close_auth_sidebar
        header_block.is_element_visible(close_auth_sidebar)
        header_block.click(close_auth_sidebar)

        header_block.click(header_block.wishlist_button)
        header_block.is_element_visible(header_block.order_wishlist)
        close_wishlist_button = header_block.close_wishlist
        header_block.is_element_visible(close_wishlist_button)
        header_block.click(close_wishlist_button)

        header_block.click(header_block.basket_button)
        header_block.is_element_visible(header_block.basket)
        close_basket = header_block.close_basket
        header_block.is_element_visible(close_basket)
        header_block.click(close_basket)


































