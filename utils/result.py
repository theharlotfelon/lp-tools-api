def dependency_result(skill_list, auto_message_list, canned_list, engagement_list, widget_list, user_list, survey_list):
    result = {
        "skills": [],
        "auto-messages": [],
        "unified-auto-messages": [],
        "cannedResponses": [],
        "engagements": [],
        "widgets": [],
        "users": [],
        "surveys": {"preChatSurveys": [], "cbSurveys": []}
    }
    if skill_list:
        for skill in skill_list:
            result["skills"].append({"id": skill["id"], "name": skill["name"], "skillTransferList": skill["skillTransferList"]})
    if auto_message_list:
        if "chat" in auto_message_list:
            for c_message in auto_message_list["chat"][0]:
                result["auto-messages"].append({"id": c_message["id"], "event": c_message["messageEventId"], "skills": c_message["contexts"]["SKILL"]})
        if "messaging" in auto_message_list:
            for m_message in auto_message_list["messaging"][0]:
                result["unified-auto-messages"].append({"id": m_message["id"], "skills": m_message["contexts"]["SKILL"]})
    if canned_list:
        for response in canned_list:
            result["cannedResponses"].append({"id": response["id"], "name": response["data"][0]["title"], "skill": response["skillIds"]})
    if engagement_list:
        for campaign in engagement_list:
            name = campaign["name"]
            type = campaign["type"]
            id = campaign["id"]
            campaign_item = {"id": id, "name": name, "type": type, "engagements": []}
            result["engagements"].append(campaign_item)
            for engagement in campaign["engagements"]:
                campaign_item["engagements"].append({"id": engagement["id"], "name": engagement["name"], "skills": engagement["skillId"]})
    if widget_list:
        for widget in widget_list:
            result["widgets"].append({"id": widget["id"], "name": widget["name"], "skills": widget["skillIds"]})
    if user_list:
        for user in user_list:
            result["users"].append({"id": user["id"], "name": user["loginName"], "skills": user["skillIds"]})
    if survey_list:
        if "chat" in survey_list:
            for c_survey in survey_list["chat"]:
                result["surveys"]["preChatSurveys"].append({"name": c_survey["name"]})
        if "messaging" in survey_list:
            for s_survey in survey_list["messaging"]:
                result["surveys"]["cbSurveys"].append({"name": s_survey["botName"]})
    return result