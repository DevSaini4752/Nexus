"""
This module will be used if the user wants to get or leave the subscription of newsletter.
What will this do -
    - Make/Edit a file named "subscribers.json" and will put the username of user in a dictionary
    - The key would contain username and the value would time period
    - Through the list system will decide who has the subscription
    - Remove username from the list if the account is deleted/reset
"""

#Importing modules
import json
import colours as c
from colours import ran_col as col

#Function
#This function would be used to add the username or update frequency
def add_remove_subscriber(username, frequency, personalization=None, add=True):
    #If add=True then will add the user
    #If add=False then will remove the user
    try:
        #Turning on the subscription in accounts data (in user_accounts)
        with open(f"user_accounts/{username}.json", "r") as file:
            account_data = json.load(file)

        if add:
            account_data["have_smart_mail_news_subscription"] = True
            account_data["smartmail_frequency"] = frequency

            if personalization is None:
                #This will not remove already existing personalization
                pass

            elif not personalization is None:
                account_data["personalization"] = personalization

        elif not add:
            account_data["have_smart_mail_news_subscription"] = False
            account_data["smartmail_frequency"] = None
            account_data["personalization"] = []

        with open(f"user_accounts/{username}.json", "w") as file:
            json.dump(account_data, file, indent=4)

        #Updating the list of subscribers
        with open("subscribers.json", "r") as file:
            data = json.load(file)

        #Adding/Updating the user
        if add:
            data[username] = frequency

        #Removing the user
        if not add:
            del data[username]

        with open("subscribers.json", "w") as file:
            json.dump(data, file, indent=4)

        #Ending the process
        return f"{col()}Subscribers Updated !!!{c.end}"

    except FileNotFoundError:
        return f"{c.acidic_red}Invalid username!!! - No such username exists{c.end}"

    except KeyError:
        return f"{c.acidic_red}You were already not a subscriber!!!{c.end}"

#Trial and testing
if __name__ == "__main__":
    #Trying with a wrong username (Adding)
    print(add_remove_subscriber("Iron Man", 7))

    #Trying with a right username (Adding)
    print(add_remove_subscriber("Dev", 7, personalization=["Dogs", "War", "Cars"]))

    #Trying with a wrong username (Removing)
    print(add_remove_subscriber("Iron Man", 7, add=False))

    #Trying with a right username (Removing)
    print(add_remove_subscriber("Spider Man", 7, add=False))
