import sqlite3
from datetime import datetime

class Expense:
    def __init__(self, id, amount, category, description, date):
        self.id = id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def __str__(self):
        return f"ID: {self.id} | Amount: ${self.amount} | Category: {self.category} | Description: {self.description} | Date: {self.date}"

class ExpenseTracker:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS expenses
                            (id INTEGER PRIMARY KEY,
                             amount REAL,
                             category TEXT,
                             description TEXT,
                             date DATE)''')
        self.conn.commit()

    def add_expense(self, amount, category, description, date):
        self.cur.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                         (amount, category, description, date))
        self.conn.commit()

    def get_expenses_by_date(self, date):
        self.cur.execute("SELECT * FROM expenses WHERE date = ?", (date,))
        rows = self.cur.fetchall()
        return [Expense(*row) for row in rows]

    def get_total_spent(self, date):
        self.cur.execute(f"SELECT SUM(amount) FROM expenses WHERE date = '{date}'")
        total_spent = self.cur.fetchone()[0]
        return total_spent if total_spent else 0

    def __del__(self):
        self.conn.close()

def main():
    db_name = 'expenses.db'
    tracker = ExpenseTracker(db_name)
    
    while True:
        print("\nExpense Tracking System")
        print("1. Add Expense")
        print("2. View Expenses for a Date")
        print("3. View Total Spent for a Date")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter amount: $"))
            category = input("Enter category: ")
            description = input("Enter description: ")
            date_str = input("Enter date (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, '%Y-%m-%d')
            tracker.add_expense(amount, category, description, date)
            print("Expense added successfully.")

        elif choice == "2":
            date_str = input("Enter date (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, '%Y-%m-%d')
            expenses = tracker.get_expenses_by_date(date)
            if expenses:
                print(f"Expenses for {date_str}:")
                for expense in expenses:
                    print(expense)
            else:
                print("No expenses found for the given date.")

        elif choice == "3":
            date_str = input("Enter date (YYYY-MM-DD): ")
            date = datetime.strptime(date_str, '%Y-%m-%d')
            total_spent = tracker.get_total_spent(date)
            print(f"Total spent on {date_str}: ${total_spent}")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
