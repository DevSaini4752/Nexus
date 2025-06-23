"""
Here we will make a function which will work with weatherstack API and
will return weather depending on the parameters given.

The function will take the following arguments -
    - time (current/historical/historical_series/forecast, default: current)
    - unit (metric/fahrenheit/scientific/celsius, default: celsius, f will be converted to c)
    - location (default: New Delhi)
    - forecast_days (Of how many days forecast user need, default: 7)
"""

#!!!Important note:
#Access to/option of historical and forecast data is removed as it's not supported
# in our subscription of weatherstack API!!!

#Importing Prerequisites
import requests
import colours as c
from colours import ran_col as col
import decouple

#Key in var
key = decouple.config('WEATHERSTACK_API_KEY')

#---------------------------------------------------------------#


#Function for current weather
def current_weather(unit="f", location="New Delhi", celsius=False):

    url = "https://api.weatherstack.com/current?"
    params = {
        'query' : location,
        'access_key' : key,
        'units' : unit
    }

    data = (requests.get(url, params=params)).json()

    #If error occurs then program will return this, and this will only work when
    # success key is there because success key is only there when error occurs

    if 'success' in data:
        error = f"""{c.acidic_red}Success : {data['success']}
What happened : {data['error']['type']}{c.end}"""
        return error


    #Changing the fahrenheit to celsius if wanted
    if celsius:
        data['current']['temperature'] -= 32
        data['current']['temperature'] *= 5/9

    # Changing Unit from s/f/m to their specific name so that user can get it easily
    if unit == 'f':
        data['request']['unit'] = 'Fahrenheit'
    elif unit == 'm':
        data['request']['unit'] = 'Metric'
    elif unit == 's':
        data['request']['unit'] = 'Scientific'
    if celsius:
        data['request']['unit'] = 'Celsius'


    #Specifiying that what values has to be returned to user (what should be the final output)
    output = f"""{col()}
Time Zone : {data['location']['timezone_id']}{c.end}
{col()}Observation Time (When data was last updated) : {data['current']['observation_time']}{c.end}
{col()}Temperature : {data['current']['temperature']} {data['request']['unit']}{c.end}
{col()}UV Index : {data['current']["uv_index"]}{c.end}
{col()}Humidity : {data['current']['humidity']}{c.end}
"""
    return output


#---------------------------------------------------------------#


#Trial
if __name__=="__main__":
    return_val = (current_weather(location="Jodhpur", unit="f", celsius=True))
    if return_val is not None:
        print(return_val)