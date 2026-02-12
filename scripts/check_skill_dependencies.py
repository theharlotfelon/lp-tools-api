from utils.campaigns import get_engagements
from utils.canned_responses import check_canned_responses
from utils.skills import check_skills
from utils.users import check_users
from utils.auto_messages import get_automatic_messages
from utils.widgets import check_widgets
from utils.surveys import get_surveys
from utils.result import dependency_result

skill_list, auto_message_list, canned_list, engagement_list, widget_list, user_list, survey_list = [],[],[],[],[],[],[]

def check_skill_dependencies_api(site, token, skill):
    skill_list = check_skills(site, token, skill)
    auto_message_list = get_automatic_messages(site, token, skill)
    canned_list = check_canned_responses(site, token, skill)
    engagement_list = get_engagements(site, token, skill)
    widget_list = check_widgets(site, token, skill)
    user_list = check_users(site, token, skill)
    survey_list = get_surveys(site, token, skill)
    return dependency_result(skill_list, auto_message_list, canned_list, engagement_list, widget_list, user_list, survey_list)
