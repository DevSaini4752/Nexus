# ToDoManager (TDM)

A modular, command-line To-Do manager built with Python. It features deadline tracking, a gamified point system, a colorful CLI interface, persistent data storage, and a structured modular codebase. The project is designed to simulate a real-world software system with clean separation of concerns.

## Important Note
- This system is functionally similar to the original `ToDoManager (found at https://github.com/DevSaini4752/ToDoManager.git)`. However, specific modifications have been implemented to ensure compatibility with The Nexus project. These adjustments primarily involve and account system and the removal of animations and the system's continued operation after exiting.

## Features

- Add, remove, and view tasks
- Deadline-based reminders and penalties
- Gamified point system with history log
- JSON-based persistent data storage
- Colorful terminal interface using ANSI codes
- Animated CLI intro/outro messages
- Modular code structure for scalability

## Modules Overview

- `main.py`: Entry point, handles user input
- `taskdatamanager.py`: Adds new tasks with deadlines
- `completetsk.py`: Finalize the task's status to 'completed'
- `taskremover.py`: Removes tasks and adjusts points
- `pointmanager.py`: Manages point updates and history
- `initializer.py`: Checks for missed deadlines and errors on startup
- `report.py`: Displays a summary of task progress and points
- `colours.py`, `randomcol.py`: CLI color styling
- `anima_ToDo.py`: Text-based animations
- `resetdata.py`: Resets all data with backup support
- `account_adapter`: Made to make the TDM comfortable with the account system

## Data Structure

A folder is there named `user_accounts_TDM` contain many `.json` files with username as their filename.
For every user, there is a different data file where data related to their TDM is stored.

What a specific user file contains - 
- `total_points`: Integer value
- `PoiHis`: Dictionary with timestamped history
- Task entries with name, description, deadline, and creation time

How the **data processing** works - 
- When the user uses TDM after loging in, the data of user is transferred to data.json from the user data file
- All the changes are made in data.json
- After the user uses a feature and if two mins has passed, then data is saved to a user file
- As the user exists the TDM by exit option, the data is saved
- In the end, the data.json is emptied to keep data safe

## Usage

- Make an account in Nexus and use the TDM option

## License

This project is licensed under the MIT License.