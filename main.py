import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_category, get_amount, get_description
import matplotlib.pyplot as plt


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        }
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
            print("Entry added Successfully.")

    @classmethod
    def get_transaction(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        # mask apply to every single row inside of dataframe and it's going to filter the different elements
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions fount int the given date range")
        else:
            print(
                f"Transaction from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}"
            )
            print(
                filtered_df.to_string(
                    index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}
                )
            )
            total_income = filtered_df[filtered_df["category"] == "Income"][
                "amount"
            ].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"][
                "amount"
            ].sum()
            print("\nSummary:")
            print(f"Totaal Income: ${total_income:.2f}")
            print(f"Total Expense: ${total_expense:.2f}")
            print(f"Net Savings: ${(total_income - total_expense):.2f}")

        return filtered_df


def add():
    CSV.initialize_csv()
    date = get_date(
        "Enter the date of the transaction (dd-mm-yyyy) or press Enter for today's date:"
    )
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


def plot_transactions(df):
    if df.empty:
        print("No transactions available to plot.")
        return

    # Ensure "date" is a datetime index
    if "date" not in df.columns or not pd.api.types.is_datetime64_any_dtype(df["date"]):
        print("Error: 'date' column is missing or not in datetime format.")
        return

    df.set_index("date", inplace=True)

    # Resample and handle missing categories
    income_df = (
        df[df["category"] == "Income"]
        .resample("D")["amount"]
        .sum()
        .reindex(df.index, fill_value=0)
    )
    expense_df = (
        df[df["category"] == "Expense"]
        .resample("D")["amount"]
        .sum()
        .reindex(df.index, fill_value=0)
    )

    if income_df.empty and expense_df.empty:
        print("No income or expense data to plot.")
        return

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(
        income_df.index,
        income_df,
        label="Income",
        color="green",
        marker="o",
        linewidth=2,
    )
    plt.plot(
        expense_df.index,
        expense_df,
        label="Expense",
        color="red",
        marker="x",
        linewidth=2,
    )

    # Shaded areas for trends
    plt.fill_between(
        income_df.index, income_df, color="green", alpha=0.1, label="Income Area"
    )
    plt.fill_between(
        expense_df.index, expense_df, color="red", alpha=0.1, label="Expense Area"
    )

    # Title and labels
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Amount", fontsize=12)
    plt.title("Income and Expense Over Time", fontsize=16)

    # Rotate x-axis ticks and format dates
    plt.xticks(rotation=45, fontsize=10)
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))  # Show fewer ticks

    # Grid and legend
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend(fontsize=10)

    plt.tight_layout()  # Adjust layout to fit everything nicely
    plt.show()


def main():
    while True:
        print("\n1. Add a new transaction: ")
        print("2. View transaction and summary within a date range: ")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transaction(start_date, end_date)
            if input("Do you want to see a plot? (y/n) ").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Existing...")
            break
        else:
            print("Invalid choice. Enter 1,2 or 3.")


if __name__ == "__main__":
    main()
