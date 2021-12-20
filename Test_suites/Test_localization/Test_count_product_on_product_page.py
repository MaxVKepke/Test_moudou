from Page.CategoryPage import CategoryPage
from Page.Header import Header
from Page.Stuff_page import StuffPage
from Test_suites.BaseTest import BaseTest


class TestCountProductOnProductPage(BaseTest):

    def test_count_product_on_product_page(self):
        kids_goods = "/category/ditjachi-tovari"
        self.add_rout_in_url_and_go_to_url(kids_goods)

        category_page = CategoryPage()
        stuff_page = StuffPage()

        """Click on category toys"""
        category_page.click(category_page.toys)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on category children_room"""
        category_page.click(category_page.children_room)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on category jewelry_and_accessories"""
        category_page.click(category_page.jewelry_and_accessories)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on category strollers"""
        category_page.click(category_page.strollers)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on category baby_food"""
        category_page.click(category_page.baby_food)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on category school_and_office"""
        category_page.click(category_page.school_and_office)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on category walks_and_travels"""
        category_page.click(category_page.walks_and_travels)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on category diapers_and_swaddling"""
        category_page.click(category_page.diapers_and_swaddling)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category car_seats"""
        category_page.click(category_page.car_seats)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category feeding"""
        category_page.click(category_page.feeding)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category outdoor_games"""
        category_page.click(category_page.outdoor_games)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category toys_for_kids"""
        category_page.click(category_page.toys_for_kids)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category development_and_creativity"""
        category_page.click(category_page.development_and_creativity)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category cosmetics_and_hygiene"""
        category_page.click(category_page.cosmetics_and_hygiene)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category pregnancy_and_motherhood"""
        category_page.click(category_page.pregnancy_and_motherhood)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category children_active_rest"""
        category_page.click(category_page.children_active_rest)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category for_bathing_and_bathing"""
        category_page.click(category_page.for_bathing_and_bathing)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category children_household_chemicals"""
        category_page.click(category_page.children_household_chemicals)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category child_health"""
        category_page.click(category_page.child_health)

        oll_number_product = stuff_page.compare_number_of_goods_in_categories()

        # переклюити мову на російську
        header_block = Header()
        stuff_page.click(header_block.ru_localization_button)

        oll_number_product_ru = stuff_page.compare_number_of_goods_in_categories()

        assert oll_number_product == oll_number_product_ru

        print(f'{oll_number_product} = {oll_number_product}')
        self.add_rout_in_url_and_go_to_url(kids_goods)