import os
from constants import PAGE_STATUS_CSS
from constants import BASE_URL
from utility import UtilityPage


class FirstPageSubmission(UtilityPage):
    """
    First page submission
    """

    url = os.path.join(BASE_URL, "viewform")

    def is_browser_on_page(self):
        return self.q(css=PAGE_STATUS_CSS).visible

    def fill_fields_for_ist_page(self, indx_count, dict_value):
        """
        Fill ist page of form
        :param indx_count: are counts of each question's main div
        :param dict_value: values to put in fields
        """
        self.enter_some_correct_and_wrong_values_in_fields(indx_count, dict_value)
