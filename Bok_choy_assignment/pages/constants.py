import os

# Credentials

USER_EMAIL = os.getenv("useremail")
USER_PWD = os.getenv("userpassword")

# URL
BASE_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfSGh4qzssK1gnZ6JEUe1D4E3lmGCelVD0VZgdHs_y7K_U7rA/"

# Email/Password fields css

PWD_FIELD_CSS = 'input[type="password"]'
EMAIL_FIELD_CSS = 'input[type="email"]'

# Page Status CSS
PAGE_STATUS_CSS = '.freebirdFormviewerViewNavigationPercentComplete'

# Questions field CSS
FIELD_DIV_CSS = '.freebirdFormviewerViewItemsItemItem'
FIELD_TITLE = '.freebirdFormviewerViewItemsItemItemTitle'
CORRECT_ANS_CSS = '.freebirdFormviewerViewItemsItemGradingGradingBox .docssharedWizToggleLabeledPrimaryText > span'

# Button CSS
BUTTON_CSS = '.quantumWizButtonPaperbuttonLabel.exportLabel'


# ERROR_MSG_CSS
ERROR_MSG_CSS = '.freebirdFormviewerViewItemsItemErrorMessage'

# Grid CSS
GRID_CSS = ".freebirdFormviewerViewItemsGridRowGroup"
