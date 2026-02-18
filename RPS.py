import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x450")
root.config(bg="#7579AD")

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    
    user_label.config(text=f"You chose: {user_choice}")
    comp_label.config(text=f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1
    
    result_label.config(text=result)
    score_label.config(text=f"Score - You: {user_score}  Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_label.config(text="You chose: ")
    comp_label.config(text="Computer chose: ")
    result_label.config(text="")
    score_label.config(text="Score - You: 0  Computer: 0")

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#7579AD")
title.pack(pady=10)

user_label = tk.Label(root, text="You chose: ", font=("Arial", 12), bg="#7579AD")
user_label.pack(pady=5)

comp_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12), bg="#7579AD")
comp_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue", bg="#7579AD")
result_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#7579AD")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

reset_btn = tk.Button(root, text="Reset Game", width=15, bg="red", fg="white", command=reset_game)
reset_btn.pack(pady=15)

score_label = tk.Label(root, text="Score - You: 0  Computer: 0", font=("Arial", 12), bg="#7579AD")
score_label.pack(pady=5)

root.mainloop()
