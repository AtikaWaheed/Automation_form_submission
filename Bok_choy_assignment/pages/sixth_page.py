import os
from constants import BASE_URL
from utility import UtilityPage


class SixthPageSubmission(UtilityPage):
    """
    Sixth page submission
    """

    url = os.path.join(BASE_URL, "viewform")

    def is_browser_on_page(self):
        return self.q(css='.freebirdMaterialScalecontentRangeLabel').visible

    def rate_assignment(self):
        """
        Rating : What you think that how tough your assignment is?
        """
        self.q(css=".quantumWizTogglePaperradioOffRadio.exportOuterCircle").results[2].click()
