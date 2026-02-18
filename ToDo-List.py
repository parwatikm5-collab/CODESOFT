import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, f"• {task}")
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Kripya kuch likhiye")

def update_task():
    try:
        index = listbox.curselection()[0]
        new_task = entry.get().strip()

        if new_task:
            listbox.delete(index)
            listbox.insert(index, f"• {new_task}")
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Update karne ke liye text likhiye")

    except IndexError:
        messagebox.showwarning("Selection Error", "Pehle list se task select kariye")


def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Pehle list se task select kariye")


root = tk.Tk()
root.title("Modern To-Do List")
root.geometry("400x500")
root.config(bg="#f5f6fa")

header = tk.Label(root, text="TO-DO LIST",
                  bg="#2f3640", fg="white",
                  font=("Segoe UI", 18, "bold"),
                  pady=10)
header.pack(fill="x")

entry = tk.Entry(root, font=("Segoe UI", 12))
entry.pack(pady=15, padx=20, fill="x")

btn_frame = tk.Frame(root, bg="#f5f6fa")
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="ADD", width=9,
                    bg="#44bd32", fg="white",
                    command=add_task)
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(btn_frame, text="UPDATE", width=9,
                       bg="#273c75", fg="white",
                       command=update_task)
update_btn.grid(row=0, column=2, padx=5)

delete_btn = tk.Button(btn_frame, text="DELETE", width=9,
                       bg="#e84118", fg="white",
                       command=delete_task)
delete_btn.grid(row=0, column=3, padx=5)

listbox = tk.Listbox(root, font=("Segoe UI", 12),
                     selectbackground="#dcdde1")
listbox.pack(pady=20, padx=20, fill="both", expand=True)

root.mainloop()
