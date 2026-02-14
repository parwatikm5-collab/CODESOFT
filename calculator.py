import tkinter as tk
root = tk.Tk()
root.title("calculator")
root.geometry("450x620")
root.resizable(False,False)
root.configure(bg="#2c3e50")
for i in range(4): 
    root.columnconfigure(i, weight=1)
for i in range(1, 6): 
    root.rowconfigure(i, weight=1)

entry = tk.Entry(
    root,
    font=("Arial",22),
    bd=8,
    relief="ridge",
    justify="right"
)
entry.pack(fill="both", padx=10, pady=10, ipady=1)

def click(value):
    entry.insert(tk.END, value)
def clear():
    entry.delete(0, tk.END)
def backspace():
    entry.delete(len(entry.get())-1, tk.END)
def calculate():
    try:
        result = eval(entry.get())
        clear()
        entry.insert(0, result)
    except:
        clear()
        entry.insert(0, "Error")
        

frame = tk.Frame(root, bg="#2c3e50")
frame.pack()

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]
row = 0
col = 0

for btn in buttons:
    if btn =="=":
        b = tk.Button(
            frame, text=btn,
            width=5, height=2,
            font=("Arial",14),
            bg="#27ae60", fg="white",
            command=calculate
        )
    else:
        b = tk.Button(
            frame, text=btn,
            width=5, height=2,
            font=("Arial",14),
            bg="#ecf0f1",
            command=lambda x=btn:
click(x)
        )
    b.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col == 4:
        col = 0
        row += 1


extra_frame = tk.Frame(root, bg="#2c3e50")
extra_frame.pack(pady=20)

clear_btn = tk.Button(
    extra_frame, text="CLEAR",
    font=("Arial", 14),
    bg="#e74c3c", fg="white",
    command=clear
)
clear_btn.pack(side="left",expand=False, fill="both", padx=5, pady=10)
back_btn = tk.Button(
    extra_frame, 
    text="BACK", 
    font=("Arial", 14), 
    bg="#f39c12", 
    fg="white",
    width=10,       
    command=backspace
)
back_btn.pack(side="right", expand=False, fill="both", padx=5, pady=10) 

root.mainloop()
