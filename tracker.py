import json
import os

# file to store data
DATA_FILE = "data.json"

# load data if exists
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
else:
    data = {
        "income": [],
        "expense": []
    }

income_categories = ["Salary", "Pocket Money", "Freelance / Side Job", "Refund / Return", "Gift", "Others"]
expense_categories = ["Food", "Travel", "Shopping", "Skin care", "Online Orders", "Bills", "EMI / Recharge", "Entertainment", "Others"]

def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_income():
    print("\nIncome Categories:")
    for i, cat in enumerate(income_categories, start=1):
        print(f"{i}. {cat}")
    choice = int(input("Choose category number: "))
    category = income_categories[choice-1]

    amount = float(input("Enter amount: "))
    source = input("Enter source note: ")

    data["income"].append({"category": category, "amount": amount, "note": source})
    save_data()
    print("Income added successfully!")

def add_expense():
    print("\nExpense Categories:")
    for i, cat in enumerate(expense_categories, start=1):
        print(f"{i}. {cat}")
    choice = int(input("Choose category number: "))
    category = expense_categories[choice-1]

    amount = float(input("Enter amount: "))
    note = input("What did you spend on: ")

    data["expense"].append({"category": category, "amount": amount, "note": note})
    save_data()
    print("Expense added successfully!")

def view_summary():
    total_income = sum(i["amount"] for i in data["income"])
    total_expense = sum(e["amount"] for e in data["expense"])
    balance = total_income - total_expense

    print("\n--- SUMMARY ---")
    print("Total Income:", total_income)
    print("Total Expense:", total_expense)
    print("Balance:", balance)

while True:
    print("\n1. Add Income")
    print("2. Add Expense")
    print("3. Summary")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_income()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        view_summary()
    elif choice == "4":
        save_data()
        break
    else:
        print("Invalid Choice!")