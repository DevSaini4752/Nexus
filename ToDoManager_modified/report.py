"""This module will be used to see the full report of user"""

#Importing modules
import json
import datetime
from randomcol import col
import colours as c

#Func
def report():

    #Taking out the data
    with open("data.json", "r") as file:
        data = json.load(file)

    #Increasing readability
    #Putting History in a structured way
    history = f"""{col()}
History - {c.end}
"""
    for histime, vals in (data["PoiHis"]).items():
        temphis = f"""{col()}Time - {histime}
Points updated -> {vals[0]}
Reason - {vals[1]}
{c.end}
"""

        history += temphis

    #fdata -> final data
    fdata = f"""{col()}
Total Points - {data["total_points"]}{c.end}

Live Tasks - """


    for key in data.keys():
        #Making these empty str vars so that vars in "if" can
        # refer to these, and we can avoid the use of "global"
        deadline = ""
        savingtime = ""
        description = ""

        if key != "total_points" and key != "PoiHis" and key != "Task Name":
            deadline = datetime.datetime.fromtimestamp((data[key])[1])
            savingtime = datetime.datetime.fromtimestamp((data[key])[2])
            description = (data[key])[0]

            tasks = f"""
Task - {key}

{col()}Description - {description}{c.end}
{col()}Deadline - {deadline}{c.end}
{col()}Time when task was initialized - {savingtime}{c.end}"""

            tempdata = f"""{tasks}
"""

            fdata += tempdata

    fdata += history
    return fdata

if __name__ == "__main__":
    print(report())