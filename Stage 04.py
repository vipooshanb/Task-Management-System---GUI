#Author - B.Vipooshan
#Stagr -- 04

import json
import tkinter as tk
from tkinter import ttk


class Task:
    def __init__(self, name, description, priority, due_date):
        self.name = name
        self.description = description
        self.priority = priority.capitalize() if priority else "Low"
        self.due_date = due_date

    # Convert object to dictionary 
    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "priority": self.priority,
            "due_date": self.due_date }


class TaskManager:
    def __init__(self, json_file="data/test.json"):
        self.json_file = json_file
        self.tasks = []
        self.original_tasks = []  
        self.load_tasks_from_json()

    # Load tasks from a JSON file     
    def load_tasks_from_json(self):
        try:
            with open(self.json_file, 'r') as file:
                task_dicts = json.load(file)
                self.tasks = [Task(
                            name=task["name"],
                            description=task["description"],
                            priority=task["priority"],
                            due_date=task["due_date"]) for task in task_dicts]

                self.original_tasks = self.tasks.copy()
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []
            self.original_tasks = []

    def get_filtered_tasks(self, name_filter=None, priority_filter=None, duedate_filter=None):
        filtered_tasks = self.original_tasks
        
        if name_filter:
            filtered_tasks = [task for task in filtered_tasks if name_filter.lower() in task.name.lower()]
            
        if priority_filter:
            priority_filter = priority_filter.capitalize()
            filtered_tasks = [task for task in filtered_tasks if task.priority == priority_filter]
            
        if duedate_filter:
            filtered_tasks = [task for task in filtered_tasks if task.due_date == duedate_filter]
            
        return filtered_tasks

    def sort_tasks(self, sort_key='name'):
        reverse = False
        try:
            if sort_key == 'due_date':
                def date_key(task):
                    try:
                        return task.due_date
                    except ValueError:
                        return "9999-12-31"
                self.tasks.sort(key=date_key, reverse=reverse)
            elif sort_key == 'priority':
                priority_order = {'High': 0, 'Medium': 1, 'Low': 2}
                self.tasks.sort(key=lambda x: priority_order.get(x.priority, 3))
            else:
                self.tasks.sort(key=lambda x: getattr(x, sort_key).lower())
        except Exception as e:
            print(f"Error sorting tasks: {e}")


class TaskManagerGUI:
    def __init__(self, Window):
        self.Window = Window
        self.Window.title("Personal Task Manager")
        
        self.task_manager = TaskManager()
        self.setup_gui()

    # Design 
    def setup_gui(self):
        # Background Color
        self.Window.configure(bg="#0078d4")  

        # Title
        title_label = tk.Label(self.Window,
                               text="Task Management System",
                               font=("Segoe UI", 20, "bold italic"),
                               bg="#0078d4", fg="white")
        title_label.grid(row=0, column=0, pady=(15, 0), columnspan=3, sticky="n")

        # Subtitle
        subtitle_label = tk.Label(self.Window,
                                  text="'Plan. Do. Repeat.'",
                                  font=("Segoe UI", 12, "bold italic"),
                                  bg="#0078d4",
                                  fg="white")
        subtitle_label.grid(row=1,
                            column=0,
                            columnspan=3,
                            pady=(0, 10),
                            sticky="n")

        # task display & filter frame
        content_frame = tk.Frame(self.Window, bg="#0078d4")
        
        content_frame.grid(row=2,
                           column=0,
                           columnspan=2,
                           padx=20, pady=10,
                           sticky="nsew")
        
        self.Window.grid_rowconfigure(2, weight=1)
        self.Window.grid_columnconfigure(0, weight=1)

        # Treeview Table(added task view table)
        self.tree = ttk.Treeview(content_frame, columns=("Name", "Description", "Priority", "Due Date"), show="headings", height=15)
        self.tree.grid(row=0,
                       column=0,
                       padx=(0, 10),
                       pady=5,
                       sticky="nsew")

        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", background="black", foreground="white", font=('Segoe UI', 10, 'bold italic'))
        style.configure("Treeview",
                        font=('Segoe UI', 10, "bold"),
                        rowheight=25,
                        background="white",
                        foreground="black")
        
        for col in ("Name", "Description", "Priority", "Due Date"):
            self.tree.heading(col, text=col, command=lambda c=col.lower(): self.sort_tasks(c))
            self.tree.column(col,
                             width=150,
                             anchor="center")

        # Filter Frame (Right Side)
        filter_frame = tk.LabelFrame(content_frame, 
                             text="(:Filter Tasks:) ", 
                             bg="#0078d4",         
                             fg="white",         
                             font=("Segoe UI", 11, "bold italic"),
                             padx=15, pady=10,
                             relief="groove",
                             bd=3)

        filter_frame.grid(row=0,
                          column=2,
                          padx=(10, 0), pady=5,
                          sticky="n")

        # Filters (stacked vertically)
        name_text = tk.Label(filter_frame, text=" Name:",
                             font=("Segoe UI", 9, "bold italic"),
                             bg="#007acc", fg="white")
        
        name_text.grid(row=0, column=0, sticky="w", pady=(0, 2))
        
        self.name_filter_var = tk.StringVar()
        
        ttk.Entry(filter_frame, textvariable=self.name_filter_var, width=25).grid(row=1, column=0, pady=(0, 10))

        priority_text = tk.Label(filter_frame, text="Priority:",
                             font=("Segoe UI", 9, "bold italic"),
                             bg="#007acc",
                                 fg="white")
        
        priority_text.grid(row=2,
                           column=0,
                           sticky="w",
                           pady=(0, 2))
        
        self.priority_filter_var = tk.StringVar()
        
        ttk.Combobox(filter_frame, textvariable=self.priority_filter_var,
                     
                     values=["Show All Tasks", "High", "Medium", "Low"], state="readonly", width=23).grid(row=3, column=0, pady=(0, 10))

        due_date_text = tk.Label(filter_frame, text="Due Date (YYYY-MM-DD):",
                                             font=("Segoe UI", 9, "bold italic"),
                                             bg="#007acc",
                                             fg="white")
        due_date_text.grid(row=4,
                           column=0,
                           sticky="w",
                           pady=(0, 2))
        
        self.due_date_filter_var = tk.StringVar()
        
        ttk.Entry(filter_frame, textvariable=self.due_date_filter_var, width=25).grid(row=5, column=0, pady=(0, 10))

        apply_filter_button = tk.Button(filter_frame, 
                  text=" Apply Filter", 
                  command=self.apply_filter, 
                  bg="#0078d4",       
                  fg="white",       
                  activebackground="white",
                  font=("Segoe UI", 10, "bold italic"),
                  relief="raised", 
                  bd=2)
        apply_filter_button.grid(row=6, column=0, pady=10)


        
                # Exit Button 
        exit_button = tk.Button(self.Window,
                                text="Exit",
                                command=self.Window.destroy,
                                bg="black",
                                fg="white",
                                font=("Segoe UI", 10, "bold italic"),
                                relief="raised",
                                bd=1,
                                padx=10, pady=5)
        exit_button.grid(row=3, column=0, columnspan=3, pady=(0, 15), sticky="e", padx=20)

        self.populate_tree()

    def populate_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for task in self.task_manager.tasks:
            self.tree.insert("", "end", values=(task.name, task.description, task.priority, task.due_date))

    def apply_filter(self):
        name_filter = self.name_filter_var.get() or None
        priority_filter = self.priority_filter_var.get() or None
        if priority_filter == "Show All Tasks":
            priority_filter = None
        due_date_filter = self.due_date_filter_var.get() or None
        
        filtered_tasks = self.task_manager.get_filtered_tasks(name_filter, priority_filter, due_date_filter)
        
        self.task_manager.tasks = filtered_tasks
        
        self.populate_tree()

    def sort_tasks(self, sort_key):
        self.task_manager.sort_tasks(sort_key)
        self.populate_tree()



if __name__ == "__main__":
    Window = tk.Tk()
    app = TaskManagerGUI(Window)
    Window.mainloop()
