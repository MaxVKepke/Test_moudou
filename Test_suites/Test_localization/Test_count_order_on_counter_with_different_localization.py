import time

from Page.CategoryPage import CategoryPage
from Page.Header import Header
from Page.Stuff_page import StuffPage
from Test_suites.BaseTest import BaseTest


class TestCountOrderOnCounterWithDifferentLocalization(BaseTest):

    def test_count_order_in_category_children_goods(self):
        kids_goods = "/category/ditjachi-tovari"
        self.add_rout_in_url_and_go_to_url(kids_goods)

        category_page = CategoryPage()
        stuff_page = StuffPage()

        """Click on category toys"""
        category_page.click(category_page.toys)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on category children_room"""
        category_page.click(category_page.children_room)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on category jewelry_and_accessories"""
        category_page.click(category_page.jewelry_and_accessories)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on category strollers"""
        category_page.click(category_page.strollers)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on category baby_food"""
        category_page.click(category_page.baby_food)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on category school_and_office"""
        category_page.click(category_page.school_and_office)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on category walks_and_travels"""
        category_page.click(category_page.walks_and_travels)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on category diapers_and_swaddling"""
        category_page.click(category_page.diapers_and_swaddling)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category car_seats"""
        category_page.click(category_page.car_seats)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category feeding"""
        category_page.click(category_page.feeding)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category feeding outdoor_games"""
        category_page.click(category_page.outdoor_games)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """category feeding toys_for_kids"""""
        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category feeding toys_for_kids"""
        category_page.click(category_page.toys_for_kids)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category feeding development_and_creativity"""
        category_page.click(category_page.development_and_creativity)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category feeding cosmetics_and_hygiene"""
        category_page.click(category_page.cosmetics_and_hygiene)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category feeding pregnancy_and_motherhood"""
        category_page.click(category_page.pregnancy_and_motherhood)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category feeding children_active_rest"""
        category_page.click(category_page.children_active_rest)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category feeding for_bathing_and_bathing"""
        category_page.click(category_page.for_bathing_and_bathing)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category feeding children_household_chemicals"""
        category_page.click(category_page.children_household_chemicals)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category feeding child_health"""
        category_page.click(category_page.child_health)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(kids_goods)

    def test_count_order_in_category_eco_and_organic_goods(self):
        eco_and_organic_goods = "/sub-category/eko-i-organichni-tovari"
        self.add_rout_in_url_and_go_to_url(eco_and_organic_goods)

        stuff_page = StuffPage()

        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(eco_and_organic_goods)

    def test_count_order_in_category_household_chemicals(self):
        household_chemicals = "/category/pobutova-himija"
        self.add_rout_in_url_and_go_to_url(household_chemicals)

        category_page = CategoryPage()
        stuff_page = StuffPage()

        """Click on category"""
        category_page.click(category_page.chemistry_for_electronics)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(household_chemicals)

        """Click on category"""
        category_page.click(category_page.cleaning_chemicals)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(household_chemicals)

        """Click on category"""
        category_page.click(category_page.chemistry_for_washing_dishes)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(household_chemicals)

        """Click on category"""
        category_page.click(category_page.washing_chemicals)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(household_chemicals)

    def test_count_order_in_category_beauty_and_health(self):
        beauty_and_health = "/category/krasa-i-zdorov-ja"
        self.add_rout_in_url_and_go_to_url(beauty_and_health)

        category_page = CategoryPage()
        stuff_page = StuffPage()

        """Category facial_care"""
        """Click on category"""
        category_page.click(category_page.facial_care)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(beauty_and_health)

        """Category health_and_safety"""
        """Click on category"""
        category_page.click(category_page.health_and_safety)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(beauty_and_health)

        """Category gift_sets"""
        """Click on category"""
        category_page.click(category_page.gift_sets)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(beauty_and_health)

        """Category perfumery"""
        """Click on category"""
        category_page.click(category_page.perfumery)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(beauty_and_health)

        """Category body_care"""
        """Click on category"""
        category_page.click(category_page.body_care)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(beauty_and_health)

        """Category makeup"""
        """Click on category"""
        category_page.click(category_page.makeup)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(beauty_and_health)

        """Category oral_care"""
        """Click on category"""
        category_page.click(category_page.oral_care)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(beauty_and_health)

        """Category cosmetics_and_accessories"""
        """Click on category"""
        category_page.click(category_page.cosmetics_and_accessories)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(beauty_and_health)

        """Category dermatocosmetics"""
        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category"""
        category_page.click(category_page.dermatocosmetics)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(beauty_and_health)

        """Category organic_cosmetics"""
        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category"""
        category_page.click(category_page.organic_cosmetics)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(beauty_and_health)

        """Category asian_cosmetics"""
        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category"""
        category_page.click(category_page.asian_cosmetics)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(beauty_and_health)

        """Category personal_care"""
        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category"""
        category_page.click(category_page.personal_care)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(beauty_and_health)

        """Category hair_care"""
        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category"""
        category_page.click(category_page.hair_care)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(beauty_and_health)

        """Category cosmetics_for_children"""
        """Click on button show oll"""
        category_page.click(category_page.show_oll_button)
        """Click on category"""
        category_page.click(category_page.cosmetics_for_children)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(beauty_and_health)

    def test_count_order_in_category_food(self):
        food = "/category/produkti-harchuvannja"
        self.add_rout_in_url_and_go_to_url(food)

        category_page = CategoryPage()
        stuff_page = StuffPage()

        """Category desserts_and_sweets"""
        """Click on category"""
        category_page.click(category_page.desserts_and_sweets)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(food)

        """Category grocery"""
        """Click on category"""
        category_page.click(category_page.grocery)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(food)

    def test_count_order_in_category_alcohol_and_beverages(self):
        alcohol_and_beverages = "/category/alkogol-i-napoi"
        self.add_rout_in_url_and_go_to_url(alcohol_and_beverages)

        category_page = CategoryPage()
        stuff_page = StuffPage()

        """Category strong_alcohol"""
        """Click on category"""
        category_page.click(category_page.strong_alcohol)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(alcohol_and_beverages)

        """Category wine"""
        """Click on category"""
        category_page.click(category_page.wine)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(alcohol_and_beverages)

        """Category beer"""
        """Click on category"""
        category_page.click(category_page.beer)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(alcohol_and_beverages)

        """Category non_alcoholic_and_low_alcohol_beverages"""
        """Click on category"""
        category_page.click(category_page.non_alcoholic_and_low_alcohol_beverages)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(alcohol_and_beverages)

    def test_count_order_in_category_household_goods(self):
        household_goods = "/category/tovari-dlja-domu"
        self.add_rout_in_url_and_go_to_url(household_goods)

        category_page = CategoryPage()
        stuff_page = StuffPage()

        """Category dishes"""
        """Click on category"""
        category_page.click(category_page.dishes)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(household_goods)

        """Category interior_and_decor"""
        """Click on category"""
        category_page.click(category_page.interior_and_decor)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(household_goods)

        """Category home_textiles"""
        """Click on category"""
        category_page.click(category_page.home_textiles)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(household_goods)

        """Category household_goods"""
        """Click on category"""
        category_page.click(category_page.household_goods)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(household_goods)

    def test_count_order_in_category_pet_products(self):
        pet_products = "/category/zootovary"
        self.add_rout_in_url_and_go_to_url(pet_products)

        category_page = CategoryPage()
        stuff_page = StuffPage()

        """Category to_the_dogs"""
        """Click on category"""
        category_page.click(category_page.to_the_dogs)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(pet_products)

        """Category cats"""
        """Click on category"""
        category_page.click(category_page.cats)
        "Save value in stuff count end compare number ua end ru localization"
        stuff_page.save_value_in_stuff_count_end_compare_number_ua_end_ru_loc()
        self.add_rout_in_url_and_go_to_url(pet_products)
