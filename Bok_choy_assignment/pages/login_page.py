from bok_choy.page_object import PageObject
from selenium.webdriver.common.keys import Keys
from first_page import FirstPageSubmission
from constants import EMAIL_FIELD_CSS, PWD_FIELD_CSS


class GoogleLoginPage(PageObject):

    url = None

    def is_browser_on_page(self):
        return self.q(css=EMAIL_FIELD_CSS).visible

    def enter_email(self, username):
        """
        :param username: Enter verified username
        """
        self.wait_for_element_visibility(EMAIL_FIELD_CSS, 'element is visible')
        user_field = self.q(css=EMAIL_FIELD_CSS)
        user_field.fill(username)
        user_field[0].send_keys(Keys.RETURN)

    def enter_password(self, password):
        """
        :param password: Enter verified password
        """
        self.wait_for_element_visibility(PWD_FIELD_CSS, 'element is visible')
        pasw_field = self.q(css=PWD_FIELD_CSS)
        pasw_field.fill(password)
        pasw_field[0].send_keys(Keys.RETURN)
        FirstPageSubmission(self.browser).wait_for_page()
