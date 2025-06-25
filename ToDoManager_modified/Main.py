"""So this file will handle the final execution of all modules and 
housekeeping."""

#Importing modules
import ToDoManager_modified.colours as c
import ToDoManager_modified.initializer as initializer
import ToDoManager_modified.taskdatamanager as taskdatamanager
import ToDoManager_modified.taskremover as taskremover
import time
import ToDoManager_modified.resetdata as resetdata
import ToDoManager_modified.report as report
import ToDoManager_modified.completetsk as completetsk
from ToDoManager_modified.randomcol import col
from ToDoManager_modified.animations import type_write
from ToDoManager_modified import account_adapter
import get_path


def main(username):
    #Adapting the system
    account_adapter.adapter(username)

    #Using initializer to initialize sys
    initializer.initializer()

    #Intro
    type_write(f"""{col()}Get ready to kick chaos out of your day! This is ToDoManager – your no-nonsense task tracker. Simple, fast, 
and made to keep your brain clutter-free. Let’s roll{c.end}""",  wait=0.03)

    # This time process will run continuously run, and we will use
    # it such that initializer is run after every 2 mins to keep
    # a check on tasks and other
    start_time = int(time.time())

    #Final execution for user
    while True:
        user = input(f"""{c.end}{col()}
Hello!!! User, I hope that you are doing well...
Well!!! What do you want to do ?
a. Add Task
b. Completed Task
c. Remove Task
d. See report
e. Exit
f. Reset

Kindly choose (a/b/c/d) : {c.end}""").lower()

        if user == "a":
            task_name = input(f"""{col()}Kindly enter the name of the task : {c.end}""").lower()
            description = input(f"""{col()}Kindly enter the description of the task : {c.end}""")

            #Keeping the further proceedings in loop, so if a wrong option
            # is chosen, then user can get one more chance
            while True:
                hrsorday = input(f"""{col()}Do you want to put your deadline in Hrs or Days -
    a. Hours
    b. Days
    
    a/b : {c.end}""").lower()

                #Proceding depending on hrs or days deadline
                if hrsorday == "a":
                    deadline = input(f"In how many {c.cyan}hour/hours{c.end} will you complete the task (Deadline in hours) : ")

                    #If user kept anything empty, then it will be stopped
                    if not (deadline == "" or task_name == "" or description == ""):
                        taskdatamanager.mtd(**{task_name : [description, deadline]})
                        print(f"{col()}Task added successfully !!!{c.end}")
                        break
                    else:
                        print()
                        print(f"{c.red}You left one of the input empty!!!{c.end}")
                        break

                elif hrsorday == "b":

                    deadline = input(f"In how many {c.cyan}day/days{c.end} will you complete the task (Deadline in days) : ")

                    # If user kept anything empty, then it will be stopped
                    if not (deadline == "" or task_name == "" or description == ""):
                        taskdatamanager.mtd(hours=False, **{task_name : [description, deadline]})
                        print(f"{col()}Task added successfully !!!{c.end}")
                        break

                    else:
                        print()
                        print(f"{c.red}You left one of the input empty!!!{c.end}")
                        break

                else:
                    print()
                    print(f"{c.red}Invalid input!!! Kindly choose a/b")
                    print()

        elif user == "b":
            tsk = input(f"{col()}Which task have you completed : ").lower()
            completetsk.complete(tsk)

        elif user == "c":
            task = input(f"{c.red}Which task do you want to remove : {c.end}").lower()
            taskremover.tskrem(task)

        elif user == "d":
            print(report.report())
            print()


        elif user == "e":
            #Getting the path that its data can be removed
            data_json = get_path.get_path("ToDoManager_modified", "data.json")

            print(f"{col()}Saving data.....{c.end}")

            # Updating the user tdm data file
            account_adapter.updater(username)

            # Emptying the data.json to keep the user's data safe
            file = open(data_json, "w")
            file.close()

            type_write(f"""{col()}Saved\nThank you for using our services. Stay focused, 
stay organized - and keep building{c.end}""", wait=0.03)

            break

        elif user == "f":

            yon = input(f"""{c.red}This will remove all of the data of you, and the step can't be reversed!!"
Are you sure (Y/n) !? : """).lower()

            if yon == "y":
                print(f"{col()}Bye user :), deleting.....{c.end}")
                resetdata.reset()
                print(f"{col()}Data reset Successfully !!!{c.end}")

            elif yon == "n":
                print(f"{col()}Getting back.....{c.end}")

        else:
            print(f"\n{c.red}Invalid Option !!!{c.end}")

        #Running initializer and updater if 2 mins have passed
        diff = int(time.time()) - start_time
        if diff >= 120:
            initializer.initializer()
            start_time = int(time.time())

            # Updating the user tdm data file
            account_adapter.updater(username)



if __name__ == "__main__":
    main("dev2")