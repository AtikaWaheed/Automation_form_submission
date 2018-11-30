from datetime import datetime
from datetime import date

now = datetime.now()
today = date.today()
current_month = today.month
current_day = today.day
current_time_minutes = now.strftime('%M')
current_time_hour = now.strftime('%I')

pages_dict = {
            'Email': {'empty_field_error': 'This is a required question',
                      'wrong_pattern_error': 'Must be a valid email address',
                      'input_value': 'a@a.com'},
            'Name': {'empty_field_error': 'This is a required question', 'input_value': 'Tester'},
            'CNIC': {'empty_field_error': 'This is a required question', 'input_value': '4353444444444',
                     'wrong_pattern_error': 'Must match pattern'},
            'Phone_Number': {'empty_field_error': 'This is a required question', 'input_value': '43534444444',
                             'wrong_pattern_error': 'Must match pattern'},
            'Select_the_name_which_is_NOT_a_type_of_the_locater': {'empty_field_error': 'This is a required question',
                                                                   'input_value': 'ID'},
            'Use_of_Firebug_in_Selenium': {'empty_field_error': 'This is a required question',
                                           'input_value': 'Programming'},
            'Select_the_correct_answers': {'empty_field_error': 'This is a required question'},
            'Select_the_two_numbers_that_are_not_prime.': {'empty_field_error': 'This is a required question'},
            'Capital_of_Pakistan': {'empty_field_error': 'This is a required question',
                                    'input_value': 'Islamabad'},
            'Capital_of_Punjab': {'empty_field_error': 'This is a required question',
                                  'input_value': 'Lahore'},
            'Upload_pdf_file': {'empty_field_error': 'This is a required question'},
            'Upload_Image_File': {'empty_field_error': 'This is a required question'},
            'On_a_scale_of_1_to_five_how_hard_this_assignment_is': {'empty_field_error': 'This is a required question'},
            'How_satisfied_are_you_with_the_following': {'empty_field_error': 'This question requires one response per row'},
            'Select_your_proficiency_in_following': {'empty_field_error': 'This question requires at least one response per row'},
            'Enter_Current_time': {'empty_field_error': 'This is a required question',
                                   'wrong_pattern_error': 'Invalid time', 'first_field': current_time_hour,
                                   'second_field': current_time_minutes},
            'Enter_Current_date': {'empty_field_error': 'This is a required question',
                                   'wrong_pattern_error': 'Invalid date', 'first_field': current_month,
                                   'second_field': current_day}
}
