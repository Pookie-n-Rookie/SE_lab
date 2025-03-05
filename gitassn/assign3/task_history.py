import sqlite3
import time 


def log_task_history(task_id,action,title,description,completed):
	conn=sqlite3.connect("tasks.db")
	cursor=conn.cursor()
	timestamp=time.time()

	cursor.execute('''INSERT INTO task_history(task_id,action,timestamp,title,description,completed) VALUES (?,?,?,?,?,?)''',(task_id,action,timestamp,title,description,completed))
	conn.commit()
	conn.close()


