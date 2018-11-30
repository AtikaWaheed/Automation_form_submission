import os
from constants import BASE_URL
from utility import UtilityPage
from selenium.webdriver.common.keys import Keys


class NinthPageSubmission(UtilityPage):
    """
    Ninth Page submission
    """

    url = os.path.join(BASE_URL, "viewform")

    def is_browser_on_page(self):
        return self.q(css='[aria-label="Year"]').visible

    def enter_current_date_and_time(self, **kwargs):
        """
        Enter current date and time
            - Current date and time fetched from 'datetime'
        """
        if kwargs['question_header'] == "Enter_Current_date":
            self.enter_current_date(kwargs['first_field'], kwargs['second_field'])
        else:
            self.enter_current_time(kwargs['first_field'], kwargs['second_field'])

    def enter_current_date(self, current_month, current_day):
        """
        Enter current date
            -First clear field to make sure its empty
            - Enter current month/current day
        """
        month_field = self.q(css="input[aria-label='Month']")
        month_field.fill(Keys.BACKSPACE)
        month_field.fill(current_month)
        self.q(css="input[aria-label='Day of the month']").fill(current_day)
        self.q(css="input[aria-label='Year']").fill('2018')

    def enter_current_time(self, current_time_hour, current_time_minutes):
        """
        Enter current date
            -First clear field to make sure its empty
            -Enter current time hour and minutes
        """
        hour_field = self.q(css="input[aria-label='Hour']")
        hour_field.click()
        hour_field.fill(Keys.BACKSPACE)
        hour_field.fill(current_time_hour)
        min_field = self.q(css="input[aria-label='Minute']")
        min_field.fill(Keys.BACKSPACE)
        min_field.fill(current_time_minutes)
