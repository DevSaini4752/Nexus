"""This will be the final module that will bring all modules together and will
make them user-friendly, whole CLI would be developed here"""

#Importing all modules
from account_sys import account_maker
from account_sys import settings
from account_sys import forgot_password
import colours as c
from colours import ran_col as col
import news
import stocks_finance
import weather
import currency_finance
import smart_mail.newsletter_smartmail
from get_path import get_path
import json
import ToDoManager_modified.Main



#Function for registration
def register():
    """In this function it won't have any parameters, instead it would be directly used,
    all input, output, exceptions would be managed by this only."""

    try:
        #Taking all inputs
        username = input(f"Kindly enter your username : ").lower()
        password_0 = input(f"Kindly enter your password : ")
        password_1 = input(f"Kindly renter the password for confirmation : ")
        email = input(f"Kindly enter your email : ")


        #Checking passwords is same or not
        if password_0 != password_1:
            msg = f"{c.acidic_red}Invalid password: The confirmation password isn't same as previous one"
            return msg

        #Making the account
        account = account_maker.make_account(username, password_1, email)

        #Ending the process
        return account

    #Any unexpected error
    except Exception as ex:
        error = f"""{c.acidic_red}Unexpected Error Occurred !!!{c.end}\nError : {ex}{c.end}"""
        return error

#Function for login
def login():
    """In this function it won't have any parameters, instead it would be directly used,
        all input, output, exceptions would be managed by this only. Here function will
        return True if the password is correct and False if not

        And whatever this func returns, it should be in the list and the first element should
        tell whether the login succeeded or not by True/False"""

    try:
        username = input(f"{col()}Kindly enter your username : ").lower()
        password = input(f"{col()}Kindly enter your password : ")

        #Getting the path
        user_data_file_path = get_path("account_sys", "user_accounts", f"{username}.json")

        #Checking whether password is correct or not :)
        with open(user_data_file_path, "r") as file:
            user_data = json.load(file)

        if user_data["password"] != password:
            msg = f"{c.acidic_red}Invalid password!!! If you forgot the password, try forgot password option"
            print(msg)
            return [False]

        #If the password is okay
        print(f"{col()}Logged in successfully{c.end}")
        return True, username

    except FileNotFoundError:
        msg = f"{c.acidic_red}Invalid username, Try again !!!{c.end}"
        print(msg)
        return [False]


#Function to handle things after user logins
def after_login(username):
    """This function will handle all the things after user logins"""

    while True:
        options = input(f"""{col()}
So whats your choice !?
a. News
b. Stock market
c. Currency exchange
d. Weather
e. To Do Manager
f. Settings
g. Logout
{c.end}{col()}
Kindly choose one of the option (a/b/c/d/e) : {c.end}""").lower()



        if options == "a":
            opt_a = input(f"""{col()}\nWhat kind of news do you want user ?
a. Custom
b. From your personalization
c. Current affairs
Kindly choose one : {c.end}""").lower()

            if opt_a == "a":
                topic = input(f"""{col()}Kindly enter the topic of which news you want : """)
                print(news.getnews(topic, num_of_art_user_want=20))

            elif opt_a == "b":
                user_data = settings.get_data(username, structured=False)
                personalization = user_data["personalization"]

                #If we don't found and personalization is user data file
                if personalization is None or personalization == []:
                    print(f"{c.acidic_red}No personalization found, first put your personalization through settings")

                #If something is there
                else:
                    print(news.getnews(topic=personalization, num_of_art_user_want=20))

            elif opt_a == "c":
                print(news.getnews(num_of_art_user_want=20))


            else:
                print(f"{c.acidic_red}Invalid option, Try again !?")



        elif options == "b":
            #Taking input
            code = input(f"""{col()}Kindly put the code of the stock for e.g. Microsoft - MSFT : """)

            opt_b = input(f"""{col()}a. Get recent data\nb. Get of a specific date\nc. Get last day data
d. Get data of last day and a specific date\nSpecify (a/b/c/d) : {c.end}""").lower()

            #Acting according to condition
            if opt_b == "a":
                print(stocks_finance.get_stocks(code))

            elif opt_b == "b":
                date = input(f"{col()}Kindly enter the date of which data you want (format : YYYY-MM-DD) : ")
                print(stocks_finance.get_stocks(code, our_date=date))

            elif opt_b == "c":
                print(stocks_finance.get_stocks(code, latest_day=True))

            elif opt_b == "d":
                date = input(f"{col()}Kindly enter the date of which data you want (format : YYYY-MM-DD) : ")
                print(stocks_finance.get_stocks(code, our_date=date, latest_day=True))

            else:
                print(f"{c.acidic_red}Invalid option, Try again !!!{c.end}")



        elif options == "c":
            opt_c = input(f"""{col()}Do you want current rates or historical rates ?
a. Live/Current \nb. Historical \nc. List of currencies\na/b/c : """).lower()

            if opt_c == "a" or opt_c == "b":
                #Asking for currency code only if user chooses the first or second option
                currency = input(f"""{c.acidic_red}
Note : If you want multiple currencies together the kindly separate them with ',' and don't add 
       any extra space. e.g. - 'INR,USD,XYZ,ABC'
{c.end}
{col()}Kindly put the code of the the currency : {c.end}""")



            if opt_c == "a":
                print(currency_finance.live(currencies=currency))


            elif opt_c == "b":
                #Taking the inputs
                print(f"{col()}You can access the data of any day from 1999-01-01 to Today.\nThe format of date is - YYYY-MM-DD. Be cautions while putting the date{c.end}")
                date = input(f"{col()}Kindly put the date of which data you want : {c.end}")

                #Giving the output
                print(currency_finance.historical(date=date, currencies=currency))

            elif opt_c == "c":
                print(currency_finance.list_currencies())

            else:
                print(f"{c.acidic_red}Invalid option, Try again !!!")



        elif options == "d":
            location = input(f"{col()}Kindly enter the location : ")
            opt_d = input(f"{col()}In what unit do you want whether ?\na. Celsius b. Fahrenheit\na/b : ").lower()

            if opt_d == "a":
                print(weather.current_weather(celsius=True, location=location))

            else:
                print(weather.current_weather(location=location))


        elif options == "e":
            ToDoManager_modified.Main.main(username)


        elif options == "f":
            settings.settings(username)


        elif options == "g":
            print(f"{col()}\nLoging out....")
            break

        else:
            print(f"{c.acidic_red}Invalid option!!!{c.end}")

#Final function
def main():
    """This is the main function that will handle and execute everything"""
    print(f"{col()}Welcome user, I hope you will enjoy our services")

    #This function will run every time the user opens an application and will check
    # data and  will send the newsletters  to subscribers  according to  their time
    # period and date
    smart_mail.newsletter_smartmail.send_news()

    while True:
        try:
            options = input(f"""{col()}\na. Register\nb. Login\nc. Forgot Password\nKindly choose one of the option a/b : """).lower()

            #If the user wants to register
            if options == "a":
                print(register())

            #For login
            elif options == "b":
                login_check = login()

                #Checking whether user is logged in or not
                #If yes
                if login_check[0]:
                    after_login(login_check[1])

                #If user fails then it is already handled in login func


            #If the user forgets password
            elif options == "c":
                username = input(f"{col()}Kindly enter your username : {c.end}").lower()
                new_password = input(f"{col()}Kindly enter your new password : {c.end}")

                print(forgot_password.reset_pass(username, new_password))

            else:
                print(f"{c.acidic_red}Invalid option!!!{c.end}")

        #For any unexpected error occurred as most of them are already handled
        except Exception as ex:
            print(f"{c.acidic_red}Unexpected Error Occurred!!!\nError: {ex}")

#Trial and testing
if __name__ == "__main__":
    main()
