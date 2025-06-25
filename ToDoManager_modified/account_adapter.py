"""This module is being made because as I want to make the TDM collaborate with
the NEXUS, so this module would be an adapter of TDM. Planning of how TDM  will
adapt with the account system is given below -

So there would be a folder named 'user_accounts_TDM' and that would
contain files  of different usernames, and  the data.json file which  was the
main  file  where all  data was being  stored would  become a temporary data
holder. The system would bring the data of the user from  user_accounts_TDM/
by the  username  of the  user and will put that in the data.json and as any
process would  end. The system would store the  data back  into the original
user's data file to keep the same data in data.json also. It will remove the
data from the data.json after the user logs out."""

#Importing modules
import json
import get_path


#This function loads data from the user's TDM file into data.json once. All updates
# happen in data.json until the user exits, at which  point the data  is saved back
# to the original TDM file to avoid continuous processing overhead.
def adapter(username):
    # Abs. path of files so that they don't get stuck anywhere if we import Main.py out of TDM
    tdm_user_file_path = get_path.get_path("ToDoManager_modified", "user_accounts_TDM", f"{username}.json")
    data_json = get_path.get_path("ToDoManager_modified", "data.json")

    #Updating the data.json file by putting user's data in it
    with open(tdm_user_file_path, "r") as file:
        user_data_tdm = json.load(file)

    with open(data_json, "w") as file:
        json.dump(user_data_tdm, file, indent=4)

#This will update the original user tdm data at the end. It would even run after
# every 2 mins, so there would be minimum chances of data loss
def updater(username):
    # Abs. path of files so that they don't get stuck anywhere if we import Main.py out of TDM
    tdm_user_file_path = get_path.get_path("ToDoManager_modified", "user_accounts_TDM", f"{username}.json")
    data_json = get_path.get_path("ToDoManager_modified", "data.json")

    #Updating....
    with open(data_json, "r") as file:
        temp_data = json.load(file)

    with open(tdm_user_file_path,"w") as file:
        json.dump(temp_data, file, indent=4)


#Trial and testing
if __name__ == "__main__":
    #Adapting
    adapter("dev2")

    #Changing data in data.json to check changes in user tdm file
    data_json = get_path.get_path("ToDoManager_modified", "data.json")

    with open(data_json, "r") as file:
        data = json.load(file)

    data["total_points"] = 300

    with open(data_json, "w") as file:
        json.dump(data, file, indent=4)

    updater("dev2")