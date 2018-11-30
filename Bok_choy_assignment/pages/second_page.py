import os
from constants import BASE_URL
from utility import UtilityPage
from ..pages.constants import FIELD_DIV_CSS


class SecondPageSubmission(UtilityPage):
    """
    Second Page submission
    """

    url = os.path.join(BASE_URL, "viewform")

    def is_browser_on_page(self):
        return self.q(css='[aria-label="Parallel Testing"]').visible

    def fill_answers_for_locator_and_firebug(self, index_count, data_value):
        """
        Second page all questions to be executed
        :param index_count: question div count
        :param data_value: to fetch from dictionary
        """
        self.q(css='{}:nth-child({}) [data-value="{}"]'.format(FIELD_DIV_CSS, index_count, data_value)).click()
