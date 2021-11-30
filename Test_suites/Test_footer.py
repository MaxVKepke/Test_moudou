from Page.Footer import Footer
from Test_suites.BaseTest import BaseTest
from utilities.settings import base_url


class TestFooter(BaseTest):
    def test_footer(self, url_on_page=""):
        self.add_rout_in_url_and_go_to_url(url_on_page)
        """ Test footer """
        footer_block = Footer()
        footer_block.is_element_visibility(footer_block.footer)