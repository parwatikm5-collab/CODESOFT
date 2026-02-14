import tkinter as tk
from tkinter import messagebox

def add_task(event=None): 
    task = entry.get().strip() 
    if task:
        listbox.insert(tk.END, f"• {task}") 
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Kripya kuch likhiye!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Pehle list se ek task select karein!")

root = tk.Tk()
root.title("Modern To-Do List")
root.geometry("400x500")
root.configure(bg="#f5f6fa")



header = tk.Label(root, text="TO-DO LIST", font=("Segoe UI", 18, "bold"), 
                 bg="#2f3640", fg="white", pady=15)
header.pack(fill="x")


frame = tk.Frame(root, bg="#f5f6fa", pady=10)
frame.pack()

entry = tk.Entry(frame, font=("Segoe UI", 12), width=25, borderwidth=2, relief="groove")
entry.grid(row=0, column=0, padx=5, ipady=3)
entry.bind('<Return>', add_task) 
entry.focus_set() 

add_btn = tk.Button(frame, text="ADD", bg="#4cd137", fg="white", width=8, 
                   font=("Segoe UI", 10, "bold"), command=add_task, cursor="hand2")
add_btn.grid(row=0, column=1)


list_frame = tk.Frame(root, bg="#f5f6fa")
list_frame.pack(pady=10, padx=20, fill="both", expand=False)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(list_frame, font=("Segoe UI", 12), width=30, height=10, 
                    bg="white", fg="#2f3640", borderwidth=0, 
                    yscrollcommand=scrollbar.set, selectbackground="#dcdde1")
listbox.pack(side="left", fill="both", expand=False)

scrollbar.config(command=listbox.yview)


del_btn = tk.Button(root, text="DELETE SELECTED", bg="#e84118", fg="white", 
                   font=("Segoe UI", 10, "bold"), pady=8, command=delete_task, 
                   cursor="hand2", relief="flat")
del_btn.pack(fill="x", padx=20, pady=20)

root.mainloop()
