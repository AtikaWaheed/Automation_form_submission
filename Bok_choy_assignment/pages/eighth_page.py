import os
from constants import BASE_URL
from ..pages.seventh_page import SeventhPageSubmission


class EighthPageSubmission(SeventhPageSubmission):
    """
    Eight Page submission
    """

    url = os.path.join(BASE_URL, "viewform")

    def is_browser_on_page(self):
        return self.q(css='.freebirdFormviewerViewItemsGridScrollContainer').visible

    def choose_multiple_proficiency_options(self):
        """
        Select multiple options from each row
        """
        self.choose_multiple_satisfactory_options()
