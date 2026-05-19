from storage import load_tasks, save_tasks

class TodoManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, name):
        task = {"name": name, "done": False}
        self.tasks.append(task)
        save_tasks(self.tasks)
        print(f"Task '{name}' added!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
            return
        for i, task in enumerate(self.tasks):
            status = "✅" if task["done"] else "❌"
            print(f"{i++1}. {status} {task['name']}")

    def mark_done(self, idx):
        if idx<0 or idx>=len(self.tasks):
            print("Invalid task number!")
            return
        name = self.tasks[idx]["name"]
        if self.tasks[idx]["done"] == False:
            self.tasks[idx]["done"] = True
            print(f"Task '{name}' marked as done!")
        else:
            self.tasks[idx]["done"] = False
            print(f"Task '{name}' marked as undone!") 
        save_tasks(self.tasks)    

    def delete_tasks(self, idx):
        if idx<0 or idx>=len(self.tasks):
            print("Invalid task number!")
            return
        name = self.tasks[idx]["name"]
        self.tasks.pop(idx)
        save_tasks(self.tasks)
        print(f"Task '{name}' deleted!")
