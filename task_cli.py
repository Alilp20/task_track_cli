import cmd
from datetime import date
from tabulate import tabulate
import json
import os

class TaskTracker(cmd.Cmd):
    intro = 'Welcome to the Task Tracker!\n'
    prompt = 'task-cli> '
    
    if not os.path.exists("tasks.json") :
        with open("tasks.json", "w") as tasks:
            json.dump([],tasks)
    
    def do_add(self, arg):
        """ Add a task: add <new_description>"""
        if not arg:
            print("Usage: add <task_description>")
        else:
            arg = arg.strip('"')
            today = date.today().strftime("%d/%m/%Y")
            with open("tasks.json", "r") as file:
                data = json.load(file)
                if data :
                    for task in data:
                        task_id = max(task["id"])
                    task_id += 1
                else :
                    task_id = 1
        
            new_task = {
                "id" : task_id,
                "description" : arg,
                "status" : "to-do",
                "createdAt" : today,
                "updatedAt" : today
            }
            
            data.append(new_task)
            
            with open("tasks.json", "w") as file :
                json.dump(data, file, indent=6)
            
            print(f"✅ Task {arg} added.")
        
    
    
    
    def do_update(self, arg):
        """ Update a task: update <id> <new_description> """
        parts = arg.split(maxsplit=1)
        if len(parts) != 2:
            print("Usage: update <id> <new_description>")
            return
        
        try:
            task_id = int(parts[0])
            new_task_description = parts[1].strip('"')
            found = False
            
            with open("tasks.json", "r") as file:
                data = json.load(file)
                
            if data:
                for task in data:
                    if task["id"] == task_id:
                        found = not found
                        task["description"] = new_task_description
                        task["updatedAt"] = date.today().strftime("%d/%m/%Y")
                        with open("tasks.json", "w") as f:
                            json.dump(data, f, indent=6)
                        print(f"task {task_id} updated successfully.")
                        return
                        
            else:
                print("No tasks available")
                
            print(f"❌ Task with id {task_id} not found.")
            
        except ValueError:
            print("Invalid ID.")
        
            
    def do_list(self):
        with open("tasks.json", "r") as f:
            data = json.load(f)
            
        if not data:
            print("No tasks found.")
        else:
            print(tabulate(data, headers="keys", tablefmt="grid", ))
        
            
    def do_delete(self, arg):
        """ Delete a task: delete <id> """
        try:
            task_id = int(arg)
            with open("tasks.json", "r") as file:
                data = json.load(file)
            
            if data:
                new_data = [task for task in data if task["id"] != task_id]
                
            with open("tasks.json", "w") as f:
                json.dump(new_data, f, indent=6)

            print(f"❌ Task with id {task_id} not found.") if data == new_data else print(f"✅ Task with id {task_id} was removed.") 
            
        except ValueError:
            print("Invalid ID.")
        
        
        
    def do_exit(self, arg):
        """Exit the CLI"""
        print("👋 Goodbye!")
        return True
    
if __name__ == '__main__':
    TaskTracker().cmdloop()