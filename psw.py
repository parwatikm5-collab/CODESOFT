import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password():
    length = length_scale.get()

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%&*?"

    characters = ""

    if var_lower.get():
        characters += lower
    if var_upper.get():
        characters += upper
    if var_number.get():
        characters += digits
    if var_symbol.get():
        characters += symbols

    if characters == "":
        messagebox.showwarning("Warning", "Select at least one option!")
        return

    password = ''.join(secrets.choice(characters) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("500x600")
root.config(bg="#0b0f1a")


tk.Label(
    root,
    text="Password Generator",
    font=("Helvetica", 22, "bold"),
    bg="#1e1e2f",
    fg="#1df50a"
).pack(pady=20)

tk.Label(
    root,
    text="Select Password Length",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="sky blue"
).pack()

length_scale = tk.Scale(
    root,
    from_=12,
    to=50,
    orient="horizontal",
    length=50,
    bg="#1e1e2e",
    fg="white",
    troughcolor="#2d2d44",
    highlightthickness=3
)
length_scale.set(16)
length_scale.pack(pady=10)


var_upper = tk.IntVar(value=1)
var_lower = tk.IntVar(value=1)
var_number = tk.IntVar(value=1)
var_symbol = tk.IntVar(value=0)

options_frame = tk.Frame(root, bg="#1e1e2e")
options_frame.pack(pady=15)

def styled_checkbox(text, variable):
    return tk.Checkbutton(
        options_frame,
        text=text,
        variable=variable,
        bg="#1e1e2f",
        fg="white",
        selectcolor="#2d2d44",
        activebackground="#1e1e2f",
        activeforeground="#00f5d4",
        font=("Arial", 11)
    )

styled_checkbox("Include Uppercase (A-Z)", var_upper).pack(anchor="w")
styled_checkbox("Include Lowercase (a-z)", var_lower).pack(anchor="w")
styled_checkbox("Include Numbers (0-9)", var_number).pack(anchor="w")
styled_checkbox("Include Symbols (!@#$)", var_symbol).pack(anchor="w")

generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 14, "bold"),
    bg="#00bbf9",
    fg="dark blue",
    activebackground="#0096c7",
    padx=10,
    pady=5
)
generate_btn.pack(pady=25)
def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()   
        print("Password Copied!")
copy_btn = tk.Button(
    root,
    text="📋 Copy Password",
    command=copy_password,
    bg="#28a745",
    fg="white",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=5
)

copy_btn.pack(pady=10)


password_entry = tk.Entry(
    root,
    font=("Courier", 16, "bold"),
    justify="center",
    bg="#2d2d44",
    fg="#00f5d4",
    bd=0,
    width=25
)
password_entry.pack(pady=15, ipady=8)

tk.Label(
    root,
    text="Secure | Fast | Simple",
    font=("Arial", 9),
    bg="#1e1e2f",
    fg="gray"
).pack(side="top", pady=15)

border_frame = tk.Frame(
    root,
    bg="white",        
    padx=3, pady=3     
)
border_frame.pack(pady=20)
root.mainloop()
