"""
This module would be used to reset password. User will be using this module
if they want to reset their password.
"""

#Importing modules
import json
import colours as c
import decouple
from colours import ran_col as col
import random
from smart_mail import smart_mail
from datetime import datetime

#Getting variables from .env
sys_mail = decouple.config("MAIL_FOR_SMART_MAIL")
app_pass = decouple.config("GMAIL_APP_PASSWORD")

#Function
def reset_pass(username, new_password):
    try:
        #Openening the file and getting the data (mail, passw, etc.)
        with open(f"user_accounts/{username}.json", "r") as file:
            data = json.load(file)
            user_email = data["email"]

        #Generating verification token
        token = str(random.randint(100000, 999999))

        #Sending the verification token
        subject = "Verification token for Password reset"
        content = f"""This mail has been sent from NEXUS and we want to verify that you are the only one who is 
try to change the password so pls enter the token....
Token : {token}"""

        smart_mail.sending(content=content, subject=subject, to=user_email)

        #Taking the input and verifying
        user_token = input(f"""{col()}A email has been sent to you containing the token for verifying it's you....
Kindly insert the token : """)

        if user_token == token:
            print(f"{col()}Correct Token!!!, Verified....")

        else:
            msg = f"{c.acidic_red}Invalid token, You failed to pass the verification....Try Again!!!"
            return msg

        #Changing the password and updating data
        data["password"] = new_password
        data["is_logged_in"] = False
        data["last_mail_sent_time"] = str(datetime.now())[0:10]
        data["dates_of_password_change"].append(str(datetime.now())[0:10])

        #Updating password at the file
        with open(f"user_accounts/{username}.json", "w") as file:
            json.dump(data, file, indent=4)

        #Ending the process
        return f"{col()}Password changed successfully{c.end}"


    #If user gives invalid username then we would not be able to find the file as the files are named behind the username
    except FileNotFoundError:
        msg = f"""{c.acidic_red}Error: Invalid username, No such username exists in our system
    -> Kindly recheck for the username!!!{c.end}"""
        return msg

    # If any other error occurs
    except Exception as ex:
        return f"{c.acidic_red}Error : {ex}{c.end}"

#Trial and testing
if __name__ == "__main__":
    #Checking for the wrong username
    print(reset_pass("hello", "12none"))

    #Trying to change of a real account I had made earlier
    print(reset_pass("Dev", "123321"))

    #Trying wrong token
    print(reset_pass("Dev", "123321"))