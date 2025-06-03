"""This module made to stock market APIs and give data to user -
APIs we are going to use -
    - Marketstack (100 requests per month)
    - Finhub.io (60 requests per minute)(Back up)

The user will be asked for the code of the stock about whom they want to know
in the main.py. Then that  input will be given to this module, and  this will
give that code to API and will return the data to the user in a better format."""

#Importing prerequisites modules
from datetime import datetime
import requests
import colours as c
from colours import ran_col as col

#Some useful variable
key = '2fb2ec09d702bd8ab2126cc94884d8d6'
url = 'https://api.marketstack.com/v2/eod?'

#e.g. https://api.marketstack.com/v2/eod?access_key=2fb2ec09d702bd8ab2126cc94884d8d6&symbols=AAPL

live_time = str(datetime.now())[0:11]

#Function
def get_stocks(code='AAPL', date=None, today=False):
    """
    Conditions and Actions -
    1. today=False and date=None - Then we will just give the recent  data what the API
    returns

    2. today=True and date=None - Then we will return the data of today/latest day data
    available

    3. today=True and date=Some date - Then we will return data of today or latest day
    data we have and data of the date the user wants

    4. date=Some date and today=False - Then we will return the  data of that day, but
    if its in out  range as we can only access past one-year  data because of our free
    plan.

    """

    #Condition 1
    if date is None and today is False:

        #Action
        parameters = {
            'access_key' : key,
            'symbols' : code
        }

        data = (requests.get(url, params=parameters)).json()

        # If error occurs
        if "error" in data:

            #If the user hasn't put a valid code for a stock
            if data["error"]["code"] == "no_valid_symbols_provided":

                output = f"""{c.acidic_red}!!!Error occurred!!!
                        Error : {data["error"]["code"]}
                        Info  : Kindly put a valid code/symbol of stock, For e.g. Apple Inc - AAPL
                        """
                return output

            output = f"""{c.acidic_red}!!!Error occurred!!!
        Error : {data["error"]["code"]}
        Info  : {data["error"]["message"]}
        """
            return output

        days_of_data = len(data["data"])
        name_of_stock = data["data"][0]["name"]


        #If everything goes fine
        #Intro of output
        output = f"""{c.electric_Blue}Here is your data - 
Stock Name : {name_of_stock}
Data of past {c.end}{c.acidic_red}{days_of_data}{c.end}{c.electric_Blue} days

"""

        for n in range(days_of_data):
            day = data["data"][n]
            to_be_add = f"""{col()}Date: {day["date"]}
Open  : {day["open"]}{day["price_currency"]}
High  : {day["high"]}{day["price_currency"]}
Close : {day["close"]}{day["price_currency"]}

"""
            output += to_be_add

        return output


    #Condition 2
    elif today is True and date is None:
        pass

    #Condition 3
    elif today is True and date is not None:
        pass

    #Condtion 4
    elif date is not None and today is False:
        pass


#Trials and testing
if __name__=="__main__":
    x = get_stocks(code="TSLA")
    if x is not None:
        print(x)

    x= get_stocks(code="Choco")
    if x is not None:
        print(x)

    x= get_stocks(today=True)
    if x is not None:
        print(x)

    x= get_stocks(date="2024-09-05")
    if x is not None:
        print(x)

    x= get_stocks(date="2024-09-05", today=True)
    if x is not None:
        print(x)
