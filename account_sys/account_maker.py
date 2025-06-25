"""So this module will make accounts in the JSON file, What will a system do:
    - The system would make a unique JSON file for every user.
    - The name of the JSON file would be the username.
    - A history JSON file would also be there which would store all the usernames the system ever had.
    - A default JSON file would be there which will have the format of all the json files but with no data
    - If a user resets the account, then the material of default will be copied to it.
"""

#Importing modules
import json
import os
import decouple
from get_path import get_path
from smart_mail import smart_mail
import random
import colours as c
from colours import ran_col as col
import datetime

#Getting the paths
default_path = get_path("account_sys", "default.json")
history_path = get_path("account_sys", "history.json")

#Getting the data to put in a new account
with open(f"{default_path}", "r") as file:
    data_format = json.load(file)

#Func for making an account
def make_account(username, password, email, wanted_topics=None):
    #Verifying whether there was no same username in the system
    with open(f"{history_path}", "r") as history_file:
        history = json.load(history_file)

    if username in history["usernames"]:
        msg = f"{c.acidic_red}Kindly choose another username as this username has been already used{c.end}"
        return msg

    #Verifying email
    """This function will itself ask for input of the token"""

    #Generating token of 6 digit
    token = str(random.randint(100000, 999999))

    #Defining the material of email
    subject = f"""Verification Token"""
    content = f"""Here is your verification code for this mail - {token}"""

    #Sending the mail
    smart_mail.sending(subject=subject, content=content, to=email)

    #Live time for store time of last mail
    live_time = str(datetime.datetime.now())

    #Asking for the token
    verifying = input(f"""A 6 digit token has been sent on the email you gave ({email}), 
Check for the token in SPAM if not found.
Kindly put that token : """)

    if verifying == token:
        print(f"{col()}Correct token !!!, Email verified...{c.end}")

    else:
        msg = f"User failed to verify the email, {c.acidic_red}Try Again!!!{c.end}\n"
        return msg

    #Making the directory, if not found
    path_for_dir = get_path("account_sys", "user_accounts")
    if not os.path.exists(path_for_dir):
        os.makedirs(path_for_dir)

    #Making the account if email is verified

    #Getting the path of that individual account
    indi_acc_path = get_path("account_sys", "user_accounts", f"{username}.json")

    with open(f"{indi_acc_path}", "w") as account_file:
        #Editing the data according to need
        data_format["username"] = username
        data_format["password"] = password
        data_format["email"] = email
        data_format["is_logged_in"] = False
        data_format["last_mail_sent_time"] = live_time[0:10]
        data_format["personalization"] = wanted_topics
        data_format["account_making_date"] = live_time
        data_format["have_smart_mail_news_subscription"] = False

        json.dump(data_format, account_file, indent=4)

    #Updating the history of username
    history["usernames"].append(username)

    with open(f"{history_path}", "w") as update_hist:
        json.dump(history, update_hist, indent=4)


    #Also making a data file of user for TDM in user_accounts_TDM dir
    # Will use 'databackup.json' file to take default format/structure
    path_for_databackup = get_path("ToDoManager_modified", "databackup.json")
    with open(path_for_databackup, "r") as file_TDM:
        format_tdm = json.load(file_TDM)

    acc_data_path_tdm = get_path("ToDoManager_modified", "user_accounts_TDM", f"{username}.json")
    with open(acc_data_path_tdm, "w") as file_acc:
        json.dump(format_tdm, file_acc, indent=4)

    return f"{c.ran_col()}Account created successfully!!!{c.end}\n"

#Trials and testing
if __name__ == "__main__":
    #Getting my mail for testing
    mail = decouple.config("MY_PERSONAL_MAIL")
    print(make_account(username="Dev", password="123456789", email=mail))

    #Checking if raising error on same usernames works fine
    print(make_account(username="Dev", password="123456789", email=mail))