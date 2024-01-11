import tkinter as tk
from tkinter import ttk, messagebox
from collections import defaultdict
import calendar
import datetime

class ExpenseTrackerApp:
    def __init__(self, root):
        # Initialize the application
        self.root = root
        self.root.title("Expense Tracker")

        # Data storage
        self.expenses = []  # List to store individual expenses
        self.categories = defaultdict(float)  # Dictionary to store total expenses per category

        # User interface components
        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_entry = tk.Entry(root)

        self.description_label = tk.Label(root, text="Description:")
        self.description_entry = tk.Entry(root)

        self.category_label = tk.Label(root, text="Category:")
        self.category_entry = tk.Entry(root)

        self.submit_button = tk.Button(root, text="Submit", command=self.submit_expense)

        self.monthly_summary_button = tk.Button(root, text="Monthly Summary", command=self.show_monthly_summary)

        # Treeview for displaying expenses
        self.tree = ttk.Treeview(root, columns=('Amount', 'Description', 'Category', 'Date'))
        self.tree.heading('#0', text='ID')  # ID column for Treeview
        self.tree.heading('Amount', text='Amount')
        self.tree.heading('Description', text='Description')
        self.tree.heading('Category', text='Category')
        self.tree.heading('Date', text='Date')
        self.tree.column('#0', stretch=tk.NO, width=40)  # Set column width
        self.tree.column('Amount', stretch=tk.YES, width=80)
        self.tree.column('Description', stretch=tk.YES, width=150)
        self.tree.column('Category', stretch=tk.YES, width=80)
        self.tree.column('Date', stretch=tk.YES, width=100)

        # Grid layout
        self.amount_label.grid(row=0, column=0, padx=10, pady=10)
        self.amount_entry.grid(row=0, column=1, padx=10, pady=10)

        self.description_label.grid(row=1, column=0, padx=10, pady=10)
        self.description_entry.grid(row=1, column=1, padx=10, pady=10)

        self.category_label.grid(row=2, column=0, padx=10, pady=10)
        self.category_entry.grid(row=2, column=1, padx=10, pady=10)

        self.submit_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.monthly_summary_button.grid(row=5, column=0, columnspan=2, pady=10)

    def submit_expense(self):
        # Function to handle expense submission
        amount = self.amount_entry.get()
        description = self.description_entry.get()
        category = self.category_entry.get()

        if amount and description and category:
            try:
                amount = float(amount)
                expense = {
                    "Amount": amount,
                    "Description": description,
                    "Category": category,
                    "Date": datetime.date.today()
                }
                # Update data structures and UI
                self.expenses.append(expense)
                self.categories[category] += amount
                self.update_treeview(expense)
                messagebox.showinfo("Success", "Expense submitted successfully!")
                self.clear_entries()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid numerical amount.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def show_monthly_summary(self):
        # Function to display monthly expense summary
        today = datetime.date.today()
        month_range = calendar.monthrange(today.year, today.month)
        first_day = datetime.date(today.year, today.month, 1)
        last_day = datetime.date(today.year, today.month, month_range[1])

        monthly_expenses = [expense for expense in self.expenses if first_day <= expense["Date"] <= last_day]

        if not monthly_expenses:
            messagebox.showinfo("Monthly Summary", "No expenses for the current month.")
            return

        total_expenses = sum(expense["Amount"] for expense in monthly_expenses)

        summary_text = f"Total Expenses for {today.strftime('%B %Y')}:\n\n"

        for category, amount in self.categories.items():
            summary_text += f"{category}: ${amount:.2f}\n"

        summary_text += f"\nTotal: ${total_expenses:.2f}"

        messagebox.showinfo("Monthly Summary", summary_text)

    def update_treeview(self, expense):
        # Function to update the Treeview with the latest expense
        expense_id = len(self.expenses)
        self.tree.insert('', 'end', iid=expense_id, values=(expense["Amount"], expense["Description"],
                                                             expense["Category"], expense["Date"]))

    def clear_entries(self):
        # Function to clear input entries after submitting an expense
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)

if __name__ == "__main__":
    # Run the application
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()
