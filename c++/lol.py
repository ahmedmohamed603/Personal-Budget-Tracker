##################################### Personal Budget Tracker #####################################


#JSON Import
import json

# Totals variables
total_income = 0
total_expenses = 0

# Categories for income
income_categories = {
    "salary": 0,
    "freelance": 0,
    "other income": 0
}

# Categories for expenses
expense_categories = {
    "food": 0,
    "transport": 0,
    "groceries": 0,
    "rent": 0,
    "other expense": 0
}

# Authentication
users = {
    "Ahmed": "3266",
    "user": "0000"
}
current_role = None  # none variable without value
current_user = ""

# laod data from json if available / if not starting from zero
def load_user_data(username):
    global total_income, total_expenses, income_categories, expense_categories
    try:
        with open(f"{username}_data.json", "r") as file:
            data = json.load(file)
            total_income = data["total_income"]
            total_expenses = data["total_expenses"]
            income_categories = data["income_categories"]
            expense_categories = data["expense_categories"]
            print(f"Data loaded for {username} \n")
    except FileNotFoundError:
        print(f"No data found for {username}. Starting from zero.\n")

# Save user data
def save_user_data():
    with open(f"{current_user}_data.json", "w") as file:
        json.dump({
            "total_income": total_income,
            "total_expenses": total_expenses,
            "income_categories": income_categories,
            "expense_categories": expense_categories
        }, file)

# Authentication function
def authenticate():
    global current_role, current_user
    print("Welcome to Personal Budget Tracker")
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Checking if user and password are right
        if username in users and users[username] == password:
            current_user = username

            # Checking if User or Admin 
            current_role = "admin" if username == "Ahmed" else "user"
            print(f"Login successful! Role: {current_role}\n")
            load_user_data(username)
            return
        else:
            print("Invalid credentials. Try again.\n")

# Reset all data
def reset_data():
    global total_income, total_expenses, income_categories, expense_categories
    total_income = 0
    total_expenses = 0
    for key in income_categories:
        income_categories[key] = 0
    for key in expense_categories:
        expense_categories[key] = 0
    print("All data has been reset!\n")

# Add income
def add_income():
    global total_income
    print("Income Categories: ", ", ".join(income_categories.keys()))
    category = input("Enter category: ").lower()
    while True:
        try:
            amount = float(input("Enter income amount: "))
            if category in income_categories:
                income_categories[category] += amount
            else:
                print("Invalid category! Adding to 'other'.")
                income_categories["other income"] += amount
            total_income = sum(income_categories.values())
            print("Income added!\n")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

# Add expense
def add_expense():
    global total_expenses
    print("Expense Categories: ", ", ".join(expense_categories.keys()))
    category = input("Enter category: ").lower()
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            if category in expense_categories:
                expense_categories[category] += amount
            else:
                print("Invalid category! Adding to 'other'.")
                expense_categories["other expense"] += amount
            total_expenses = sum(expense_categories.values())
            print("Expense added!\n")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

# View summary
def view_summary():
    balance = total_income - total_expenses
    print("\nSummary:")
    print(f"Total Income: {total_income}")
    print("Income by Category:")
    for key, value in income_categories.items():
        print(f"  {key}: {value}")
    print(f"Total Expenses: {total_expenses}")
    print("Expenses by Category:")
    for key, value in expense_categories.items():
        print(f"  {key}: {value}")
    print(f"Remaining Balance: {balance}\n")

# Search by category
def search_category():
    category = input("Enter category to search: ").lower()
    if category in income_categories:
        print(f"Income in '{category}': {income_categories[category]}")
    elif category in expense_categories:
        print(f"Expenses in '{category}': {expense_categories[category]}")
    else:
        print("Category not found.\n")

# Edit category
def edit_category():
    print("1. Edit Income Category\n2. Edit Expense Category")
    choice = input("Choose an option (1 or 2): ")
    if choice == "1":
        category = input("Enter income category to edit: ").lower()
        if category in income_categories:
            try:
                new_value = float(input(f"Enter new value for '{category}': "))
                income_categories[category] = new_value
                global total_income
                total_income = sum(income_categories.values())
                print("Income category updated!\n")
            except ValueError:
                print("Invalid value.\n")
        else:
            print("Category not found.\n")
    elif choice == "2":
        category = input("Enter expense category to edit: ").lower()
        if category in expense_categories:
            try:
                new_value = float(input(f"Enter new value for '{category}': "))
                expense_categories[category] = new_value
                global total_expenses
                total_expenses = sum(expense_categories.values())
                print("Expense category updated!\n")
            except ValueError:
                print("Invalid value.\n")
        else:
            print("Category not found.\n")
    else:
        print("Invalid option.\n")

# Delete category
def delete_category():
    print("1. Delete Income Category\n2. Delete Expense Category")
    choice = input("Choose an option (1 or 2): ")
    if choice == "1":
        category = input("Enter income category to delete: ").lower()
        if category in income_categories and category != "other income":
            del income_categories[category]
            global total_income
            total_income = sum(income_categories.values())
            print("Income category deleted.\n")
        else:
            print("Cannot delete or category not found.\n")
    elif choice == "2":
        category = input("Enter expense category to delete: ").lower()
        if category in expense_categories and category != "other expense":
            del expense_categories[category]
            global total_expenses
            total_expenses = sum(expense_categories.values())
            print("Expense category deleted.\n")
        else:
            print("Cannot delete or category not found.\n")
    else:
        print("Invalid option.\n")

# view user data  "FOR ADMIN ONLY"
def view_user_file():
    if current_role != "admin":
        print("Access denied.\n")
        return
    username = input("Enter username to view data: ")
    try:
        with open(f"{username}_data.json", "r") as file:
            data = json.load(file)
            print(f"\nSummary for {username}:")
            print(f"Total Income: {data['total_income']}")
            print("Income by Category:")
            for key, value in data["income_categories"].items():
                print(f"  {key}: {value}")
            print(f"Total Expenses: {data['total_expenses']}")
            print("Expenses by Category:")
            for key, value in data["expense_categories"].items():
                print(f"  {key}: {value}")
            print(f"Remaining Balance: {data['total_income'] - data['total_expenses']}\n")
    except FileNotFoundError:
        print("User file not found.\n")

# Main Menu
def main_menu():
    while True:
        print("1. Add Income\n2. Add Expense\n3. View Summary\n4. Search Category\n5. Reset Data (Admin Only)")
        print("6. Edit Category\n7. Delete Category\n8. View User File (Admin Only)\n9. Exit")
        choice = input("Choose an option (1-9): ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            search_category()
        elif choice == "5" and current_role == "admin":
            reset_data()
        elif choice == "6":
            edit_category()
        elif choice == "7":
            delete_category()
        elif choice == "8" and current_role == "admin":
            view_user_file()
        elif choice == "9":
            save_user_data()
            print("Data saved! Goodbye!")
            break
        else:
            print("Invalid choice or restricted access.\n")

# Run the program
authenticate()
main_menu()
