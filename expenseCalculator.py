from Expernse import expense


def main():
    #print("Welcome to Expense Calculator.")
    expense_file_path = "expense.csv"
    #final_expense = user_expense()
    #print(final_expense)

    #save_expense_to_file(final_expense, expense_file_path)

    summarize_expenses(expense_file_path)

def user_expense():
    spender_name = input("Please enter your name: ")
    spender_expense = float(input("Please enter you expense. "))

    categories_list = [
        "Rent / Mortgage",
        "Food",
        "Medical Expense",
        "Miscellaneous"
    ]

    #print(categories_list)
    
    while True:
        print("Select a category.")
        for i, category_name in enumerate(categories_list):
            print(f"{i + 1}. {category_name}")

        category_number = int(input("\nPlease select a number from 1 - 4.\n"))

        if(category_number > 4 or category_number < 0 or type(category_number) != int):
            print("Invalid input. Please try again.")
        
        else:
             if (category_number == 1):
                category = categories_list[0]

             if (category_number == 2):
                category = categories_list[1]
            
             if (category_number == 3):
                category = categories_list[2]

             if (category_number == 4):
                category = categories_list[3]

             new_expense = expense(
                name = spender_name, amount = spender_expense, category = category
            )
             return new_expense

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

            if(len(splitted_list) >= 3):
                expense_name = splitted_list[0]
                expense_amount = splitted_list[1]
                expense_category = splitted_list[2]
                line_expense = expense(
                    name = expense_name,
                    amount = float(expense_amount),
                    category = expense_category
                )            
                print(line_expense)
            else:
                print("Invalid!!!")



if __name__ == "__main__":
    main()
