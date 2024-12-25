from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}


def get_date(prompt, allow_default=True):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)  # formating today date
    try:
        # cleans up the date that user type in
        valid_date = datetime.strptime(date_str, date_format)
        # give to the user in format that we need
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yyyy format.")


def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense):").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    print("Invalid category. Enter the category ('I' for Income or 'E' for Expense):")
    return get_category()


def get_description():
    return input("Enter a description (optional):")


# date = get_date(
#     "Enter a date (dd-mm-yyyy) or press Enter for today's date: ", allow_default=True
# )
# print("Validated Date:", date)
