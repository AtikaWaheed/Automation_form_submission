import os
from constants import BASE_URL
from utility import UtilityPage
from ..pages.constants import FIELD_DIV_CSS
from selenium.common.exceptions import NoSuchElementException


class FourthPageSubmission(UtilityPage):
    """
    Fourth Page submission
    """

    url = os.path.join(BASE_URL, "viewform")

    def is_browser_on_page(self):
        return self.q(css='.quantumWizMenuPaperselectOptionList').visible

    def select_capital_options(self, ind, dict_value):
        """
        Select one option from each
            -Click on the tab
            -Choose one option
        :param ind: index is the complete question div's number
        :param dict_value: values fetched from dictionary
        """
        self.wait_for_element_visibility('.quantumWizMenuPaperselectOptionList', 'Element is visible')
        self.q(css='{}:nth-child({}) .isSelected'.format(FIELD_DIV_CSS, ind)).click()
        select_option = self.q(css='.exportSelectPopup [data-value="{}"]'.format(dict_value))
        try:
            select_option.click()
        except NoSuchElementException:
            # Different value
            select_option.click().click()
