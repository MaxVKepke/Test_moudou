from selenium.webdriver.common.by import By

from Page.BasePage import BasePage


class CategoryPage(BasePage):
    """------ locator for category block ------"""
    category_locator_str = 'ul.sidebar__category-list'
    category_list = (By.CSS_SELECTOR, category_locator_str)

    """------ children_goods ------"""
    toys = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/igrashki"]')
    children_room = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/ditjacha-kimnata"]')
    jewelry_and_accessories = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/prikrasi-ta-aksesuari"]')
    strollers = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/koljaski"]')
    baby_food = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/ditjache-harchuvannja"]')
    school_and_office = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/shkola-i-kanctovari"]')
    walks_and_travels = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/proguljanki-i-podorozhi"]')
    diapers_and_swaddling = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/pidguzki-i-spovivannja"]')
    car_seats = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/avtokrisla"]')
    feeding = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/goduvannja"]')
    outdoor_games = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/igri-na-vulici"]')
    toys_for_kids = (By.CSS_SELECTOR, f'{category_locator_str} a[href="/sub-category/igrashki-dlja-maljukiv"]')
    development_and_creativity = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/rozvitok-i-tvorchist"]')
    cosmetics_and_hygiene = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/kosmetika-i-gigiena"]')
    pregnancy_and_motherhood = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/vagitnist-i-materinstvo"]')
    children_active_rest = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/ditjachij-aktivnij-vidpochinok"]')
    for_bathing_and_bathing = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/dlja-kupannja-ta-vanni"]')
    children_household_chemicals = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/ditjacha-pobutova-himija"]')
    child_health = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/zdorov-ja-ditini"]')

    """------ eco_and_organic_goods ------"""
    "eco_and_organic_goods don't have eny sub-category"

    """------ household chemicals ------"""
    chemistry_for_electronics = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/zasobi-po-dogljadu-za-pobutovoju-tehnikoju"]')
    cleaning_chemicals = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/zasobi-dlja-pribirannja"]')
    chemistry_for_washing_dishes = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/zasobi-dlja-mittja-posudu"]')
    washing_chemicals = (By.CSS_SELECTOR, f'{category_locator_str} a[href="/sub-category/tovari-dlja-prannja"]')

    """------ Beauty and health ------"""
    facial_care = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/dogljad-za-oblichchjam"]')
    health_and_safety = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/zdorov-ja-ta-bezpeka"]')
    gift_sets = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/podarunkovi-nabori"]')
    perfumery = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/parfumerija"]')
    body_care = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/dogljad-za-tilom"]')
    makeup = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/makijazh"]')
    oral_care = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/dogljad-za-porozhninoju-rota"]')
    cosmetics_and_accessories = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/kosmetichni-aparati-i-aksesuari"]')
    dermatocosmetics = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/dermatokosmetyka"]')
    organic_cosmetics = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/orhanichna-kosmetyka"]')
    asian_cosmetics = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/aziatska-kosmetyka"]')
    personal_care = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/osobista-gigiena"]')
    hair_care = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/dogljad-za-volossjam"]')
    cosmetics_for_children = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/kosmetika-dlja-ditej"]')

    """------ food ------"""
    desserts_and_sweets = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/deserti-i-solodoschi"]')
    grocery = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/bakalija"]')

    """------ alcohol and beverages ------"""
    strong_alcohol = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/micnij-alkogol"]')
    wine = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/vino"]')
    beer = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/pivo"]')
    non_alcoholic_and_low_alcohol_beverages = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/bezalkogol-ni-ta-slaboalkogol-ni-napoi"]')

    """------ household goods ------"""
    dishes = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/posud"]')
    interior_and_decor = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/inter-er-i-dekor"]')
    home_textiles = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/tekstil-dlja-domu"]')
    household_goods = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/gospodars-ki-tovari"]')

    """------ pet products ------"""
    to_the_dogs = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/sobakam"]')
    cats = (By.CSS_SELECTOR, f'{category_locator_str} a[href*="/sub-category/kotam"]')

    show_oll_button = (By.CSS_SELECTOR, 'div.sidebar__btn-fold')





