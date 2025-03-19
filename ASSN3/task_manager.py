import sqlite3
from task_history import log_task_history

class TaskManager:
    def __init__(self, db_name="tasks.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Create tables for tasks and task history
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            completed BOOLEAN NOT NULL
        )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS task_history (
            history_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER,
            action TEXT NOT NULL,
            title TEXT,
            description TEXT,
            completed BOOLEAN,
            FOREIGN KEY(task_id) REFERENCES tasks(task_id)
        )''')

        self.conn.commit()

    def add_task(self, title, description):
        # Add a new task to the tasks table
        self.cursor.execute('''INSERT INTO tasks (title, description, completed)
                               VALUES (?, ?, ?)''', (title, description, False))
        self.conn.commit()
        task_id = self.cursor.lastrowid

        # Log this action in the task history
        log_task_history(task_id, "created", title, description, False)
        print("Task '{}' added successfully.".format(title))

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
            self._print_table(tasks, ["Task ID", "Title", "Description", "Completed"])

    def print_db(self, table_name):
        # Print the contents of a table in a proper table format
        self.cursor.execute('''SELECT * FROM {}'''.format(table_name))
        rows = self.cursor.fetchall()
        if not rows:
            print("No data available in {}.".format(table_name))
        else:
            if table_name == "tasks":
                self._print_table(rows, ["Task ID", "Title", "Description", "Completed"])
            elif table_name == "task_history":
                self._print_table(rows, ["History ID", "Task ID", "Action", "Title", "Description", "Completed"])

    def _print_table(self, rows, headers):
        # Helper function to print rows in a table format
        col_widths = [max(len(str(item)) for item in col) for col in zip(*rows)]
        col_widths = [max(col_widths[i], len(headers[i])) for i in range(len(headers))]

        # Print headers
        header_row = " | ".join("{:<{}}".format(headers[i], col_widths[i]) for i in range(len(headers)))
        print(header_row)
        print("-" * len(header_row))

        # Print rows
        for row in rows:
            print(" | ".join("{:<{}}".format(str(item), col_widths[i]) for i, item in enumerate(row)))

    def close(self):
        # Close the database connection
        self.conn.close()
