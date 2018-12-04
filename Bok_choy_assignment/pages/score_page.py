from utility import UtilityPage
from constants import FIELD_DIV_CSS, FIELD_TITLE, CORRECT_ANS_CSS


class ScorePage(UtilityPage):

    url = None

    def is_browser_on_page(self):
        return self.q(css='.freebirdFormviewerViewHeaderGradeContainer').visible

    def get_total_points(self):
        """
        Note down the total number you get.
        """
        return self.q(css='.freebirdFormviewerViewHeaderGradeFraction').text

    def find_all_grading_questions_title(self, form_card_ind, div_ind):
        """
        Find out all grading questions those need to re assess.
        """
        return self.q(css='.freebirdFormviewerViewFormCard:nth-child({}) {}:nth-child({}) {}'.
                      format(form_card_ind, FIELD_DIV_CSS, div_ind, FIELD_TITLE)).text

    def find_all_correct_answers_from_each_section(self, form_card_ind, div_ind):
        """
        Collect all correct answers from form
        """
        return self.q(css='.freebirdFormviewerViewFormCard:nth-child({}) {}:nth-child({}) {}'.
                      format(form_card_ind, FIELD_DIV_CSS, div_ind, CORRECT_ANS_CSS)).text
