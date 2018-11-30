import os
from constants import BASE_URL
from utility import UtilityPage
from constants import GRID_CSS


class SeventhPageSubmission(UtilityPage):
    """
    Seventh page submission
    """

    url = os.path.join(BASE_URL, "viewform")

    def is_browser_on_page(self):
        return self.q(css='.freebirdFormviewerViewItemsGridUngraded').visible

    def choose_multiple_satisfactory_options(self):
        """
        From each grid, select multiple options
        """
        self.q(css="{}:nth-child(2) label".format(GRID_CSS)).results[2].click()
        self.q(css="{}:nth-child(3) label".format(GRID_CSS)).results[2].click()
        self.q(css="{}:nth-child(4) label".format(GRID_CSS)).results[2].click()
