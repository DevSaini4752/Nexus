"""
This module will have a NEWS api which will allow user to have news, of any
topic and other things.

- API - Newsapi
- Website - 'https://newsapi.org/'
- URL - 'https://newsapi.org/v2/endpoint?parameters'

- Endpoints -
    - Everything - /v2/everything - Gives all news over 150K sources of past 5 years

    - Top headlines - /v2/top-headlines - Returns breaking news headlines for countries,
        categories, and singular publishers.

    - Sources - /v2/top-headlines/sources – returns information(including name, description,
        and category) about the most notable sources available for obtaining top headlines from.
"""


#importing modules
import requests
from colours import ran_col as col
import colours as c
import decouple

#Key in variable
key = decouple.config("NEWSAPI_API_KEY")

#Function
#Have kept the topic Current affairs by default, It will give all kinds of news
# if in any case user or other module doesn't give any topic
def getnews(topic='Current Affairs', num_of_art_user_want=10):
    url = 'https://newsapi.org/v2/everything?'
    parameters = {
        'q' : topic,
        'apiKey' : key,
        'pageSize' : 100,
        'language' : 'en'
    }

    data = (requests.get(url, params=parameters)).json()

    #Handling error :)
    if data["status"] == 'error':

        output = f"""{c.acidic_red}
Status : {data["status"]}{c.end}{col()}
Error : {data["code"]}{c.end}{col()}
Info : {data["message"]}{c.end}{col()}
"""
        return output

    # Total results will give all the articles it got. However, it only shows maximum 100 articles
    # per page, and if we try to go next page than for every page, we would need a new request and
    # our requests are limited so it won't work. So we will just tell the number of articles we got
    # on this page.
    arts_we_got = len(data['articles'])

    #If total results is lesser than the user's need (no_of_art), then converting
    #'user need variable (num_of_art_user_want)' to 'num of result (arts_we_got)'
    #variable
    if arts_we_got < num_of_art_user_want:

        #Variable to be added in output
        art_num_in_output = f"{num_of_art_user_want}" + f"""
{c.acidic_red}Note: As the number of total number of articles was less then you need, so we are 
giving you all the articles we found in through sources{c.end}"""

        num_of_art_user_want = arts_we_got


    else:
        art_num_in_output = num_of_art_user_want


    #Working on final output
    #Intro of output msg
    output = f"""
Total Results : {arts_we_got}
Number of articles you want : {art_num_in_output}

"""


    #If no articles are found
    total_results = int(data["totalResults"])
    if total_results == 0:
        warning = f"{c.acidic_red}!!!---Sorry to inform but no articles found---!!!{c.end}"
        output += warning

        return output


    #Adding number of articles user want
    #Through loop adding number of articles user want. Articles are in a list in the data returned by API
    for n in range(num_of_art_user_want):
        article = data['articles'][n]
        added = f"""{col()}
#-----Article {n + 1}-----#

Source : {article["source"]["name"]}
Author : {article["author"]}
URL of article: {article["url"]}

Title : {article["title"]}
Description : {article["description"]}{c.end}
"""

        output += added



    return output

if __name__=="__main__":
    return_val = getnews(topic='Current affairs', num_of_art_user_want=15)

    if not return_val is None:
        print(return_val)