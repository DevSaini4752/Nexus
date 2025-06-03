"""The module would be there for a function which will be called
every time the  project is started, and it will check the status
that which task's deadline is crossed whose deadline is near. If
the  deadline is  near, then  it  will  warn the  user. May this
initializer would be called many times depending on the situation."""

#Importing modules
import pointmanager
import json
import time
import taskremover
import colours as c
from ToDoManager.resetdata import reset


#Fucntion
def initializer():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        #This will not allow the system to edit important data
        for key in data.keys():
            if key == "total_points" or key == "PoiHis" or key == "Task Name":
                pass

            else:
                #Deadline time will be stored in var
                value = data[key]
                value = value[1]

                #Checking whether deadline of any task is crossed or not
                if value < time.time():
                    pointmanager.point_manger(-6, "Crossing the Deadline")
                    taskremover.tskrem(key)
                    print(f"{c.red}Warning!!! - You crossed a task's({key}) deadline so 6 points has been deducted{c.end}")

    except FileNotFoundError:
        reset()

    except Exception as ex:
        return print(f"""{c.red}Unexpected Error occurred - {ex}""")

if __name__ == "__main__":
    initializer()