import os
from constants import BASE_URL
from utility import UtilityPage
from ..pages.constants import FIELD_DIV_CSS


class ThirdPageSubmission(UtilityPage):
    """
    Third page submission
    """

    url = os.path.join(BASE_URL, "viewform")

    def is_browser_on_page(self):
        return self.q(css='.freebirdMaterialHeaderbannerPagebreakText ').visible

    def select_multiple_checkboxes(self, index_count):
        """
        Select multiple answers
        :param index_count: is a complete question div
        """
        answers = self.q(css='{}:nth-child({}) .docssharedWizToggleLabeledLabelText:nth-child(1)'.format(
            FIELD_DIV_CSS, index_count))
        answers[0].click()
        answers[3].click()
