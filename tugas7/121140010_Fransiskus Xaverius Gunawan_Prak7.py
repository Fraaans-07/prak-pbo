import tkinter as tk
import random

def check_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Seri"
    elif (
        (player_choice == "Gunting" and computer_choice == "Kertas") or
        (player_choice == "Kertas" and computer_choice == "Batu") or
        (player_choice == "Batu" and computer_choice == "Gunting")
    ):
        return "Anda Menang!"
    else:
        return "Anda Kalah!"

def play_game(player_choice):
    global computer_choice
    choices = ["Gunting", "Kertas", "Batu"]
    computer_choice = random.choice(choices)
    result = check_winner(player_choice, computer_choice)
    label_result.config(text=f"Komputer memilih: {computer_choice}\n{result}")

def reset_game():
    label_result.config(text="")
    computer_choice = ""

window = tk.Tk()
window.title("Gunting Kertas Batu")
window.geometry("300x250")

label_title = tk.Label(window, text="Pilih Gunting, Kertas, atau Batu")
label_title.pack(pady=10)

button_gunting = tk.Button(window, text="Gunting", command=lambda: play_game("Gunting"))
button_gunting.pack(pady=5)

button_kertas = tk.Button(window, text="Kertas", command=lambda: play_game("Kertas"))
button_kertas.pack(pady=5)

button_batu = tk.Button(window, text="Batu", command=lambda: play_game("Batu"))
button_batu.pack(pady=5)

button_reset = tk.Button(window, text="Ulangi", command=reset_game)
button_reset.pack(pady=10)

label_result = tk.Label(window, text="")
label_result.pack(pady=10)

window.mainloop()