from tkinter import Tk, Label, Entry, Button, Listbox, Scrollbar, END
from datetime import datetime

def add_task():
    task = task_entry.get()
    due_date = due_date_entry.get()
    if task and due_date:
        task_with_due_date = f"{task} - Due: {due_date}"
        task_listbox.insert(END, task_with_due_date)
        sort_tasks_by_due_date()
        task_entry.delete(0, END)
        due_date_entry.delete(0, END)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

def sort_tasks_by_due_date():
    tasks = task_listbox.get(0, END)
    sorted_tasks = sorted(tasks, key=lambda task: extract_due_date(task))
    task_listbox.delete(0, END)
    for task in sorted_tasks:
        task_listbox.insert(END, task)

def extract_due_date(task_with_due_date):
    due_date_str = task_with_due_date.split(" - Due: ")[-1]
    return datetime.strptime(due_date_str, "%Y-%m-%d")

# Create the main window
root = Tk()
root.title("To-Do List")

# Create and position the UI elements
task_label = Label(root, text="Enter a task:")
task_label.pack()

task_entry = Entry(root, width=30)
task_entry.pack()

due_date_label = Label(root, text="Enter due date (YYYY-MM-DD):")
due_date_label.pack()

due_date_entry = Entry(root, width=30)
due_date_entry.pack()

add_button = Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

task_listbox = Listbox(root, width=50)
task_listbox.pack(side="left")

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Start the main event loop
root.mainloop()
