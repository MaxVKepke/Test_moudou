from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.DriverWrapper import DriverWrapper


class BasePage:
    wait_element_time = 20

    def __init__(self):
        self.driver = DriverWrapper.get_webdriver()
        self.wait = WebDriverWait(self.driver, self.wait_element_time)

    def is_element_located(self, locator):
        """
        Looks for element with given locator and check if this element is visible
        :param locator:
        :return: true if element visible or false if element invisible
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception as error:
            print(f"I'm IS_ELEMENT_LOCATED: {error}e")
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
            print(f'I am a CHECK_ARE_ALL_ELEMENTS, can not find {error}')
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
            locator.click()
        return self

    def get_current_url(self):
        """
        Get url page which you are
        :return current url
        """
        url = self.driver.current_url
        # print(f'\n---------CURRENT URL-------------\n{url}')
        return url

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
        if type(locator) is tuple:
            element = self.wait.until(EC.presence_of_element_located(locator))
            text = element.text
        else:
            text = locator.text

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
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            return True

        except Exception as error:
            raise error

    def is_element_visibility(self, locator):
        """
        Check visibility of element by given locator
        :param locator: css_selector, x_path, class_name and other options to search the web element
        :return: true or false if element invisible
        """
        try:
            if locator is tuple:
                element = self.wait.until(EC.presence_of_element_located(locator))
                self.wait.until(EC.visibility_of(element))
                return True
            else:
                self.wait.until(EC.visibility_of(locator))
                return True

        except Exception as error:
            return False

    def scroll_page_into_element(self, locator):
        """
        Scroll page into element by locator
        :param locator: css_selector, x_path, class_name and other options to search the web element
        :return: self
        """
        element = self.wait.until((EC.presence_of_element_located(locator)))
        self.driver.execute_script("return arguments[0].scrollIntoView();", element)
        return self

    def is_element_invisible(self, locator):
        """
        Check and wait the invisibility of the element by locator
        :param locator: css_selector, xz-path or another path to the element
        :return: self
        """
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True

        except Exception as error:
            print(f'I am a IS_ELEMENT_INVISIBLE, {error}')
            return False

    def get_oll_element_by_locator(self, locator):
        """
        Searches for and waits for web-element by locator
        :param locator: css_selector, xz-path or another path to the element
        :return: web-element_list
        """
        element_list = self.wait.until(EC.presence_of_all_elements_located(locator))
        return element_list

    def get_web_element(self, locator):
        """
        Wait until
        :param locator:
        :return:
        """

    def return_on_privies_page(self):
        """
        Return on privies page
        :return: self page
        """
        self.driver.execute_script("window.history.go(-1)")
        return self

    def wait_until_url_cheng(self, changeable_url):
        self.get_current_url()
        self.wait.until(EC.url_changes(changeable_url))

    def check_work_item_in_some_menu(self, scroll_element, click_element, expected_url: str):
        self.scroll_page_into_element(scroll_element)
        self.wait_until_url_changes_after_click(click_element)
        current_url = self.get_current_url()
        assert expected_url in current_url

        return self
