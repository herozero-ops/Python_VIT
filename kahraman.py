def delete_task(tasks, task_id, tasks_file):
    
    task_found = False
    for task in tasks:
        if task.get("id") == task_id:
            task_found = True
            task["status"] = "Deleted"
            task["id"] = None
            break

    if not task_found:
        print("Task not found")
        return False


    for task in tasks:
        if task.get("id") and task["id"] > task_id:
            task["id"] -= 1

    save_file(tasks_file, tasks)

    print(f"Task with ID {task_id} has been successfully deleted.")
    return True

def save_file(filename, tasks):
    with open(filename, "w") as file:
        import json
        json.dump(tasks, file, indent=4)
