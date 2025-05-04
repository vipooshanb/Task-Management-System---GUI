#Author - B.Vipooshan
#stage --03


import json


# crate a test.json file into data folder
Task_File = "data/test.json"


# Load Function
def load_tasks():
    try:
        with open(Task_File, "r") as file:   # open file in read mode
            return json.load(file)      
    except (FileNotFoundError , json.JSONDecodeError):
        return []

# writing function for saves the tasks to tasks_file
def save_tasks(tasks):
    with open(Task_File, "w") as file:
        json.dump(tasks, file , indent=4)


# Functions for CRUD operations
def add_task():
    print()
    print("- - - > ADD TASKS < - - -")
    
    # Getting tasks information about tasks 
    print("-Enter following Tasks Details")

    # 01. Task name 
    while True:
        task_name = input("Task name --: ")
        if task_name:
            break
        else:
            print("Error! please enter your Task name ")

    # 02. Description
    while True:
        description = input("Task description --: ")
        if description:
            break
        else:
            print("Error! please enter your Task description ")
    
    # 03. Priority
        # Input Validation
    while True:
        priority_list = ['low', 'medium', 'high']
        priority = input("Task priority [Low|Medium|High] --: ").lower()
        if priority in priority_list:
            break
        else:
            print("Invalid input please enter [low|medium|high]")

    # 04. Due_date
        # Date input Validation (month , day)
    while True:
        due_date = input("Task Due date (DD.MM.YYYY) --: ")
        try:
            day = int(due_date[0:2])
            month = int(due_date[3:5])
            year = int(due_date[6:10])
            
            # Month input validation
            if month < 1 or month > 12:
                print("Invalid month. Please enter between 1-12.")
                continue
                
            # Month-day validation
            # 1st validation for Feburary month (28/29)
            if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
                day_end = 29
            # Which month ends in 31 Validation
            elif month in [1,3,5,7,8,10,12]:
                day_end = 31
            # Which months ends in 30 validation
            elif month in [4,6,9,11]:
                day_end = 30  
            else:
                day_end = 28        # else Non - leep years feb 28 days 
            
            if 1 <= day <= day_end and len(due_date) == 10 and due_date[2] == '.' and due_date[5] == '.':   
                break
            else:
                print(f"Invalid inputs. Please enter between 1-{day_end} for month {month}.")
        except ValueError:
            print("Invalid date format. Please use DD.MM.YYYY this format.") 
    #Store to list
    task = {
        "name":task_name,
        "description": description,
        "priority": priority,
        "due_date": due_date
        }
    # add task to tasks list
    tasks.append(task)
    save_tasks(tasks)
    print(f"""
--------------------------------------------
* Your Task ({task['name']}) has been added to JSON File successfully ! 
--------------------------------------------""")



def view_tasks():
    print()
    print(" - - - > VIEW TASKS < - - - ")
    if tasks:
        # Using loop to view all tasks which are stored in list
        for i in range(len(tasks)):
            print(f"Tasks {i + 1}")
            # View Task Design Table
            print(f'''
+--------------------+------------------------------------------------+
|     Name           |     {tasks[i]['name']}                              
+--------------------+------------------------------------------------+
|  Description       |     {tasks[i]['description']}                              
+--------------------+------------------------------------------------+
|     Priority       |     {tasks[i]['priority']}                              
+--------------------+------------------------------------------------+
|     Due_Date       |     {tasks[i]['due_date']}                              
+--------------------+------------------------------------------------+''')
    else:
         print("""
-------------------------------------------------------
* No Tasks available
-------------------------------------------------------""")  # Does no have any task print no available




#Writing Update task to update tasks
def update_task():
    print()
    print(" - - - > UPDATE TASK < - - - ")
    if tasks:
        try:
            get_user_task_id = int(input("Enter the task number to update: "))
            update_task_id = get_user_task_id - 1
            if 0 <= update_task_id < len(tasks):
                task = tasks[update_task_id]
                print(f'''
Your Current Task Is 
-------------------------------------------------------
Name: {task['name']}
Description: {task['description']}
Priority: {task['priority']}
Due Date: {task['due_date']}
-------------------------------------------------------''')

                print("Press Enter to keep the current value")
                task['name'] = input("Enter the Task name: ") or task['name']
                task['description'] = input("Enter the Task description: ") or task['description']

                # Priority
                priority_list = ['low', 'medium', 'high']
                while True:
                    new_priority = input(f"Enter the priority (Low|Medium|High) (current: {task['priority']}): ")
                    if not new_priority:
                        break
                    elif new_priority.lower() in priority_list:
                        task['priority'] = new_priority.lower()
                        break
                    else:
                        print("Invalid input. Please enter Low, Medium, or High.")

                # Due date
                while True:
                    new_due_date = input(f"Task Due date (DD.MM.YYYY) (current: {task['due_date']}): ") or task['due_date']
                    try:
                        day = int(new_due_date[0:2])
                        month = int(new_due_date[3:5])
                        year = int(new_due_date[6:10])

                        if month < 1 or month > 12:
                            print("Invalid month. Please enter between 1-12.")
                            continue

                        if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
                            day_end = 29
                        elif month in [1,3,5,7,8,10,12]:
                            day_end = 31
                        elif month in [4,6,9,11]:
                            day_end = 30
                        else:
                            day_end = 28

                        if 1 <= day <= day_end and len(new_due_date) == 10 and new_due_date[2] == '.' and new_due_date[5] == '.':
                            task['due_date'] = new_due_date
                            break
                        else:
                            print(f"Invalid inputs. Please enter between 1-{day_end} for month {month}.")
                    except ValueError:
                        print("Invalid date format. Please use DD.MM.YYYY format.")

                save_tasks(tasks)
                print("""
-------------------------------------------------------
* Task Updated Successfully
-------------------------------------------------------""")
            else:
                print("Invalid Task number")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("""
-------------------------------------------------------
* No Tasks available to Update
-------------------------------------------------------""")



# Delete Function
def delete_task():
    print()
    print("- - -> DELETE TASK <- - -")
    if tasks:
        try:
            get_User_task_id = int(input("Enter the task number to delete: "))
            del_task = get_User_task_id - 1
            if 0 <= del_task < len(tasks):
                deleted_task = tasks[del_task]['name']
                del tasks[del_task]
                save_tasks(tasks)
                print(f"""
-------------------------------------------------------
* Task '{deleted_task}' Deleted Successfully!
-------------------------------------------------------""")
            else:
                print("Invalid Task Number.")
        except ValueError:
            print("Invalid Task number.")
    else:
        print("""
-------------------------------------------------------
* No Tasks to delete.
-------------------------------------------------------""")

#load tasks
tasks = load_tasks()

# Main program 
if __name__== "__main__":
    print("- - - - > Task Management System < - - - - ")
    while True:
        print()
        print("1. Add_tasks")
        print("2. View_tasks")
        print("3. Update_tasks")
        print("4. Delete_tasks")
        print("5. Exit")

        try: # Giving input validation
                user_choice = int(input("Enter the option (1-5) :: "))
                if 1 <= user_choice <= 5:
                        if user_choice == 1:
                            add_task()
                        elif user_choice == 2:
                            view_tasks()
                        elif user_choice == 3:
                            update_task()
                        elif user_choice == 4:
                            delete_task()
                        elif user_choice == 5:
                            print("""
-------------------------------------------------------
Exiting The Program Thank you. !
------------------------------------------------------""")
                            break
                else:
                    print("Invalid! Please Enter Number (1-5)--> :")
        except ValueError:
            print("Invalid Input Please Enter a number --> :")
