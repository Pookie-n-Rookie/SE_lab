import sqlite3

def log_task_history(task_id, action, title, description, completed):
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO task_history(task_id, action, title, description, completed)
                      VALUES (?, ?, ?, ?, ?)''', (task_id, action, title, description, completed))
    conn.commit()
    conn.close()
