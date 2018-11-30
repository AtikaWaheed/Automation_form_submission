from utility import UtilityPage


class ScorePage(UtilityPage):

    url = None

    def is_browser_on_page(self):
        return self.q(css='.freebirdFormviewerViewHeaderGradeContainer').visible

    def get_total_points(self):
        """
        Note down the total number you get.
        """
        return self.q(css='.freebirdFormviewerViewHeaderGradeFraction').text
