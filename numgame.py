import tkinter as tk
import random

# Constants
MAX_ATTEMPTS = 10
RANGE_MIN = 1
RANGE_MAX = 100
BG_COLOR = "#f0f8ff"
HEADER_COLOR = "#4682b4"
TEXT_COLOR = "#333"
BUTTON_COLOR = "#6495ed"
BUTTON_HOVER = "#4169e1"
SUCCESS_COLOR = "#228B22"
FAIL_COLOR = "#B22222"

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("🎯 Number Guessing Game")
        self.master.geometry("400x300")
        self.master.configure(bg=BG_COLOR)
        self.reset_game()
        
        # Header
        self.header = tk.Label(master, text="🎮 Guess the Number!", font=("Helvetica", 18, "bold"), bg=BG_COLOR, fg=HEADER_COLOR)
        self.header.pack(pady=10)
        
        # Instruction
        self.label = tk.Label(master, text=f"Guess a number between {RANGE_MIN} and {RANGE_MAX}:", font=("Arial", 12), bg=BG_COLOR, fg=TEXT_COLOR)
        self.label.pack(pady=5)
        
        # Entry box
        self.entry = tk.Entry(master, font=("Arial", 12), justify="center", width=20)
        self.entry.pack(pady=5)
        
        # Result message
        self.result = tk.Label(master, text="", font=("Arial", 12, "bold"), bg=BG_COLOR)
        self.result.pack(pady=8)

        # Attempts left
        self.attempts_label = tk.Label(master, text=f"Attempts left: {self.attempts}", font=("Arial", 12), bg=BG_COLOR, fg=TEXT_COLOR)
        self.attempts_label.pack(pady=4)
        
        # Submit Button
        self.submit_button = tk.Button(master, text="✅ Submit Guess", font=("Arial", 11, "bold"), bg=BUTTON_COLOR, fg="white", command=self.check_guess, activebackground=BUTTON_HOVER)
        self.submit_button.pack(pady=6)

        # Reset Button
        self.reset_button = tk.Button(master, text="🔁 Restart Game", font=("Arial", 11, "bold"), bg="#dcdcdc", fg="black", command=self.reset_game)
        self.reset_button.pack()

    def reset_game(self):
        self.target = random.randint(RANGE_MIN, RANGE_MAX)
        self.attempts = MAX_ATTEMPTS
        if hasattr(self, 'result'):
            self.result.config(text="", fg=TEXT_COLOR)
        if hasattr(self, 'attempts_label'):
            self.attempts_label.config(text=f"Attempts left: {self.attempts}")
        if hasattr(self, 'entry'):
            self.entry.delete(0, tk.END)
        if hasattr(self, 'submit_button'):
            self.submit_button.config(state=tk.NORMAL)

    def check_guess(self):
        guess = self.entry.get()
        try:
            guess = int(guess)
        except ValueError:
            self.result.config(text="⚠️ Please enter a valid integer!", fg=FAIL_COLOR)
            return
        
        self.attempts -= 1
        self.attempts_label.config(text=f"Attempts left: {self.attempts}")

        if guess > self.target:
            self.result.config(text="📉 Too high!", fg=FAIL_COLOR)
        elif guess < self.target:
            self.result.config(text="📈 Too low!", fg=FAIL_COLOR)
        else:
            self.result.config(text=f"🎉 Congratulations! You guessed it right: {self.target}", fg=SUCCESS_COLOR)
            self.submit_button.config(state=tk.DISABLED)
            return

        if self.attempts == 0 and guess != self.target:
            self.result.config(text=f"❌ Game Over! The number was {self.target}", fg=FAIL_COLOR)
            self.submit_button.config(state=tk.DISABLED)

# Launch the game
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
