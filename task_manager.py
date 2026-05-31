'''
Landon Pack
IS 303 - A05

Task Manager Program
A program allowing the user to organize their tasks, mark them as complete, and check the priority of the task

Inputs: No user input; tasks are hardcoded

Processes: Processes: 
Task- stores a single task's name, priority,
and completion status; can mark itself
complete and return a summary string

-TaskManager - holds a list of Task objects; can
add tasks, mark a task complete by name,
display all tasks, and return incomplete tasks                    

Outputs:
- A formatted task list showing task name, priority, and completion status

CLASS: Task
RESPONSIBILITIES                    | COLLABORATORS
------------------------------------|-------------
Knows its name, Knows its priority,
Knows if it is complete.
    
 

CLASS: TaskManager
RESPONSIBILITIES                               | COLLABORATORS
-----------------------------------------------|-------------
Knows all existing tasks (maintains the list)  | Task
Can add a task                                 |Task
Can remove a task                              |Task
Can retrieve tasks                             |Task

'''



class Task:

    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.complete = False

    def mark_complete(self):
        self.complete = True

    def is_done(self):
        return self.complete

    def summary(self):
        if self.complete:
            status = "Complete"
        else:
            status = "Incomplete"
        return f"{self.name} | Priority: {self.priority} | Status: {status}"

    def __str__(self):
        if self.complete:
            status = "Complete"
        else:
            status = "Incomplete"
        return f"[{status}] {self.name} (Priority: {self.priority})"


class TaskManager:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                print(f"Task '{name}' removed.")
                return True
        return False

    def complete_task(self, name):
        for task in self.tasks:
            if task.name == name:
                task.mark_complete()
                print(f"Task '{name}' marked as complete.")
                return True
        return False

    def get_incomplete(self):
        return [task for task in self.tasks if not task.is_done()]

    def display_all(self):
        print("--- All Tasks ---")
        for task in self.tasks:
            print(task)

    def __str__(self):
        total = len(self.tasks)
        done = sum(1 for task in self.tasks if task.is_done())
        return f"TaskManager: {total} task(s), {done} complete"


# Main flow
def main():
   
    manager = TaskManager()

    manager.add_task(Task("Write project report", "High"))
    manager.add_task(Task("Reply to emails", "Medium"))
    manager.add_task(Task("Buy groceries", "Low"))
    manager.add_task(Task("Study for exam", "High"))

    
    manager.display_all()

    manager.complete_task("Reply to emails")
    manager.complete_task("Buy groceries")
    manager.remove_task("Buy groceries")
    print()
    manager.display_all()

    print(f"\n{manager}")

    print("\n--- Incomplete Tasks ---")
    for task in manager.get_incomplete():
        print(f"  {task.summary()}")

main()