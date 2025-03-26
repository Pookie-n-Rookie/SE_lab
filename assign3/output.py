from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\nTask Manager - Choose an action:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Complete Task")
        print("4. List Tasks")
        print("5. Exit")
        
        choice = raw_input("Enter your choice: ")
        
        if choice == '1':
            title = raw_input("Enter task title: ")
            description = raw_input("Enter task description: ")
            manager.add_task(title, description)
        
        elif choice == '2':
            task_id = int(raw_input("Enter task ID to edit: "))
            new_title = raw_input("Enter new task title: ")
            new_description = raw_input("Enter new task description: ")
            manager.edit_task(task_id, new_title, new_description)
        
        elif choice == '3':
            task_id = int(raw_input("Enter task ID to mark as completed: "))
            manager.complete_task(task_id)
        
        elif choice == '4':
            manager.list_tasks()
        
        elif choice == '5':
            print("Exiting Task Manager.")
            manager.close()
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

