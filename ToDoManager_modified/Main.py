"""So this file will handle the final execution of all modules and 
housekeeping."""

#Importing modules
import anima_ToDo
import colours as c
import initializer
import taskdatamanager
import taskremover
import time
import sys
import resetdata
import report
import completetsk
from randomcol import col


def main():
    #Using initializer to initialize sys
    initializer.initializer()
    anima_ToDo.intro()

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
            col()
            anima_ToDo.outro()
            sys.exit()

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

        #Running initializer if 2 mins have passed
        diff = int(time.time()) - start_time
        if diff >= 120:
            initializer.initializer()
            start_time = int(time.time())

if __name__ == "__main__":
    main()