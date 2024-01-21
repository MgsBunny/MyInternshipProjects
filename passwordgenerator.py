import tkinter as tk
from tkinter import ttk
import random
import string


class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.length_label = ttk.Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.length_entry = ttk.Entry(master, width=5)
        self.length_entry.insert(0, "12")  # Default length
        self.length_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.number_label = ttk.Label(master, text="Number of Passwords:")
        self.number_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.number_entry = ttk.Entry(master, width=5)
        self.number_entry.insert(0, "1")  # Default number of passwords
        self.number_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.generate_button = ttk.Button(master, text="Generate Passwords", command=self.generate_passwords)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=20)

        self.result_text = tk.Text(master, height=5, width=40)
        self.result_text.grid(row=3, column=0, columnspan=2, pady=10)

    def generate_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def generate_passwords(self):
        try:
            length = int(self.length_entry.get())
            number_of_passwords = int(self.number_entry.get())
        except ValueError:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Invalid input. Please enter valid integers.")
            return

        if length <= 0 or number_of_passwords <= 0:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END,
                                    "Invalid input. Length and number of passwords should be greater than zero.")
            return

        passwords = [self.generate_password(length) for _ in range(number_of_passwords)]

        self.result_text.delete(1.0, tk.END)
        for i, password in enumerate(passwords, start=1):
            self.result_text.insert(tk.END, f"Password {i}: {password}\n")


def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
