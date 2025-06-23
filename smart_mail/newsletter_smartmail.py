"""
This module will be used to send newsletters to user. What will this do -
    - Check the subscribers in subscribers.json
    - Check for their frequency
    - Will check the last mail sent to them for news purpose
    - Will send the news if timeperiod completes
"""

#Importing modules
import json
import news
import datetime
from .smart_mail import sending
from get_path import get_path


path_subscribers = get_path("account_sys", "subscribers.json")
path_user_accounts = get_path("account_sys", "user_accounts")

# Load JSON data
with open(f"{path_subscribers}", 'r') as f:
    subscribers = json.load(f)
    keys_subs = subscribers.keys()

#Functions
#Function to check who has what personalization and will send mail
def send_news():
    live_time = str(datetime.datetime.now())[0:10]

    #Running a loop to get to each user individually and check there frequency....
    for key in keys_subs:
        with open(f"{path_user_accounts}/{key}.json", "r") as file:
            user_data = json.load(file)

        topic = user_data["personalization"]
        frequency = user_data["smartmail_frequency"]

        days_difference = 0

        #If it's not the user's first smart mail then finding difference of days between previous and present date
        if user_data["last_news_mail_sent_date"] != "":
            last_news_mail_sent_date = datetime.datetime.strptime(user_data["last_news_mail_sent_date"], "%Y-%m-%d")
            live_time = datetime.datetime.strptime(live_time, "%Y-%m-%d")
            days_difference = (last_news_mail_sent_date - live_time).days


        #If the user's time period completed to send next mail or if no mail is sent before
        if days_difference >= frequency or user_data["last_news_mail_sent_date"] == "":

            #Defining the var earlier so that there is no need of using a global statement
            newsletter = ""

            #If a user wants personalized news
            if topic != "" and not topic is None and topic != []:
                newsletter = news.getnews(topic=topic)

            #If a user just wants news and personalization is empty
            elif topic == "" or topic is None or topic == []:
                newsletter = news.getnews()

            subject = "Nexus Newsletter"
            content = f"""Here is your latest news - 
{newsletter}"""

            #Sending mail
            sending(content, subject, to=user_data["email"])

            #Updating data in user's data, updating only if news is sent
            user_data["last_news_mail_sent_date"] = live_time
            user_data["last_mail_sent_time"] = live_time

            with open(f"{path_user_accounts}/{key}.json", "w") as file:
                json.dump(user_data, file, indent=4)

#Trial and testing
if __name__ == "__main__":
    send_news()