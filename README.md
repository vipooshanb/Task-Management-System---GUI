**🗂 Task Management System**

**Technologies Used**: Python, Tkinter, JSON, Dictionary

🔧 **Overview**
This is a desktop-based Task Management System designed using Python and Tkinter for the graphical user interface. 
It helps users add, view, update, and delete their tasks in an organized manner. 
All task data is persistently stored in a JSON file using Python dictionaries, ensuring structured and reliable task tracking.

💡 Key Features
✅ **Add Task**
Users can add new tasks through an easy-to-use input form.

Each task includes essential details like title, description, and possibly a due date or priority.

📝 **Update Task**
Tasks can be edited via a pop-up window.

Users select a task from a list, edit the contents, and save changes.

Real-time update to the JSON file ensures data consistency.

🗑 **Delete Task**
Allows users to delete specific tasks.

Tasks are shown in a list where the user selects one and clicks “Delete.”

The deleted task is removed from both the display and the JSON file.

📁 **JSON Data Handling**
Tasks are stored as dictionaries within a JSON file.
When the application starts, it loads tasks from the file, and all changes are saved automatically.

🖥 **GUI Highlights**
Built using Tkinter, Python’s standard GUI library.
Modular design for each functionality (Add, Update, Delete).

🎯 **Purpose and Benefits**
Helps individuals manage daily tasks efficiently.
Lightweight and fast – ideal for personal use or as a base for larger systems.
