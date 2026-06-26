class Task:
    def __init__(self, name, done = False):
        self.name = name
        self.done = done
    
    def __str__(self):
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.name}"


class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, name):
        task = Task(name)
        self.tasks.append(task)
        print(f"Added: {name}")
    
    def show_tasks(self):
        if not self.tasks:
            print("No tasks yet!")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}: {task}")
    
    def delete_task(self, number):
        if 0 < number <= len(self.tasks):
            removed  = self.tasks.pop(number - 1)
            print(f"Deleted: {removed.name}")
        else:
            print("Invalid Task Number!")
    
    def complete_task(self, number):
        if 0 < number <= len(self.tasks):
            self.tasks[number - 1].done = True
            print(f"Completed: {self.tasks[number - 1].name}")
        else:
            print("Invalid Task Number")
    

def main():
    todo = TodoList()
    
    while True:
        print("\n--- My Todo List ---")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Quit")
            
        choice = input("Choose an option: ")
            
        if choice == "1":
            name = input("Task name: ")
            todo.add_task(name)
        elif choice == "2":
            todo.show_tasks()
        elif choice == "3":
            num = int(input("Task number to complete: "))
            todo.complete_task(num)
        elif choice == "4":
            num = int(input("Task number to delete: "))
            todo.delete_task(num)
        elif choice == "5":
            print("Bye!")
            break

main()

