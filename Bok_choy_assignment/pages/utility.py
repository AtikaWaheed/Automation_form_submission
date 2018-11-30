from bok_choy.page_object import PageObject
from ..pages.constants import FIELD_DIV_CSS, BUTTON_CSS, ERROR_MSG_CSS, FIELD_TITLE
from selenium.webdriver.common.keys import Keys


class UtilityPage(PageObject):

    url = None

    def is_browser_on_page(self):
        return True

    def status_of_page(self):
        """
        :return: the current page status which is (etc Page 1 of 9)
        """
        return self.q(css='.freebirdFormviewerViewNavigationPercentComplete').results[0].text

    def all_question_headings(self):
        """
        It would pile up all question headings(titles)on each page
        :return: All question titles
        """
        return self.q(css='{}.freebirdCustomFont'.format(FIELD_TITLE)).text

    def click_next_button(self):
        """
        Click next button to move to next page
        """
        self.wait_for_element_visibility('.freebirdFormviewerViewNavigationButtonsAndProgress', 'Buttons are visible')
        button = self.q(css=BUTTON_CSS).results[-1]
        button.click()

    def error_with_empty_and_wrong_fields(self, ind):
        """
        Note down the empty and wrong field errors
        :param ind: is the index of each question in a list
        :return: error occurs with empty and wrong fields
        """
        self.wait_for_element_visibility('.HasError', 'Error messages are visible')
        error_msg = self.q(
            css='{}:nth-child({}) {}'.format(FIELD_DIV_CSS, ind, ERROR_MSG_CSS))[0].text
        return error_msg

    def enter_some_correct_and_wrong_values_in_fields(self, ind, field_value):
        """
        Enter some wrong value to verify wrong field value error.
        :param ind: is the index of each question in a list
        :param field_value: is the input value, either its wrong characters or correct inputs
        """
        value = self.q(
            css='{}:nth-child({}) .quantumWizTextinputPaperinputInputArea > input'.format(FIELD_DIV_CSS, ind))
        value.fill(Keys.BACKSPACE)
        value[0].send_keys(field_value)
