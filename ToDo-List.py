import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500")
root.config(bg="#f5f6fa")


def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def update_task():
    try:
        selected = listbox.curselection()[0]
        new_task = entry.get()
        if new_task != "":
            listbox.delete(selected)
            listbox.insert(selected, new_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter updated task!")
    except:
        messagebox.showwarning("Warning", "Select a task to update!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def track_task():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)

        if not task.startswith("✔ "):
            listbox.delete(selected)
            listbox.insert(selected, "✔ " + task)
            listbox.itemconfig(selected, {'fg': 'green'})
    except:
        messagebox.showwarning("Warning", "Select a task to track!")


title = tk.Label(root, text="TO-DO LIST", 
                 font=("Segoe UI", 20, "bold"), 
                 bg="#2f3640", fg="white")
title.pack(fill="x")

entry = tk.Entry(root, font=("Segoe UI", 12))
entry.pack(pady=15, padx=20, fill="x")

btn_frame = tk.Frame(root, bg="#f5f6fa")
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="ADD", width=10,
                    bg="#44bd32", fg="white",
                    command=add_task)
add_btn.grid(row=0, column=0, padx=5)

track_btn = tk.Button(btn_frame, text="TRACK", width=10,
                      bg="#16a085", fg="white",
                      command=track_task)
track_btn.grid(row=0, column=1, padx=5)

update_btn = tk.Button(btn_frame, text="UPDATE", width=10,
                       bg="#273c75", fg="white",
                       command=update_task)
update_btn.grid(row=0, column=2, padx=5)

delete_btn = tk.Button(btn_frame, text="DELETE", width=10,
                       bg="#e84118", fg="white",
                       command=delete_task)
delete_btn.grid(row=0, column=3, padx=5)

listbox = tk.Listbox(root, font=("Segoe UI", 12),
                     selectbackground="#dcdde1")
listbox.pack(pady=20, padx=20, fill="both", expand=True)

root.mainloop()
