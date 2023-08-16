import tkinter as tk

root = tk.Tk()

# root.geometry("400x500")
tasks = tk.Variable(value=("ali","hasan"))

add_butt = tk.Button(root, text = "Add")
complete_butt = tk.Button(root, text = "Complete")
lb = tk.Listbox(root,
    listvariable=tasks,
    height=12,
    selectmode=tk.EXTENDED)
lb2 = tk.Listbox(root,
    listvariable=tasks,
    height=12,
    selectmode=tk.EXTENDED)
entry = tk.Entry(root, borderwidth=10, width=50)

entry.grid(row=0, column=0, columnspan=3)
lb.grid(row=1, column=0, rowspan=6)
lb2.grid(row=1, column=2,rowspan=6)
add_butt.grid(row=1, column=1)
complete_butt.grid(row=2, column=1)


