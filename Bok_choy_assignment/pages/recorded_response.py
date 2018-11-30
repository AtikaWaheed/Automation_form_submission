import os
from constants import BASE_URL
from utility import UtilityPage
from constants import BUTTON_CSS


class RecordedResponse(UtilityPage):

    url = os.path.join(BASE_URL, "formResponse")

    def is_browser_on_page(self):
        return self.q(css='.freebirdFormviewerViewResponseConfirmationMessage').visible

    def click_view_score(self):
        """
        Click 'view score' button
            -Need to switch window
            -Wait page to load
        """
        self.q(css=BUTTON_CSS).click()
        window = self.browser.window_handles[-1]
        self.browser.switch_to.window(window)
        self.wait_for_element_visibility('.freebirdFormviewerViewHeaderGradeContainer', 'Element is visible')
