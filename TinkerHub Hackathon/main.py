import tkinter as tk
from tkinter import messagebox
import sneak as s

def start_game():
    messagebox.showinfo("Start Game", "The Game is Starting!!!")

    root = tk.Tk()
    root.title("Select the colours")
    root.geometry("300x300")
    root.configure(bg = "teal")

    def buttona(n):
        d = s.shuffle()
        messagebox.showinfo("Result", s.element(n, d))
        root.quit()


    def init_root(color, nl):
        root = tk.Tk()
        root.title("Select a number")
        root.geometry("300x300")
        root.configure(bg = "white")
        button_ac = [buttona]
        positions = [(0, 0), (0, 1), (1, 0), (1, 1)]
        for i, (row, col) in enumerate(positions):
            button = tk.Button(root, text = str(nl[i]), command=lambda i = i: button_ac[0](nl[i]), bg=color, activebackground=color, relief="flat", width=10, height=5)
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        root.grid_rowconfigure([0, 1], weight=1)
        root.grid_columnconfigure([0, 1], weight=1)

        root.mainloop()


    def button1_action():
        init_root("blue", [1, 3, 6, 8])
        root.quit()

    def button2_action():
        init_root("red", [2, 5, 7, 4])
        root.quit()

    def button3_action():
        init_root("green", [1, 2, 6, 8])
        root.quit()

    def button4_action():
        init_root("yellow", [3, 4, 5, 6])
        

    colors = ["blue", "red", "green", "yellow"]
    button_act = [button1_action, button2_action, button3_action, button4_action]

    positions = [(0, 0), (0, 1), (1, 0), (1, 1)]

    for i, (row, col) in enumerate(positions):
        button = tk.Button(root, text=colors[i].title(), command=button_act[i], bg=colors[i], activebackground=colors[i], relief="flat", width=10, height=5)
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    root.grid_rowconfigure([0, 1], weight=1)
    root.grid_columnconfigure([0, 1], weight=1)

    root.mainloop()


def quit_game():
    root.quit()

root = tk.Tk()
root.title("Tip Top Game")
root.geometry("300x300") 

start_button = tk.Button(root, text="Start Game", command=start_game, width=30)
quit_button = tk.Button(root, text="Quit", command=quit_game, width=30)

start_button.pack(pady=20)
quit_button.pack(pady=20)

root.mainloop()