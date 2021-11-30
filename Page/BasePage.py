from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.DriverWrapper import DriverWrapper


class BasePage:
    wait_element_time = 20

    def __init__(self):
        self.driver = DriverWrapper.get_webdriver()
        self.wait = WebDriverWait(self.driver, self.wait_element_time)

    def check_is_element_present(self, locator):
        """
        Searches the web element on the page (in dom), for given locator;
        :param locator: css_selector, x_path, class_name and other options to search the web element
        :return: True if web element will by found in dom-tree \
        :return: False if web element will by not found in dom-tree;
        """
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except Exception:
            return False

    def check_are_all_elements_present(self, locator, error_message="Element is missing"):
        """
        Searches the all web element on the page (in dom), from given locator;
        :param locator: css_selector, x_path, class_name and other options to search more then one web elements
        :param error_message: some error message
        :return: list with web elements
        """
        try:
            element_list = self.wait.until(EC.presence_of_all_elements_located(locator), error_message)
            return element_list

        except Exception as error:
            print(f'I am a CHECK_ARE_ALL_ELEMENTS_PRESENTS, can not find {error}')
            return False

    def click(self, locator):
        """
        Searches the web element on the page (in dom), from given locator and click on it;
        :param locator: css_selector, x_path, class_name and other options to search the web element
        :return: self in any way
        """

        if type(locator) is tuple:
            web_element = self.wait.until(EC.presence_of_element_located(locator))
            web_element.click()
        else:
            locator.clicl()
        return self

    def get_current_url(self):
        """
        Get url page which you are
        :return current url
        """
        url = self.driver.current_url
        # print(f'\n---------CURRENT URL-------------\n{url}')
        return url

    def is_element_visible(self, locator):
        """
        Looks for element with given locator and check if this element is visible
        :param locator:
        :return: true if element visible or false if element invisible
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception as error:
            print(f"I'm IS_ELEMENT_VISIBLE: {error}e")
            return False

    def move_cursor_on_element(self, locator):
        """
        Move cursor on element with given locator
        :param locator: css_selector, x_path, class_name and other options to search the web element
        :return: self
        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element).perform()
        return self

    def write_text_in_input(self, locator, text):
        """
        Written text to input with given locator
        :param locator:  css_selector, x_path, class_name and other options to search the web element
        :param text: text to be written to input
        :return: self
        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.send_keys(text)
        return self

    def get_text(self, locator):
        """
        Get text from web element by given locator
        :param locator: css_selector, x_path, class_name and other options to search the web element
        :return: text from element
        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        text = element.text
        return text

    def wait_until_url_changes_after_click(self, click_locator):
        """
        Wait until url changes after clin on element by given locator
        :param click_locator: css_selector, x_path, class_name and other options to search the web element
        :return: self
        """
        current_url = self.driver.current_url
        element = self.wait.until(EC.presence_of_element_located(click_locator))
        element.click()
        self.wait.until(EC.url_changes(current_url))
        return self

    def is_element_clickable(self, locator):
        """
        Check element? by given locator is lickable
        :param locator: css_selector, x_path, class_name and other options to search the web element
        :return: self
        """
        self.wait.until(EC.element_to_be_clickable(locator))
        return self

    def is_element_visibility(self, location):
        """
        Check visibility of element by given locator
        :param location: css_selector, x_path, class_name and other options to search the web element
        :return: self
        """
        element = self.wait.until(EC.presence_of_element_located(location))
        self.wait.until(EC.visibility_of(element))
        return self

    def scroll_page_into_element(self, locator):
        """
        Scroll page into element by locator
        :param locator: css_selector, x_path, class_name and other options to search the web element
        :return: self
        """
        element = self.wait.until((EC.presence_of_element_located(locator)))
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)
        return self

    def check_is_element_invisible(self, element_locator):
        """
        Check and wait the invisibility of the element by locator
        :param element_locator: css_selector, xz-path or another path to the element
        :return: self
        """
        self.wait.until(EC.invisibility_of_element_located(element_locator))
        return self


