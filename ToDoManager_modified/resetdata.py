"""This will be used to reset all the data in data.json"""

#Importing modules
import json
import get_path

#Abs. path of files so that they don't get stuck anywhere if we import Main.py out of TDM
data_json = get_path.get_path("ToDoManager_modified", "data.json")
databackup_json = get_path.get_path("ToDoManager_modified", "databackup.json")

#function
def reset():
    with open(databackup_json, "r") as file:
        backupdata = json.load(file)

    with open(data_json, "w") as file:
        json.dump(backupdata, file, indent=4)

#Trial
if __name__ == "__main__":
    reset()