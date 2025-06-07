"""This module will be used for all the works related to currency rates
asked by user.

Accessibility of our API's free plan API -
    - Can get live currency values
    - Can access all currency they have (listed in currency_list.json)
    - Can't change base currency (through which all currencies are compared)
    - Can get all historical data till 1999 (date format: YYYY-MM-DD)"""

"""
Things we should know -
    Base currency : USD
    Endpoints : 'live'
              : 'historical'
              
    Returned currency format : [Base Currency][Currency] - For e.g. INR -> USDINR
    Multiple currencies: Separate currencies by comma
    
    Parameters : access_key
               : date
               : currencies
    
Possible conditions (for user) : 
    1. Get all currencies live
    2. Get all currencies of specific date
    3. Get single currency of live
    4. Get single currency of specific date
    5. Get multiple currencies of live
    6. Get multiple currencies of specific date
    
How will we handle conditions - 

We would have a function and it parameters would be 
"""

#Importing modules
import decouple
import requests
import colours as c
from colours import ran_col as col
import json
import datetime

#Extracting key
key = decouple.config("CURRENCYLAYER_API_KEY")

#Base url
base_url = "https://api.currencylayer.com/"

#Getting the list of currencies
with open("currencies_list.json", "r") as file:
    currencies_list = json.load(file)["currencies"]

#Error checker
#API allways return success status
def error_check(data, currencies=None):
    if not data["success"]:

        code = str(data["error"]["code"])

        #Finding error info through code
        with open("currency_API_errors.json", "r") as file_ex:
            errors = json.load(file_ex)
            error = errors[code]

        output = f"""{c.acidic_red}!!!ERROR OCCURRED!!!
        Success     : {data["success"]}
        Error Code  : {code}
        Info        : {error}"""

        return output

    #If currency code is not in the list

    output = f"{c.acidic_red}!!!ERROR OCCURRED!!! - The currency code you gave is probably invalid or not in our list{c.end}"
    if not currencies is None:
        for curr in currencies:
            if not curr in currencies_list:
                return output


##Functions
#For current data
def get_currencies(params={"access_key": key}, url=f"{base_url}/live?"):

    # Getting and converting data into readable form
    response = requests.get(url, params=params)
    data = response.json()

    # Checking error
    ex_check = error_check(data)
    if ex_check is not None:
        return ex_check

    #Getting date from data
    #Coverting the epoch into readable time
    timestamp = data["timestamp"]
    date = datetime.datetime.fromtimestamp(timestamp)

    output = f"""{col()}
Success : {data["success"]}
Base Currency (Through which other currencies are compared) : USD
Date Collection date (exact time when data was collected): {date}

Currency Code : Currency Name : Currency Value
{c.end}"""

    #Will use curr
    data_quotes = data['quotes']
    data_keys = list(data_quotes.keys())

    for user_curr in data_keys:
        value = data_quotes[user_curr]

        #Taking out currency code as API returns it as 'USD' at frontend and code at end
        user_curr = user_curr[3:]
        #Preparing final material to be added
        add = f"\n{col()}{user_curr} : {currencies_list[user_curr]} : {value}"

        output += add
    return output


#Final function which would be the real show casers
def live(currencies=None):
    #Currencies must be in list type
    #Seprating depending-on-currencies parameter value

    #If no currencies are specified, then we will give whatever we get
    if currencies is None:
        params = {
            "access_key" : key
        }
        return get_currencies(params=params)

    #If currencies are specified
    elif isinstance(currencies, list):
        params = {
            'currencies': currencies,
            'access_key': key
        }

        return get_currencies(params=params)

    #If something unexpected happens, like our system doesn't pass as a list whatever they gave
    else:
        return f"{c.acidic_red}Unexpected error !!!{c.end}"



def historical(date, currencies=None):
    # If no currencies are specified, then we will give whatever we get
    if currencies is None:
        params = {
            "access_key": key,
            "date" : date
        }

        return get_currencies(params=params, url=f"{base_url}/historical?")

    # If currencies are specified
    elif isinstance(currencies, list):
        params = {
            'currencies': currencies,
            'access_key': key,
            'date' : date
        }

        return get_currencies(params=params, url=f"{base_url}/historical?")

    # If something unexpected happens, like our system doesn't pass as a list whatever they gave
    else:
        return f"{c.acidic_red}Unexpected error !!!{c.end}"


if __name__=="__main__":
    print(f"""
Live - All
{live()}""")

    print(f"""
Live - Specified
{live(["INR", "JPY"])}""")

    print(f"""
Historical - All
{historical(date="2025-06-01")}""")

    print(f"""
Historical - specified
{historical(date="2025-06-01", currencies=["INR", "JPY"])}""")

    print(f"""
Checking errors
Wrong code

{live(currencies=["HI", "BYE"])}""")

    print(f"""
{historical(date="1999-01-01", currencies=["HI"])}""")

    print(f"""
Out of range date
{historical(date="1990-01-01")}""")

    print(f"""
Wrong date
{historical(date="123-456-678")}""")
