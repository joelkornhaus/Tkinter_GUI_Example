import tkinter as tk
# much of this code generated with chatgpt

# Create the main application window
root = tk.Tk()
root.title("To-Do List")

# Create a list to store to-do items
tasks = []

# Create a function to add tasks
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)

# Create a function to remove selected tasks
def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_listbox()

# Create a function to update the listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Create entry, listbox, and buttons
entry = tk.Entry(root, width=30)
entry.pack(pady=10,padx=10)

listbox = tk.Listbox(root, selectmode=tk.SINGLE)#, width=30, height=10)
listbox.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5,padx=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5,padx=10)

# Run the Tkinter main loop
root.mainloop()
