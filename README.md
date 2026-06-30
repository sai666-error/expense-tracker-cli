# expense-tracker-cli
A command-line expense tracker built with Python — log expenses, view totals, and see spend by category, with data saved to CSV.
## What it does

This tool lets a user log daily expenses with category, amount, and a short note, and view summaries like total spend or spend broken down by category — all through a simple text-based menu.

## Features

- Add a new expense (category, amount, note, auto-dated)
- View all logged expenses
- View total spend across all entries
- View spend grouped by category
- Data persists between runs using a CSV file (`expenses.csv`)
- Basic input validation and error handling

## Tech Stack

- **Python** — core application logic
- **csv module** — reading and writing expense records to a CSV file
- **datetime module** — automatically records the date of each expense
- **Functions** — separate functions for adding, viewing, and summarizing expenses, keeping the code organized

## How to Run

1. Make sure Python 3 is installed:
   ```
   python --version
   ```
2. Clone this repository or download `expense_tracker_cli.py`.
3. Open a terminal in the project folder and run:
   ```
   python expense_tracker_cli.py
   ```
4. Use the on-screen menu (1–5) to add or view expenses.

## Example Menu

```
===== Expense Tracker CLI =====
1. Add Expense
2. View All Expenses
3. View Total Spend
4. View Spend by Category
5. Exit
```

## What I Learned

This project helped me understand how to persist data using CSV files without a database, structure a program using functions for separate responsibilities, and work with the `datetime` module to automatically timestamp records.

## Possible Improvements

- Add monthly/date-range filtering for expenses
- Add the ability to edit or delete a specific expense entry
- Migrate storage from CSV to SQLite for more robust data handling

