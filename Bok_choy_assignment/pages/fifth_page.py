import os
from constants import BASE_URL
from utility import UtilityPage
from ..pages.constants import FIELD_DIV_CSS, BUTTON_CSS
from selenium.webdriver.common.action_chains import ActionChains


class FifthPageSubmission(UtilityPage):
    """
    Fifth Page submission
    """

    url = os.path.join(BASE_URL, "viewform")

    def is_browser_on_page(self):
        return self.q(css='#i\.desc\.794947146').visible

    def uploading_files(self, ind):
        """
        Before uploading make sure you have files in 'My Drive'.
        Upload both question files(PDF and JPG)
           -Click on select , popup opens
           -Click my drive link
           -Select a file by double click
        :param ind: is the complete question div's number
        """
        self.q(css='{}:nth-child({}) {}'.format(FIELD_DIV_CSS, ind, BUTTON_CSS)).click()
        if ind == 2:
            self.wait_for_element_visibility('.picker.modal-dialog-content', 'Element is visible')
            frame = self.q(css='iframe.picker-frame').results[0]
            self.browser.switch_to.frame(frame)
            print 'Yes'
        else:
            frame_to_be_switched = self.q(css='.picker.modal-dialog.picker-dialog:nth-last-child(2) .picker-frame')[0]
            self.browser.switch_to.frame(frame_to_be_switched)
            print 'no'
        self.wait_for_element_visibility('#picker\:ht', 'Element is visible')
        self.q(css='#\:6 > div').click()
        self.wait_for_element_visibility('[aria-label="Files and folders list view."]', 'Element is visible')
        element = self.q(css='div[aria-label="Files and folders list view."] > div')
        actions = ActionChains(self.browser)
        actions.move_to_element(element[0])
        actions.click(on_element=element[0])
        actions.click(on_element=element[0])
        actions.perform()
        self.browser.switch_to.default_content()
        self.wait_for_element_visibility('#i\.desc\.1516501855', 'Element is visible')
