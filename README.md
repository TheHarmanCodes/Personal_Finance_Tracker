---
# Personal Finance Tracker

A Python-based personal finance tracking tool that allows users to manage their financial transactions effectively. With features to log transactions, view summaries, and visualize income and expenses over time, this project serves as a practical demonstration of Python's capabilities in file handling, data manipulation, and plotting.
---

## Features

- **Add Transactions**: Record income or expense transactions with details such as date, amount, category, and description.
- **View Transaction History**: Retrieve and view transactions within a specific date range.
- **Summary Generation**: Calculate total income, expenses, and net savings over a selected period.
- **Data Visualization**: Generate a visual plot of income and expenses over time.
- **CSV File Storage**: All transactions are stored in a CSV file for easy data handling and persistence.
- **Customizable Categories**: Transactions can be categorized for better organization.

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Virtual environment (recommended)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/TheHarmanCodes/Personal_Finance_Tracker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Personal_Finance_Tracker
   ```
3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Linux/Mac
   .venv\Scripts\activate     # For Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the main Python file:
   ```bash
   python main.py
   ```
2. Choose from the available options:

   - **Add a new transaction**
   - **View transactions within a date range**
   - **Exit the program**

3. If viewing transactions, you will have the option to visualize income and expenses through a plotted graph.

---

## File Structure

- `main.py`: The main entry point of the application.
- `data_entry.py`: Contains helper functions for collecting user input.
- `finance_data.csv`: Stores transaction records in CSV format (auto-created if it doesn't exist).
- `.gitignore`: Ensures unnecessary files like virtual environments and editor-specific configurations are not tracked.

---

## Demo

### Transaction Summary

Example output:

```
Transactions from 01-12-2024 to 25-12-2024:
    date       amount  category     description
01-12-2024    1000.00   Income       Salary
05-12-2024     500.00   Expense      Rent
10-12-2024     200.00   Expense      Groceries

Summary:
Total Income: $1000.00
Total Expense: $700.00
Net Savings: $300.00
```

### Visualization

Generates a line plot of income and expenses over time for quick insights.

---

## Contribution

Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation of your changes.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Python Libraries: `pandas`, `matplotlib`
- Inspired by real-world finance management needs.
