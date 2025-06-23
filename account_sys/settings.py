"""This module will provide access of the following to the user -
    - Security -
        - Change password ✅
        - Reset Account ✅
        - Change Email ✅
        - Delete Account

    - View Data ✅
    - Start or End subscription ✅
    - Personalization ✅

I will make such a function and all which would be perfect for direct
execution (it would have its own CLI),  all inputs and print function
would be used"""

#Importing modules
import json
import colours as c
from colours import ran_col as col
import account_sys.subscription as subscription
import account_sys.forgot_password as forgot_password
import account_sys.reset_account as reset_account
import os
import sys
from smart_mail import smart_mail
import random
from get_path import get_path

#Path for subscribers.json
subscribers_path = get_path("account_sys", "subscribers.json")

#Functions for different purposes
#For extracting the data of the user
def get_data(username, structured=True):
    try:
        # Getting the path so that we can access that file anywhere
        indi_acc_path = get_path("account_sys", "user_accounts", f"{username}.json")

        with open(f"{indi_acc_path}", "r") as file:
            user_data = json.load(file)
            pass_date = user_data["dates_of_password_change"]
            personalization = user_data["personalization"]
            if pass_date != [] and pass_date is not None:
                pass_date = ", ".join(pass_date)

            if personalization is not None and personalization != []:
                personalization = ", ".join(personalization)

        #Returning structured data
        if structured:
            struc_out = f"""{col()}
Username - {user_data["username"]}
Password - {user_data["password"][0:1]}*****{user_data["password"][-1:]}
Password changing dates - {pass_date}
Email - {user_data["email"]}
Personalized topics - {personalization}
Frequency of newsletter - {user_data["smartmail_frequency"]}
Account making date - {user_data["account_making_date"]}
Last mail date - {user_data["last_mail_sent_time"]}
Last newsletter mail - {user_data["last_news_mail_sent_date"]}
Do you have newsletter subscription - {user_data["have_smart_mail_news_subscription"]}
"""

            return struc_out

        #Returning raw data
        elif not structured:
            return user_data

    except FileNotFoundError:
        msg = f"{c.acidic_red}Invalid username!!! No such username exists, recheck it !{c.end}"
        return msg





#Function for editing personalization of user's news
def personalisation(username):

    # Getting the path so that we can access that file anywhere
    indi_acc_path = get_path("account_sys", "user_accounts", f"{username}.json")

    user_data = get_data(username=username, structured=False)
    topics = input(f"""Kindly write the topics you love or like to get news about and write it in the following format - 
Format : topic1,topic2,topic3....(separate with a comma)
Topics : """)
    topics_list = topics.split(",")

    #If in data personalization in None, then....
    if user_data["personalization"] is None:
        user_data["personalization"] = []

    #Adding topics
    for topic in topics_list:
        user_data["personalization"].append(topic)

    #Saving the updated data
    with open(f"{indi_acc_path}", "w") as file:
        json.dump(user_data, file, indent=4)

    #Ending the process
    print(f"Topics Added successfully!!!")





#Function for changing email
def change_mail(username, updated_email):
    # Getting the path so that we can access that file anywhere
    indi_acc_path = get_path("account_sys", "user_accounts", f"{username}.json")

    user_data = get_data(username, structured=False)
    user_data["email"] = updated_email

    #Updating data
    with open(f"{indi_acc_path}", "w") as file:
        json.dump(user_data, file, indent=4)

    return f"{col()}Data updated successfully !!!"





#Function of deleting the account
def delete_account(username):
    y_or_n = input(f"""{c.acidic_red}Are you sure (Y/n) : """).lower()

    if y_or_n == "y":
        print(f"Deleting the account ({username})....!!!")

        #Getting the path for an account file
        path_user_account = get_path("account_sys", "user_accounts", f"{username}.json")

        #Deleting
        os.remove(path_user_account)
        print("Account deleted successfully !!!")

        with open(f"{subscribers_path}", "r") as file:
            subs = json.load(file)

        #Trying to delete the user's name from the list, and if they are not there,
        # then we will let it pass
        if username in subs:
            del subs[username]

        with open(f"{subscribers_path}", "w") as file:
            json.dump(subs, file)

    elif y_or_n == "n":
        print(f"{c.acidic_red}Cancelling the deletion of account !!!{c.end}")

    else:
        print(f"{c.acidic_red}Invalid input !!!, Cancelling the deletion of account....")





#Function for verifying email
def email_verification(email):
    #Generating token of 6 digit
    token = str(random.randint(100000, 999999))

    #Defining the material of email
    subject = f"""Verification Token"""
    content = f"""Here is your verification code for this mail - {token}"""

    # Sending the mail
    smart_mail.sending(subject=subject, content=content, to=email)


    # Asking for the token
    verifying = input(f"""A 6 digit token has been sent on the email you gave ({email}), 
    Check for the token in SPAM if not found.
    Kindly put that token : """)

    if verifying == token:
        return True

    else:
        return False


#Final function
def settings(username):
    while True:
        options = input(f"""{col()}
Settings....
    - a. Security
    - b. View Data
    - c. Start or End subscription
    - d. Personalization
    - e. exit

Kindly choose one of the option : """).lower()

        if options == "a":
            opt_a = input(f"""{col()}
        - a. Change password
        - b. Reset Account
        - c. Change Email
        - d. Delete Account

Kindly choose a option - {c.end}""").lower()

            if opt_a == "a":#✅
                new_pass = input(f"{c.acidic_red}Enter your new password : ")
                print(forgot_password.reset_pass(username=username, new_password=new_pass))

            elif opt_a == "b":#✅
                password = input(f"{col()}Kindly enter your account password : {c.end}")
                print(reset_account.reset_account(username, password))

            elif opt_a == "c":
                updated_email = input(f"{col()}Kindly enter the updated email : ")

                #Verifying the email
                mail_check = email_verification(updated_email)

                #Emailverification returns True for verified mail (correct token) and
                # False unverified (wrong token)
                if mail_check:
                    print(change_mail(username, updated_email))

                elif not mail_check:
                    print(f"{c.acidic_red}You entered wrong token, failed to update. Try again !!!")

            elif opt_a == "d":
                delete_account(username)

                #Stopping the whole program because user would be logged in at the time of
                # deletion, and if them they  try to do something, then it would give error.

                #So if we stop it, then user would have re-login and there they won't find
                # there account

                sys.exit()


            else:#✅
                print(f"{c.acidic_red}Invalid Option !!!{c.end}")

        elif options == "b":#✅
            print(get_data(username))
            break

        elif options == "c":
            add_remove = input(f"""What do you want -
a. Start/Update subscription
b. End subscription
Kindly choose a option (a/b) : """).lower()

            if add_remove == "a":
                frequency = input(f"{col()}What should be the frequency of newsletter (in days), pls enter a integer only : {c.end}")
                print(subscription.add_remove_subscriber(username, frequency))

            elif add_remove == "b":
                print(subscription.add_remove_subscriber(username, add=False))

            else:
                print(f"{c.acidic_red}Invalid input !!!")

        elif options == "d":#✅
            personalisation(username=username)
            break

        elif options == "e":#✅
            break

        else:#✅
            print(f"{c.acidic_red}Invalid option !!!{c.end}")

#Trial and testing
if __name__ == "__main__":
    settings("Hulk")