"""The point manager will be used to manage points.
It will take  some arguments, and depending on the
argument, it will add or deduct points.

The point manager will take 2 args, one will be for
how  many  points to  be added or deducted, and the
time will be taken by the manager on itself through time
module.

Next, 2nd would be for what purpose it was deducted or added."""

#importing module
import json
import datetime
import colours as c


# Function for the purpose
def point_manger(points, purpose):
    try:
        #Will allow saving time of initializing the task in history
        live_time = datetime.datetime.now()

        #Updating data
        with open("data.json", "r") as file:
            data = json.load(file)
            data["total_points"] += points
            history = data["PoiHis"]
            history[f"{live_time}"] = [f"{points}", f"{purpose}"]

        #Saving data
        with open("data.json", "w") as file:
            json.dump(data, file, indent =4)

    except Exception as ex:
        msg = (f"{c.red}Unexpected error occurred -"
               f"{ex}{c.end}")
        return msg


if __name__ == "__main__":
    func = point_manger(2, "Initializing")
    if not func is None:
        print(func)
