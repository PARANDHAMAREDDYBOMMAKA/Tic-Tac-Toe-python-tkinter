import tkinter as tk
from tkinter import messagebox


class AnimatedTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - Enhanced UI")
        self.root.geometry("600x600")
        self.root.configure(bg="#1e1e1e")
        self.current_player = "X"
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        self.winning_line = []

    def create_board(self):
        title = tk.Label(
            self.root,
            text="Tic Tac Toe",
            font=("Arial", 36, "bold"),
            bg="#1e1e1e",
            fg="#f5f5f5"
        )
        title.pack(pady=10)

        frame = tk.Frame(self.root, bg="#1e1e1e")
        frame.pack(expand=True)

        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    frame,
                    text="",
                    font=("Helvetica", 28, "bold"),
                    width=6,
                    height=3,
                    bg="#2e2e2e",
                    fg="#f5f5f5",
                    relief="raised",
                    command=lambda r=row, c=col: self.on_click(r, c),
                )
                button.grid(row=row, column=col, padx=10, pady=10)
                button.bind("<Enter>", lambda e, btn=button: btn.config(bg="#3a3a3a"))
                button.bind("<Leave>", lambda e, btn=button: btn.config(bg="#2e2e2e" if btn["text"] == "" else btn["bg"]))
                self.buttons[row][col] = button

    def on_click(self, row, col):
        if self.board[row][col] is not None:
            return
        self.board[row][col] = self.current_player
        self.animate_button_press(self.buttons[row][col], self.current_player)
        if self.check_winner():
            self.highlight_winner()
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.reset_board()
        elif self.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_board()
        else:
            self.current_player = "O" if self.current_player == "X" else "X"

    def animate_button_press(self, button, player):
        target_color = "#e74c3c" if player == "X" else "#3498db"
        def fade_in(step=0):
            if step > 255:
                button.config(text=player, fg=target_color, bg="#3a3a3a")
                return
            color = f"#{int(46 + step/10):02x}{int(46 + step/10):02x}{int(46 + step/10):02x}"
            button.config(bg=color)
            button.after(10, fade_in, step + 15)
        fade_in()

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] is not None:
                self.winning_line = [(i, 0), (i, 1), (i, 2)]
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] is not None:
                self.winning_line = [(0, i), (1, i), (2, i)]
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] is not None:
            self.winning_line = [(0, 0), (1, 1), (2, 2)]
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] is not None:
            self.winning_line = [(0, 2), (1, 1), (2, 0)]
            return True
        return False

    def highlight_winner(self):
        def glow(step=0):
            glow_color = f"#{255-step:02x}{215+step//2:02x}00"
            for row, col in self.winning_line:
                self.buttons[row][col].config(bg=glow_color)
            if step >= 255:
                return
            self.root.after(50, glow, step + 15)
        glow()

    def is_draw(self):
        return all(self.board[row][col] is not None for row in range(3) for col in range(3))

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = None
                button = self.buttons[row][col]
                button.config(text="", bg="#2e2e2e")
        self.current_player = "X"


if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedTicTacToe(root)
    root.mainloop()
