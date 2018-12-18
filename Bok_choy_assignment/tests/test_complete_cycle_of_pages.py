from utils import UtilsTest
from ..pages.constants import USER_EMAIL, USER_PWD


class TestCompleteCycle(UtilsTest):

    def setUp(self):
        super(TestCompleteCycle, self).setUp()

    def test_successfully_submission_of_all_pages(self):
        """
        -Successfully LoggedIn
        -Submission of complete 9 pages form
        -Note down the total score you got(Print status)
        -Note down all correct answers from final feedback response
        -Submit all questions with all correct answers in a csv file
        """
        self.successfully_loggedIn(USER_EMAIL, USER_PWD)
        self.first_page_execution()
        self.second_page_execution()
        self.third_page_execution()
        self.fourth_page_execution()
        self.fifth_page_execution()
        self.sixth_page_execution()
        self.seventh_page_execution()
        self.eighth_page_execution()
        self.ninth_page_execution()
        self.recorded_response.click_view_score()
        self.score_page.wait_for_page()
        total_score_get = self.score_page.get_total_points()
        print "Got " + total_score_get[0] + " points."
        self.write_all_correct_answers_for_wrong_qs_in_csv()
