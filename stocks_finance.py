"""This module made to stock market APIs and give data to user -
APIs we are going to use -
    - Marketstack (100 requests per month)

The user will be asked for the code of the stock about whom they want to know
in the main_nexus.py. Then that  input will be given to this module, and  this will
give that code to API and will return the data to the user in a better format.
"""

"""
Important note:
    - Our API can't return the present-day data, and it allways gives you a day old data

Conditions and Actions -

1. latest_day=False and our_date=None - Then we will just give the recent  data what the API
returns

2. latest_day=True and our_date=None - Then we will return the data of today/latest day data
available

3. our_date=Some date and latest_day=False - Then we will return the  data of that day, but
if its in out  range as we can only access past one-year  data because of our free
plan.

4. latest_day=True and our_date=Some date - Then we will return data of today or latest day
data we have and data of the date the user wants

"""

#Importing prerequisites modules
from datetime import datetime, date, timedelta
import requests
import colours as c
from colours import ran_col as col
import decouple

#Bringing key
key = decouple.config("MARKETSTACK_API_KEY")

#e.g. https://api.marketstack.com/v2/eod?access_key=YOUR_ACESS_KEY&symbols=AAPL

#dates
live_time = str(datetime.now())[0:11]
yesterday_str = str(date.today() - timedelta(days=1))



#Function (if error occurs)
def error_check_from_api(data):
    # If error occurs
    if "error" in data:

        # If the user hasn't put a valid code for a stock
        if data["error"]["code"] == "no_valid_symbols_provided":
            output = f"""{c.acidic_red}!!!Error occurred!!!
                    Error : {data["error"]["code"]}
                    Info  : Kindly put a valid code/symbol of stock, For e.g. Apple Inc has symbol/code - AAPL
                                    """
            return output

        output = f"""{c.acidic_red}!!!Error occurred!!!
                    Error : {data["error"]["code"]}
                    Info  : {data["error"]["message"]}
                    """
        return output




#Functions for every condition

#Condition 1
def get_all_recent_data(code='AAPL'):

    #Action
    url = 'https://api.marketstack.com/v2/eod?'

    parameters = {
        'access_key' : key,
        'symbols' : code
    }

    data = (requests.get(url, params=parameters)).json()

    # If error occurs from the API side
    ex_check = error_check_from_api(data)
    if ex_check is not None:
        return ex_check

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
        to_be_add = f"""{col()}Date: {day["date"][0:10]}
Open  : {day["open"]}{day["price_currency"]}
High  : {day["high"]}{day["price_currency"]}
Close : {day["close"]}{day["price_currency"]}
{c.end}
"""
        output += to_be_add

    return output





#Condition 2
def get_latest_day(code='AAPL'):

    # Action
    url = 'https://api.marketstack.com/v2/eod/latest?'

    parameters = {
            'access_key': key,
            'symbols': code
    }

    data = (requests.get(url, params=parameters)).json()

    # If error occurs from the API side
    ex_check = error_check_from_api(data)
    if ex_check is not None:
        return ex_check

    # If everything goes fine
    that_day_data = data["data"][0]

    # Output
    output = f"""{c.electric_Blue}Here is your data of yesterday (as that is the latest data we have)- 
Stock Name : {data["data"][0]["name"]}
{col()}Date: {that_day_data["date"][0:10]}
Open  : {that_day_data["open"]} {that_day_data["price_currency"]}
High  : {that_day_data["high"]} {that_day_data["price_currency"]}
Close : {that_day_data["close"]} {that_day_data["price_currency"]}
{c.end}
        """

    return output






#Condition 3
def get_date_data(code='AAPL', our_date=yesterday_str):
    url = f'https://api.marketstack.com/v2/eod/{our_date}?'

    parameters = {
        'access_key': key,
        'symbols': code
    }

    data = (requests.get(url, params=parameters)).json()

    # If error occurs from the API side
    ex_check = error_check_from_api(data)
    if ex_check is not None:
        return ex_check

    data_sub = data['data'][0]
    output = f"""{col()}Here is your data for {code} -{c.end}
{col()}
Date : {our_date}
Open  : {data_sub["open"]} {data_sub["price_currency"]}
High  : {data_sub["high"]} {data_sub["price_currency"]}
Close : {data_sub["close"]} {data_sub["price_currency"]}
{c.end}
"""

    return output


#Condition 4
def get_both(code='AAPL', our_date=yesterday_str):
    #Condtion2 function returns the data of the latest day, condition3 function returns data of a specific date,
    # and we need both of them so instead of writing a lot of code, I will use those 2 func

    con2 = get_latest_day(code=code)
    con3 = get_date_data(code=code, our_date=our_date)

    output = f"{con2}\n\n{con3}"

    return output





# Main Function :)
def get_stocks(code='AAPL', our_date=None, latest_day=False):

    #Condition 1
    if our_date is None and latest_day is False:
        return_or_not = get_all_recent_data(code=code)

        if return_or_not is not None:
            return return_or_not

#-------------------------------------------------------------------------------------------------------------------------------------------------#

    #Condition 2
    elif latest_day is True and our_date is None:
        return_or_not = get_latest_day(code=code)

        if return_or_not is not None:
            return return_or_not

# ------------------------------------------------------------------------------------------------------------------------------------------------#

    # Condition 3
    elif our_date is not None and latest_day is False:
        return_or_not = get_date_data(code=code, our_date=our_date)

        if return_or_not is not None:
            return return_or_not

# -------------------------------------------------------------------------------------------------------------------------------------------------#

    #Condition 4
    elif latest_day is True and our_date is not None:
        return_or_not = get_both(code=code, our_date=our_date)

        if return_or_not is not None:
            return return_or_not


#Trial and testing
if __name__=="__main__":
    #Checking for error
    print(f"""Checking for errors -
Wrong code of stock-
{get_stocks(code='HELLO')}

Wrong date
{get_stocks(our_date='1220981-1381-123497')}

Out of range date
{get_stocks(our_date='2020-01-01')}""")

    #Checking for normal cases
    print(f"""
Checking for normal cases - 

Get recent data
{get_stocks(code='MSFT')}

Get of a specific date 
{get_stocks(code='MSFT', our_date='2024-11-19')}

Get of last day
{get_stocks(code='MSFT', latest_day=True)}

Get of latest and specific date 
{get_stocks(code='MSFT', our_date='2024-11-19', latest_day=True)}

""")