
import tkinter as tk
import random

root = tk.Tk()
root.title("Ultra Battle Arena: Pro Edition ⚔️")
root.geometry("500x650") 
root.config(bg="#848c8c") 

player_score = 0
comp_score = 0

game_data = {
    "Rock": {"emoji": "✊", "color": "#4e4e4e"},
    "Paper": {"emoji": "✋", "color": "#3498db"},
    "Scissors": {"emoji": "✌", "color": "#9b59b6"}
}

choices = list(game_data.keys())



title = tk.Label(root, text="ROCK PAPER SCISSORS🎮!",font=("Impact", 32), bg="#848c8c", fg="#101211")
title.pack(pady=20)


score_frame = tk.Frame(root, bg="#1a1a2e")
score_frame.pack(pady=10)

score_label = tk.Label(score_frame, 
                       text=f"YOU: {player_score}  |  COMP: {comp_score}", 
                       font=("Verdana", 18, "bold"), 
                       bg="#848c8c", fg="#f5980c")
score_label.pack()


arena_frame = tk.Frame(root, bg="#16213e", bd=0, highlightbackground="#fffeed", highlightthickness=2)
arena_frame.pack(pady=10, padx=30, fill="x")

player_label = tk.Label(arena_frame, text="YOU\n❓", font=("Verdana", 20, "bold"), bg="#16213e", fg="#00d2ff")
player_label.grid(row=0, column=0, padx=40, pady=30)

vs_label = tk.Label(arena_frame, text="VS", font=("Impact", 24), bg="#16213e", fg="#177a3d")
vs_label.grid(row=0, column=1)

comp_label = tk.Label(arena_frame, text="COMP\n❓", font=("Verdana", 20, "bold"), bg="#16213e", fg="#ff9f43")
comp_label.grid(row=0, column=2, padx=40, pady=30)

status_label = tk.Label(root, text="READY FOR BATTLE?", font=("Segoe UI", 16, "bold"), bg="#848c8c", fg="#ffffff")
status_label.pack(pady=20)


def update_score():
    score_label.config(text=f"YOU: {player_score}  |  COMP: {comp_score}")

def play(user_choice):
    global player_score, comp_score
    computer_choice = random.choice(choices)
    

    player_label.config(text=f"YOU\n{game_data[user_choice]['emoji']}")
    comp_label.config(text=f"COMP\n{game_data[computer_choice]['emoji']}")


    if user_choice == computer_choice:
        result = "DRAW! 🤝"
        res_color = "#95a5a6"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "YOU DOMINATED! 🏆"
        res_color = "#2ecc71"
        player_score += 1 
    else:
        result = "COMP WINS! 💀"
        res_color = "#e74c3c"
        comp_score += 1 

    status_label.config(text=result, fg=res_color)
    update_score()

def reset_game():
    global player_score, comp_score
    player_score = 0
    comp_score = 0
    player_label.config(text="YOU\n❓")
    comp_label.config(text="COMP\n❓")
    status_label.config(text="RESET!", fg="#ffffff")
    update_score()



btn_frame = tk.Frame(root, bg="#1a1a2e")
btn_frame.pack(pady=10)

def create_action_btn(choice):
    data = game_data[choice]
    return tk.Button(btn_frame, text=f"{data['emoji']} {choice}", font=("Arial", 11, "bold"),
                    width=10, height=2, bg=data['color'], fg="white", bd=0, cursor="hand2",
                    command=lambda: play(choice))

create_action_btn("Rock").grid(row=0, column=0, padx=8)
create_action_btn("Paper").grid(row=0, column=1, padx=8)
create_action_btn("Scissors").grid(row=0, column=2, padx=8)


reset_btn = tk.Button(root, text="RESET SCORE", font=("Arial", 9, "bold"),
                      bg="#1a1a2e", fg="#e94560", relief="flat", command=reset_game)
reset_btn.pack(pady=30)

root.mainloop()
