from Page.Header import Header
from Test_suites.BaseTest import BaseTest


class TestLangSwitcherInHeader(BaseTest):
    def test_lang_switcher_in_header(self):
        rout_on_product_page = '/pazl-avenir-yedynorih-28-elementiv-pz195051-md-98243.html'
        self.add_rout_in_url_and_go_to_url(rout_on_product_page)

        """--------- Test lang_switcher in header ---------"""
        header_block = Header()
        header = header_block.header
        header_block.check_is_element_present(header)

        lang_switcher = header_block.lang_switcher
        header_block.click(lang_switcher)