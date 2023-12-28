import tkinter as tk
from tkinter import ttk, messagebox
from quiz_data import quiz_data

class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.current_question = 0
        self.create_start_screen()

    def create_start_screen(self):
        # Create a start screen with a Start Quiz button
        start_label = ttk.Label(
            self.master,
            text="Welcome to the Quiz App!",
            font=("Helvetica", 20, "bold"),
            padding=20
        )
        start_label.pack(pady=20)

        start_button = ttk.Button(
            self.master,
            text="Start Quiz",
            command=self.start_quiz,
            padding=20
        )
        start_button.pack()

    def start_quiz(self):
        # Destroy the start screen and initialize the quiz
        for widget in self.master.winfo_children():
            widget.destroy()
        self.create_widgets()

    def create_widgets(self):
        # Create the question label
        self.qs_label = ttk.Label(
            self.master,
            anchor="center",
            wraplength=500,
            padding=10,
            font=("Helvetica", 12, "bold")  # Question font size and style
        )
        self.qs_label.pack(pady=10)

        # Display the choices on labels
        self.choice_labels = []
        for i in range(4):
            label = ttk.Label(
                self.master,
                text="",
                padding=10,
                borderwidth=2,  # Outline width
                relief="solid",  # Outline style
                font=("Helvetica", 10)  # Choice font size
            )
            label.pack(pady=5, ipadx=20, ipady=10)
            self.choice_labels.append(label)

        # Create an entry widget for user input
        self.entry_label = ttk.Label(self.master, text="Enter option number:")
        self.entry_label.pack(pady=10)
        self.entry_var = tk.StringVar()
        self.entry_widget = ttk.Entry(self.master, textvariable=self.entry_var)
        self.entry_widget.pack(pady=10)

        # Create a submit button
        self.submit_btn = ttk.Button(
            self.master,
            text="Submit",
            command=self.check_user_input
        )
        self.submit_btn.pack(pady=10)

        # Create the feedback label
        self.feedback_label = ttk.Label(
            self.master,
            anchor="center",
            padding=10
        )
        self.feedback_label.pack(pady=10)

        # Initialize the score
        self.score = 0

        # Create the score label
        self.score_label = ttk.Label(
            self.master,
            text="Score: 0/{}".format(len(self.questions)),
            anchor="center",
            padding=10
        )
        self.score_label.pack(pady=10)

        # Create the next button
        self.next_btn = ttk.Button(
            self.master,
            text="Next",
            command=self.next_question,
            state="disabled"
        )
        self.next_btn.pack(pady=10)

        # Show the first question
        self.show_question()

    def show_question(self):
        # Display the current question and choices
        question = self.questions[self.current_question]
        self.qs_label.config(text=question["question"])

        # Display choices on labels
        choices = question["choices"]
        for i in range(4):
            self.choice_labels[i].config(text=f"{i + 1}. {choices[i]}")

        # Remove feedback and enable the submit button
        self.feedback_label.config(text="")
        self.submit_btn.config(state="normal")
        self.next_btn.config(state="disabled")

    def check_user_input(self):
        # Check the user's input when the submit button is pressed
        user_input = self.entry_var.get()
        try:
            user_choice = int(user_input)
            if 1 <= user_choice <= 4:
                self.check_answer(user_choice - 1)
                self.submit_btn.config(state="disabled")  # Disable submit after checking
                self.entry_var.set("")  # Clear the entry widget after checking
            else:
                messagebox.showerror("Error", "Please enter a valid number between 1 and 4")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number between 1 and 4")

    def check_answer(self, choice):
        # Check if the selected choice is correct and update the feedback
        question = self.questions[self.current_question]
        selected_choice = self.choice_labels[choice].cget("text")

        if selected_choice.endswith(question["answer"]):
            self.score += 1
            self.score_label.config(text="Score: {}/{}".format(self.score, len(self.questions)))
            self.feedback_label.config(text="Correct!", foreground="green")
        else:
            correct_answer = next((c for c in question["choices"] if c.endswith(question["answer"])), None)
            self.feedback_label.config(text=f"Incorrect! The correct answer is: {correct_answer}", foreground="red")

        self.next_btn.config(state="normal")

    def next_question(self):
        # Move to the next question or end the quiz if there are no more questions
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Completed",
                                "Quiz Completed! Final score: {}/{}".format(self.score, len(self.questions)))
            self.master.destroy()

def main():
    # Main function to create the Tkinter window and start the quiz app
    root = tk.Tk()
    root.title("Quiz App")
    root.geometry("700x700")  # Adjust the size as needed
    app = QuizApp(root, quiz_data)
    root.mainloop()

if __name__ == "__main__":
    main()
