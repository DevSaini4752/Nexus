"""Here the taskremover() function will allow us
to remove a task from the task list (data.json)"""

#Importing Modules
import json
import colours as c
import pointmanager
import time
import datetime

# Function
def tskrem(*tasks):
    try:
        with open("data.json", "r") as file_in:
            data = json.load(file_in)
            # Will remove the task given
            for task in tasks:
                poihis = data["PoiHis"]

                # Updating points
                timeoftask = (data[task])[2]
                if (time.time() - timeoftask) > 120:
                    data["total_points"] -= 6
                    print(f"""{c.red}6 points has been deducted for not completing the task, and 
withdrawing from your commitment after 2 mins{c.end}""")

                    #Updating history
                    poihis[f"{datetime.datetime.now()}"] = [-6, "Canceled in less then 2 mins"]

                else:
                    print(f"""{c.red}No points deducted as you deleted the task in less then 2 mins, 
but the 2 points which you got for making a task is taken back{c.end}""")
                    data["total_points"] -= 2

                    # Updating history
                    poihis[f"{datetime.datetime.now()}"] = [-2, "Canceled in less then 2 mins"]

                # Deleting the task
                del data[task]

        #Updating the data in data,json
        with open("data.json", "w") as file_out:

            json.dump(data, file_out, indent=4)

    # Just to don't raise error during an empty file
    except json.JSONDecodeError:
        msg = f"{c.red}No task in inventory!!!{c.end}"
        print(msg)
    # If no file is there
    except FileNotFoundError:
        msg = f"{c.red}No task in inventory!!!{c.end}"
        print(msg)
    # If a task does not exist
    except KeyError as er:
        msg = f"{c.red}{er} : Task not found!!! Recheck the name of the task{c.end}"
        print(msg)

if __name__ == "__main__":
    tskrem("Doggo")