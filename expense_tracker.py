# Import necessary modules
from expense import Expense  # Assuming you have an Expense class defined in the 'expense' module
import datetime

# Define the main function
def main():
    print(f"Running expense Tracker!")

    # Set the path for the expense file and the budget
    expense_file_path = "expenses.csv"
    budget = 2000

    # Get user input for expense
    expense = get_user_expense()

    # Write the user's expense to a file
    save_expense_to_file(expense, expense_file_path)

    # Read the file and summarize expenses
    summarize_expense(expense_file_path, budget)

# Function to get user's expense input
def get_user_expense():
    print("Getting user expense")
    expense_name = input("Enter expense name:")
    expense_amount = float(input("Enter expense amount:"))
    print(f"You've entered {expense_amount}$")

    # Define expense categories
    expense_categories = [
        "🍔 Food",
        "🏡 Home",
        "💼 Work",
        "🎉 Fun",
        "📦 Misc"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid Category. Please try again!")

# Function to save an expense to a file
def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving user Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

# Function to summarize expenses
def summarize_expense(expense_file_path, budget):
    print("Summarizing user expenses")
    expenses: list[Expense] = []

    # Read expenses from the file
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_amount, expense_category = line.strip().split(",")
            line_expense = Expense(
                name=expense_name, amount=float(expense_amount), category=expense_category
            )
            print(line_expense)
            expenses.append(line_expense)

    # Calculate total expenses by category
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print(f"Expense by Category:")
    for key, amount in amount_by_category.items():
        print(f" {key}: ${amount:.2f}")

    # Calculate total spent and remaining budget
    total_spent = sum([x.amount for x in expenses])
    print(f"💶 Total Spent: ${total_spent:.2f}")
    remaining_budget = budget - total_spent
    print(f"✅ Budget Remaining: ${remaining_budget:.2f}")

    # Get the current date
    current_date = datetime.date.today()

    # Calculate the last day of the current month
    last_day_of_month = datetime.date(current_date.year, current_date.month, 1) + datetime.timedelta(days=32)
    last_day_of_month = last_day_of_month.replace(day=1) - datetime.timedelta(days=1)

    # Calculate the number of remaining days in the month
    remaining_days = (last_day_of_month - current_date).days

    # Calculate daily budget to stay within budget
    daily_budget = remaining_budget / remaining_days

    print(f"Budget Per Day to stay in budget: ${daily_budget:.2f}")

# Entry point of the script
if __name__ == "__main__":
    main()
