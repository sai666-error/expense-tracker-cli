"""
Expense Tracker CLI
A simple command-line app using Python + CSV + datetime
"""

import csv
import os
from datetime import date

FILENAME = "expenses.csv"


def ensure_file_exists():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])


def add_expense():
    try:
        category = input("Enter category (e.g. Food, Travel, Bills): ")
        amount = float(input("Enter amount: "))
        note = input("Enter a short note: ")
        today = date.today().isoformat()

        with open(FILENAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([today, category, amount, note])

        print("Expense added successfully.\n")
    except ValueError:
        print("Error: Please enter a valid number for amount.\n")


def view_expenses():
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    if not rows:
        print("No expenses recorded yet.\n")
        return

    print("\n--- All Expenses ---")
    for row in rows:
        print(f"{row['Date']} | {row['Category']} | ₹{row['Amount']} | {row['Note']}")
    print()


def total_spend():
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        total = sum(float(row["Amount"]) for row in reader)

    print(f"Total spend so far: ₹{total:.2f}\n")


def spend_by_category():
    totals = {}
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cat = row["Category"]
            amt = float(row["Amount"])
            totals[cat] = totals.get(cat, 0) + amt

    if not totals:
        print("No expenses recorded yet.\n")
        return

    print("\n--- Spend by Category ---")
    for cat, amt in totals.items():
        print(f"{cat}: ₹{amt:.2f}")
    print()


def main():
    ensure_file_exists()

    while True:
        print("===== Expense Tracker CLI =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spend")
        print("4. View Spend by Category")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spend()
        elif choice == "4":
            spend_by_category()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()
