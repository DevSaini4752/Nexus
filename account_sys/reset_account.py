"""This module will be used if user wants to reset the account. This will do -
    - Remove data of -
        - personalization
        - last_mail_sent_time
        - total_num_mail_till_now

    - Log out the user
    - Turn off the subscription of smart_mail_for_news
    - Make smart mail frequency to null
"""

#Importing modules
import json
import colours as c
from colours import ran_col as col

#Function
def reset_account(username, password):
    try:
        #Checking if the password is correct
        with open(f"user_accounts/{username}.json", "r") as file:
            data = json.load(file)
            original_pass = data["password"]

        if not password == original_pass:
            msg = f"{c.acidic_red}Invalid password!!!, Try Again....{c.end}"
            return msg

        #Reseting data of the account
        #Getting the data of default
        with open("default.json", "r") as default:
            default = json.load(default)

        #Keeping some imp data as it is
        default["username"] = data["username"]
        default["password"] = data["password"]
        default["email"] = data["email"]
        default["account_making_date"] = data["account_making_date"]

        #Updating data of the user account (resetting)
        with open(f"user_accounts/{username}.json", "w") as file:
            json.dump(default, file, indent=4)

        #Removing name from the subscriber list
        with open("subscribers.json", "r") as file:
            subscribers = json.load(file)
            del subscribers[data["username"]]

        with open("subscribers.json", "w") as file:
            json.dump(subscribers, file)

        #Ending the process
        return f"{col()}Account has been reset successfully!!!"



    # If user gives invalid username then we would not be able to find the file as the files are named behind the username
    except FileNotFoundError:
        msg = f"""{c.acidic_red}Error: Invalid username, No such username exists in our system
            -> Kindly recheck for the username!!!{c.end}"""
        return msg

    # If any other error occurs
    except Exception as ex:
        return f"{c.acidic_red}Error : {ex}{c.end}"

#Trial and testing
if __name__ == "__main__":
    #Checking for the wrong account by wrong username
    print(reset_account("hello", "12345"))

    #Checking for wrong password
    print(reset_account("Dev", "i dont know"))

    #Cheking for correct procedure
    print(reset_account("Dev", "123456789"))