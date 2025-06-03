"""Here we will make a function which will add a task to the list, and it will
be saved in  a JSON file in a "list" form and whenever needed, it will be used
accordingly"""

#Importing Modules
import json
import colours as c
import time
import pointmanager
import resetdata

# Function
# mtd -> Manage task and data
def mtd(hours=True, **tasks):
    try:
        with open("data.json", "r") as file_op:
            data = json.load(file_op)

    # Just to don't raise error during an empty file,
    # The file would be created if not there in next step
    except json.JSONDecodeError:
        resetdata.reset()

        #Re-executing the task after reset to give vars to execute further proceedings

        with open("data.json", "r") as file_op:
            data = json.load(file_op)

    except FileNotFoundError:
        resetdata.reset()

        #Re-executing the task after reset to give vars to execute further proceedings

        with open("data.json", "r") as file_op:
            data = json.load(file_op)

    #Keeping this out of the first try part because if
    # an exception is there in try  then it would  end
    # after  that  execution, and  this  operation  is
    # compulsory to be executed
    try:
        for tskkey, tskval in tasks.items():

            tskval[1] = float(tskval[1])

            if hours:
                tskval[1] *= 3600
                tskval[1] += time.time()
            else:
                tskval[1] *= 3600 * 24
                tskval[1] += time.time()

            data[tskkey] = tskval.append(time.time())
            data[tskkey] = tskval

    #If sys don't gets the deadline
    except IndexError as IE:
        msg = f"{c.red}{IE} - Kindly enter Deadline also in Hrs or Days, System failed to got the Deadline!!!{c.end}"
        return print(msg)

    #Updating the data
    with open("data.json", "w") as file_wr:
        json.dump(data, file_wr, indent=4)

    #Adding the points
    for _ in range(len(tasks)):
        func = (pointmanager.point_manger(2, "Initializing"))
        if not func is None:
            print(func)

#Trial
if __name__ == "__main__":
    mtd(**{"Chy":["Complete the question answers of the first chapter", 3], "Doggo":["Food", "3"]})