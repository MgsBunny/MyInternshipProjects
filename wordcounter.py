import tkinter as tk
from tkinter import ttk

def count_words():
    # Get text from the entry widget
    input_text = text_entry.get()

    # Check for empty input
    if not input_text.strip():
        word_count_label.config(text="Error: Empty input. Please enter a sentence or paragraph.")
        return

    # Split the input text into words and count them
    words_count = len(input_text.split())
    word_count_label.config(text=f"Word Count: {words_count}")

# Create the main window
root = tk.Tk()
root.title("Word Counter")

# Create and place the entry widget
text_entry = ttk.Entry(root, width=50, font=("Helvetica", 20))
text_entry.grid(row=0, column=0, padx=50, pady=50, columnspan=2)

# Create and place the count button
count_button = ttk.Button(root, text="Count Words", command=count_words)
count_button.grid(row=1, column=0, pady=10, columnspan=2)

# Create and place the word count label
word_count_label = ttk.Label(root, text="Word Count: 0", font=("Helvetica", 14, "bold"))
word_count_label.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

# Start the main event loop
root.mainloop()
