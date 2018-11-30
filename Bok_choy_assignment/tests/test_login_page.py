from ..pages.constants import USER_EMAIL, USER_PWD
from ..pages.login_page import GoogleLoginPage
from ..pages.landing_page import LandingPage
from bok_choy.web_app_test import WebAppTest


class TestGoogleLogin(WebAppTest):
    
    def setUp(self):
        """
        Instantiate driver
        """
        super(TestGoogleLogin, self).setUp()
        self.landing_page = LandingPage(self.browser)
        self.google_page = GoogleLoginPage(self.browser)

    def test_successfully_login(self):
        """
        Verify user can login successfully with verified account
        """
        self.landing_page.visit()
        self.landing_page.click_sign_in_popup()
        self.google_page.enter_email(USER_EMAIL)
        self.google_page.enter_password(USER_PWD)
