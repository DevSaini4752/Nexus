"""This will be used to reset all the data in data.json"""

#Importing modules
import json

#function
def reset():
    with open("databackup.json", "r") as file:
        backupdata = json.load(file)

    with open("data.json", "w") as file:
        json.dump(backupdata, file, indent=4)

#Trial
if __name__ == "__main__":
    reset()