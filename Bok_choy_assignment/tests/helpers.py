from bok_choy.web_app_test import WebAppTest
from ..pages.utility import UtilityPage
from ..pages.second_page import SecondPageSubmission
from ..pages.first_page import FirstPageSubmission
from dictionaries import pages_dict
from ..pages.third_page import ThirdPageSubmission
from ..pages.fourth_page import FourthPageSubmission
from ..pages.fifth_page import FifthPageSubmission
from ..pages.sixth_page import SixthPageSubmission
from ..pages.seventh_page import SeventhPageSubmission
from ..pages.eighth_page import EighthPageSubmission
from ..pages.ninth_page import NinthPageSubmission
from ..pages.recorded_response import RecordedResponse
from ..pages.score_page import ScorePage


class HelpersTest(WebAppTest):
    """
    This test class contains all helpers
    """

    def setUp(self):
        """
        Instantiate webdriver
        """
        super(HelpersTest, self).setUp()
        self.browser.maximize_window()
        self.utility_page = UtilityPage(self.browser)
        self.first_page = FirstPageSubmission(self.browser)
        self.second_page = SecondPageSubmission(self.browser)
        self.third_page = ThirdPageSubmission(self.browser)
        self.fourth_page = FourthPageSubmission(self.browser)
        self.fifth_page = FifthPageSubmission(self.browser)
        self.sixth_page = SixthPageSubmission(self.browser)
        self.seventh_page = SeventhPageSubmission(self.browser)
        self.eighth_page = EighthPageSubmission(self.browser)
        self.ninth_page = NinthPageSubmission(self.browser)
        self.recorded_response = RecordedResponse(self.browser)
        self.score_page = ScorePage(self.browser)

    def all_questions_title(self):
        """
        Collect all question's title and store into a list after some cleanups
        :return: Cleanup titles
        """
        all_headings = self.utility_page.all_question_headings()
        question_title = []
        for title in all_headings:
            """
            This loop iterates all questions on page.
            """
            title = title.replace(' *', '')
            key = title.replace(' ', '_')
            key = key.replace('?', '')
            question_title.append(key)
        return question_title

    def errors_and_correct_input_values_helper(self, wrong_pattern_error=False):
        """
        This helper helps to iterate three things :
            - Verify empty field error messages
            - Verify wrong character error messages
            - Verify correct field values has entered
        :param wrong_pattern_error: It include fields with the wrong characters only
        Procedure:
            - Note down status of page
            - Iterate all pages one by one
            - Choose each page and iterate all questions
            - Each questions  need to verify three things:
                    - Empty field error messages
                    - Wrong character field error messages(If that field contains)
                    - Enter and choose correct input
        All questions are being notified by indexes.
        """
        status_of_page = self.utility_page.status_of_page()
        question_title = self.all_questions_title()
        ind = 0
        for title in question_title:
            self.utility_page.click_next_button()
            ind = ind + 1
            try:
                empty_field_error = self.utility_page.error_with_empty_and_wrong_fields(ind)
            except IndexError:
                ind = ind + 1
                empty_field_error = self.utility_page.error_with_empty_and_wrong_fields(ind)
            self.assertEqual(empty_field_error, pages_dict.get(title).get('empty_field_error'))
            if wrong_pattern_error:
                if title != 'Name':
                    self.utility_page.enter_some_correct_and_wrong_values_in_fields(ind, '@')
                    self.utility_page.click_next_button()
                    wrong_charac_error = self.utility_page.error_with_empty_and_wrong_fields(ind)
                    self.assertEqual(wrong_charac_error, pages_dict.get(title).get('wrong_pattern_error'))
            if status_of_page == 'Page 1 of 9':
                self.first_page.fill_fields_for_ist_page(ind, pages_dict.get(title).get('input_value'))
            if status_of_page == 'Page 2 of 9':
                self.second_page.fill_answers_for_locator_and_firebug(ind, pages_dict.get(title).get('input_value'))
            if status_of_page == 'Page 3 of 9':
                self.third_page.select_multiple_checkboxes(ind)
            if status_of_page == 'Page 4 of 9':
                self.fourth_page.select_capital_options(ind, pages_dict.get(title).get('input_value'))
            if status_of_page == 'Page 5 of 9':
                self.fifth_page.uploading_files(ind)
            if status_of_page == "Page 6 of 9":
                self.sixth_page.rate_assignment()
            if status_of_page == "Page 7 of 9":
                self.seventh_page.choose_multiple_satisfactory_options()
            if status_of_page == "Page 8 of 9":
                self.eighth_page.choose_multiple_proficiency_options()
            if status_of_page == "Page 9 of 9":
                self.ninth_page.enter_current_date_and_time(question_header=title,
                                                            first_field=pages_dict.get(title).get('first_field'),
                                                            second_field=pages_dict.get(title).get('second_field')
                                                            )
        self.utility_page.click_next_button()
