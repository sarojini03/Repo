Task Master:-

Task Master is a simple task management application built using Flask, a micro web framework for Python. The application allows users to create, read, update, and delete tasks.

Features
- Create new tasks
- View all tasks
- Update existing tasks
- Delete tasks

Technologies Used
- Flask: A micro web framework for Python.
- SQLite: A self-contained, file-based database.
- HTML/CSS: For structuring and styling the application.

Project Structure
The project structure is as follows:

- app.py: The main application file that contains the Flask app and routes.
- templates/: A directory containing HTML templates for the application.
    - base.html: The base template that contains common HTML structure.
    - index.html: The template for the main page that displays all tasks.
    - update.html: The template for the update page that allows users to update tasks.
- static/: A directory containing static files such as CSS files.
    - main.css: The main CSS file that styles the application.

Installation
1. Clone the repository: git clone https://github.com/your-username/Task-Master.git
2. Navigate to the project directory: cd Task-Master
3. Install the required packages: pip install flask flask-sqlalchemy
4. Run the application: python app.py

Usage
1. Open a web browser and navigate to http://localhost:5000
2. Create a new task by entering the task description and clicking the "Add Task" button
3. View all tasks on the main page
4. Update a task by clicking the "Update" link next to the task
5. Delete a task by clicking the "Delete" link next to the task

Contributing
Contributions are welcome! If you'd like to contribute to Task Master, please fork the repository and submit a pull request.

License
Task Master is licensed under the MIT License. See LICENSE for details.
