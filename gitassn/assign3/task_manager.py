# task_manager.py
import sqlite3
import os
from task_history import log_task_history

class TaskManager:
    def __init__(self, db_name="tasks.db", tasks_dir="tasks"):
        self.db_name = db_name
        self.tasks_dir = tasks_dir
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

        # Ensure the tasks directory exists
        if not os.path.exists(self.tasks_dir):
            os.makedirs(self.tasks_dir)

    def create_tables(self):
        # Create tables for tasks and task history
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL,
            folder_path TEXT NOT NULL
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS task_history (
            history_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER,
            action TEXT NOT NULL,
            timestamp REAL NOT NULL,
            title TEXT,
            description TEXT,
            completed BOOLEAN,
            FOREIGN KEY(task_id) REFERENCES tasks(task_id)
        )''')

        self.conn.commit()

    def create_task_folder(self, task_id):
        # Create a unique folder for each task inside the tasks directory
        folder_name = "task_{}".format(task_id)  # Replaced f-string with .format()
        task_folder_path = os.path.join(self.tasks_dir, folder_name)

        if not os.path.exists(task_folder_path):
            os.makedirs(task_folder_path)

        return task_folder_path

    def add_task(self, title, description):
        # Add a new task to the tasks table
        self.cursor.execute('''INSERT INTO tasks (title, description, completed, folder_path) 
                               VALUES (?, ?, ?, ?)''', (title, description, False, ""))
        self.conn.commit()
        task_id = self.cursor.lastrowid

        # Create a folder for the task
        task_folder_path = self.create_task_folder(task_id)

        # Update the task with the folder path
        self.cursor.execute('''UPDATE tasks SET folder_path = ? WHERE task_id = ?''', 
                            (task_folder_path, task_id))
        self.conn.commit()

        # Log this action in the task history
        log_task_history(task_id, "created", title, description, False)
        print("Task '{}' added successfully with folder: {}".format(title, task_folder_path))

    def edit_task(self, task_id, new_title, new_description):
        # Edit a task's title and description
        self.cursor.execute('''UPDATE tasks SET title = ?, description = ? WHERE task_id = ?''', 
                            (new_title, new_description, task_id))
        self.conn.commit()

        # Log this action in the task history
        task_data = self.get_task(task_id)
        log_task_history(task_id, "updated", new_title, new_description, task_data[3])
        print("Task updated successfully.")

    def complete_task(self, task_id):
        # Mark a task as completed
        self.cursor.execute('''UPDATE tasks SET completed = ? WHERE task_id = ?''', (True, task_id))
        self.conn.commit()

        # Log this action in the task history
        task_data = self.get_task(task_id)
        log_task_history(task_id, "completed", task_data[1], task_data[2], True)
        print("Task marked as completed.")

    def get_task(self, task_id):
        # Get task details by task_id
        self.cursor.execute('''SELECT * FROM tasks WHERE task_id = ?''', (task_id,))
        return self.cursor.fetchone()

    def list_tasks(self):
        # List all tasks
        self.cursor.execute('''SELECT * FROM tasks''')
        tasks = self.cursor.fetchall()
        if not tasks:
            print("No tasks available.")
        else:
            for task in tasks:
                print("Task ID: {}, Title: {}, Completed: {}".format(task[0], task[1], 'Yes' if task[3] else 'No'))

    def close(self):
        # Close the database connection
        self.conn.close()

