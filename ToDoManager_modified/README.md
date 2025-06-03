# ToDoManager 

A modular, command-line To-Do manager built with Python. It features deadline tracking, a gamified point system, a colorful CLI interface, persistent data storage, and a structured modular codebase. The project is designed to simulate a real-world software system with clean separation of concerns.

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

## Data Structure

All task and point data are stored in `data.json`. The file contains:
- `total_points`: Integer value
- `PoiHis`: Dictionary with timestamped history
- Task entries with name, description, deadline, and creation time

## Usage

1. Ensure Python 3 is installed.
2. Clone the repository.
3. Run `python main.py` in your terminal.

## License

This project is licensed under the MIT License.