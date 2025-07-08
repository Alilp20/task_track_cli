import cmd
from datetime import date
from tabulate import tabulate

class TaskTracker(cmd.Cmd):
    intro = 'Welcome to the Task Tracker!\n'
    prompt = 'task-cli> '
    
    tasks = [{
        "id" : 1,
        "description" : "",
        "status" : "to-do",
        "createdAt" : "1/1/2001",
        "updatedAt" : "2/2/2002"
    }]
    task_count = 2
    
    def do_add(self, arg):
        """ Add a task: add <new_description>"""
        if not arg:
            print("Usage: add <task_description>")
        else:
            today = date.today().strftime("%d/%m/%Y")
            new_task = {
                "id" : self.task_count,
                "description" : arg,
                "status" : "to-do",
                "createdAt" : today,
                "updatedAt" : today
            }
            self.tasks.append(new_task)
            print(f"Task {arg} added.")
            self.task_count += 1
        
    
    
    
    def do_update(self, arg):
        """ Update a task: update <id> <new_description> """
        parts = arg.split(maxsplit=1)
        if len(parts) != 2:
            print("Usage: update <id> <new_description>")
            return
        
        try:
            task_id = int(parts[0])
            new_task_description = parts[1]
            
            for task in self.tasks:
                if task["id"] == task_id:
                    task["description"] = new_task_description
                    task["updatedAt"] = date.today().strftime("%d/%m/%Y")
                    print(f"task {task_id} updated successfully.")
                    return
            print(f"❌ Task with id {task_id} not found.")
            
        except ValueError:
            print("Invalid ID.")
        
            
    def do_list(self, arg):
        if not self.tasks:
            print("No tasks found.")
        else:
            print(tabulate(self.tasks, headers="keys", tablefmt="grid", ))
        
            
    def do_delete(self, arg):
        """ Delete a task: delete <id> """
        try:
            task_id = int(arg)
            print(type(task_id))
            for task in self.tasks:
                if task["id"] == task_id:
                    self.tasks.remove(task)
                    print(f"task {task_id} removed successfully.")
                    return
            print(f"❌ Task with id {task_id} not found.")
            
        except ValueError:
            print("Invalid ID.")
        
        
        
    def do_exit(self, arg):
        """Exit the CLI"""
        print("👋 Goodbye!")
        return True
    
if __name__ == '__main__':
    TaskTracker().cmdloop()