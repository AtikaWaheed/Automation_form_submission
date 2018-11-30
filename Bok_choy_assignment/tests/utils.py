from helpers import HelpersTest
from ..pages.login_page import GoogleLoginPage
from ..pages.landing_page import LandingPage


class UtilsTest(HelpersTest):
    """
    This class is a test helper
    """

    def setUp(self):
        super(UtilsTest, self).setUp()
        self.landing_page = LandingPage(self.browser)
        self.google_page = GoogleLoginPage(self.browser)

    def successfully_loggedIn(self, email, password):
        """
        Verify user can login successfully with verified account
        """
        self.landing_page.visit()
        self.landing_page.click_sign_in_popup()
        self.google_page.enter_email(email)
        self.google_page.enter_password(password)
        self.first_page.wait_for_page()

    def first_page_execution(self):
        """
        Execute and submit ist page
        Wait second page to load.
        """
        self.errors_and_correct_input_values_helper(wrong_pattern_error=True)
        self.utility_page.click_next_button()
        self.utility_page.click_next_button()
        self.second_page.wait_for_page()

    def second_page_execution(self):
        """
        Execute and submit second page
        Wait third page to load
        """
        self.errors_and_correct_input_values_helper()
        self.third_page.wait_for_page()

    def third_page_execution(self):
        """
        Execute and submit third page
        Wait fourth page to load
        """
        self.errors_and_correct_input_values_helper()
        self.fourth_page.wait_for_page()

    def fourth_page_execution(self):
        """
        Execute and Submit fourth page
        Wait fifth page to load
        """
        self.errors_and_correct_input_values_helper()
        self.fifth_page.wait_for_page()

    def fifth_page_execution(self):
        """
        Submit and execute fifth page.
        Wait sixth page to load
        """
        self.errors_and_correct_input_values_helper()
        self.sixth_page.wait_for_page()

    def sixth_page_execution(self):
        """
        Execute and Submit sixth page
        Wait seventh page to load
        """
        self.errors_and_correct_input_values_helper()
        self.utility_page.click_next_button()
        self.seventh_page.wait_for_page()

    def seventh_page_execution(self):
        """
        Execute and Submit seventh page by selecting multiple options
        Wait eighth page to load
        """
        self.errors_and_correct_input_values_helper()
        self.eighth_page.wait_for_page()

    def eighth_page_execution(self):
        """
        Execute and Submit eight page by selecting your proficiency
        Wait ninth page to load
        """
        self.errors_and_correct_input_values_helper()
        self.ninth_page.wait_for_page()

    def ninth_page_execution(self):
        """
        Execute and Submit ninth page by selecting current time and date of submission
        Wait response page to finish loading
        """
        self.errors_and_correct_input_values_helper(wrong_pattern_error=True)
        self.utility_page.click_next_button()
        self.recorded_response.wait_for_page()
