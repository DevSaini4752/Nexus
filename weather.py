"""
Here we will make a function which will work with weatherstack API and
will return weather depending on the parameters given.

The function will take the following arguments -
    - time (current/historical/historical_series/forecast, default: current)
    - unit (metric/fahrenheit/scientific/celsius, default: celsius, f will be converted to c)
    - location (default: New Delhi)
    - historical_date (if historical)
    - historical_date_start (if time series historical)
    - historical_date_end (if time series historical)
    - forecast_days (Of how many days forecast user need, default: 7)
"""

#Importing Prerequisites
import requests
import colours as c
from colours import ran_col as col
import time
from datetime import date

#Func
def weather(hist=None, hist_start=None, hist_end=None, time_weather="current", unit="c", location="New Delhi", celsius=False):
    # - 4 categories would be there, for historical, historical time series, forcast, current
    if time_weather == "current":
        current(unit=unit, location=location, celsius=celsius)

    elif time_weather == "historical":
        if hist is None:
            return f"{c.acidic_red}Error: Past date or past time series date is not inserted properly{c.end}"

        historical(hist=hist, unit=unit, location=location, celsius=celsius)

    elif time_weather == "historical_series":
        if hist_start is None:
            return f"{c.acidic_red}Error: Past date or past time series date is not inserted properly{c.end}"

        historical_series(hist_start=hist_start, hist_end=hist_end, unit=unit, location=location, celsius=celsius)

    elif time_weather == "forecast":
        forecast(unit=unit, location=location, celsius=celsius)

    else:
        return f"""{c.acidic_red}Error: 'time(current/historical/historical_series/forecast)' not specified{c.end}"""


#Function if user wants current weather
def current(unit="c", location="New Delhi", celsius=False):

    url = "https://api.weatherstack.com/current?"
    key = 'd02d6a1f40206cd47f8e0267f2a45e7c'
    params = {
        'query' : location,
        'access_key' : key,
        'units' : unit
    }

    data = (requests.get(url, params=params)).json()

    #If error occurs then program will return this, and this will only work when
    # success key is there because success key is only there when error occurs

    if 'success' in data:
        error = f"""Success : {data['success']}
What happened : {data['error']['info']}"""
        return error


    #Changing the fahrenheit to celsius if wanted
    if celsius:
        data['current']['temperature'] -= 32
        data['current']['temperature'] *= 5/9

    #Unit
    if unit == 'f':
        data['request']['unit'] = 'Fahrenheit'
    elif unit == 'm':
        data['request']['unit'] = 'Metric'
    elif unit == 's':
        data['request']['unit'] = 'Scientific'
    if celsius:
        data['request']['unit'] = 'Celsius'

    #Specifiying that what values has to be returned to user
    output = f"""{col()}
Time Zone : {data['location']['timezone_id']}{c.end}
{col()}Observation Time (When data was last updated) : {data['current']['observation_time']}{c.end}
{col()}Temperature : {data['current']['temperature']} {data['request']['unit']}{c.end}
{col()}UV Index : {data['current']["uv_index"]}{c.end}
{col()}Humidity : {data['current']['humidity']}{c.end}
"""
    return output

#---------------------------------------------------------------#

#7 days ago date in var
seven = time.time() - 604800
seven = time.strftime('%Y-%m-%d', time.gmtime(seven))

#Func for specific past date
def historical(hist=seven, unit='f', location='New Delhi', celsius=False):
    pass

#---------------------------------------------------------------#

#Func for specific past date
def historical_series(hist_start=seven, hist_end=date.today(), unit='f', location='New Delhi', celsius=False):
    pass

#---------------------------------------------------------------#

def forecast(unit='f', location='New Delhi', celsius=False):
    pass

#---------------------------------------------------------------#


#Trial
if __name__=="__main__":
    return_val = (weather(location="Jodhpur", unit="f", celsius=True))
    if return_val is not None:
        print(return_val)