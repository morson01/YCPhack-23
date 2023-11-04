def main():
    print("Welcome to Expense Calculator.")

    # Input for user's name
    spender_name = input("Please enter your name: ")

    # Input for user's salary
    salary = float(input("Please enter your salary: "))

    # Input for user's expenses
    final_expense = user_expense()

    # Input for transportation costs
    transportation_cost = float(input("Please enter your transportation costs: "))

    # Input for housing fees
    housing_fees = float(input("Please enter your housing fees: "))

    # Calculate total expenses
    total_expenses = final_expense.amount + transportation_cost + housing_fees

    print("Total Expenses: $", total_expenses)

    # Check if expenses are too high compared to salary
    if total_expenses > salary:
        print("Your expenses are too high. Consider reducing spending.")
    else:
        print("Your expenses are within your budget.")

    save_expense_to_file(final_expense, "expense.csv")

    summarize_expenses("expense.csv")


def user_expense():
    categories_list = [
        "Rent / Mortgage",
        "Food",
        "Medical Expense",
        "Miscellaneous"
    ]

    while True:
        print("Select a category.")
        for i, category_name in enumerate(categories_list):
            print(f"{i + 1}. {category_name}")

        category_number = int(input("\nPlease select a number from 1 - 4.\n"))

        if (category_number > 4 or category_number < 0 or type(category_number) != int):
            print("Invalid input. Please try again.")
        else:
            category = categories_list[category_number - 1]

            spender_expense = float(input(f"Please enter your {category} expense: "))

            new_expense = expense(
                name=spender_name, amount=spender_expense, category=category
            )
            return new_expense


# The rest of your code (save_expense_to_file and summarize_expenses) remains the same.

def save_expense_to_file(expense, expense_file_path):
    with open(expense_file_path, "a") as f:
        print("\n")
        f.write(f" \n{expense.name}, {expense.amount}, {expense.category} \n")


def summarize_expenses(expense_file_path):
    Expernse: list[expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            splitted_list = stripped_line.split(",")

            if (len(splitted_list) >= 3):
                expense_name = splitted_list[0]
                expense_amount = splitted_list[1]
                expense_category = splitted_list[2]
                line_expense = expense(
                    name=expense_name,
                    amount=float(expense_amount),
                    category=expense_category
                )
                print(line_expense)
            else:
                print("Invalid!!!")
                


if __name__ == "__main__":
    main()
