from bok_choy.page_object import PageObject
from constants import BASE_URL
from login_page import GoogleLoginPage
import os


class LandingPage(PageObject):

    url = os.path.join(BASE_URL, "viewform")

    def is_browser_on_page(self):
        return self.q(css=".quantumWizDialogPaperdialogTitleText").visible

    def click_sign_in_popup(self):
        """
        Click 'sign in' in popup
            -Wait for some element
            -Click sigIn button
            -Wait ist page to load
        """
        self.wait_for_element_visibility('.quantumWizDialogPaperdialogTitleText', 'title is visible')
        self.q(css='.isUndragged > content').click()
        GoogleLoginPage(self.browser).wait_for_page()
