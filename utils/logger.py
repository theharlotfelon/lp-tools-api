def dependency_logger(skill_list, auto_message_list, canned_list, engagement_list, widget_list, user_list, survey_list):
    if skill_list:
        print("Skills:")
        for skill in skill_list:
            print("ID: {} || Name: {} || Transfer List: {}".format(skill["id"], skill["name"], skill["skillTransferList"]))
    if auto_message_list:
        print("")
        print("Automatic Messages:")
        if "chat" in auto_message_list:
            for c_message in auto_message_list["chat"][0]:
                print("Type: Chat || ID: {} || Event: {} || SKill: {}".format(c_message["id"], c_message["messageEventId"], c_message["contexts"]["SKILL"]))
        if "messaging" in auto_message_list:
            for m_message in auto_message_list["messaging"][0]:
                print("Type: Messaging || ID: {} || Skill: {}".format(m_message["id"], m_message["contexts"]["SKILL"]))
    if canned_list:
        print("")
        print("Predefined Content:")
        for response in canned_list:
            print("ID: {} || Name: {} || Skill: {}".format(response["id"], response["data"][0]["title"], response["skillIds"]))
    if engagement_list:
        print("")
        print("Engagements:")
        for campaign in engagement_list:
            name = campaign["name"]
            type = campaign["type"]
            id = campaign["id"]
            for engagement in campaign["engagements"]:
                print("Campaign: {}({}) || Type: {} || Engagement: {}({}) || Skill: {}".format(name, id, type, engagement["name"], engagement["id"], engagement["skillId"]))
    if widget_list:
        print("")
        print("Widgets")
        for widget in widget_list:
            print("ID: {} || Name: {} || Skill: {}".format(widget["id"], widget["name"], widget["skillIds"]))
    if user_list:
        print("")
        print("Users")
        for user in user_list:
            print("ID: {} || loginName: {} || Skills: {}".format(user["id"], user["loginName"], user["skillIds"]))
    if survey_list:
        print("")
        if "chat" in survey_list:
            print("Pre-Chat Surveys:")
            for c_survey in survey_list["chat"]:
                print("Name: {}".format(c_survey["name"]))
        if "messaging" in survey_list:
            print("")
            print("Conversation Builder Surveys:")
            for s_survey in survey_list["messaging"]:
                print("Name: {}".format(s_survey["botName"]))