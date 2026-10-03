import json
import os
from datetime import date


file_name = "expenses.json"

def loading_expenses():
    if not os.path.exists(file_name):
        return []
    else:
        with open(file_name, "r") as file:
            return json.load(file)



def saving_expenses(expenses):
    with open(file_name, "w") as file:
        json.dump(expenses, file, indent=2)

def adding_expense(expenses):
    money_ammount= float(input("Enter Ammount: "))
    category = input("Enter Category: ")
    description = input("Enter Description: ")

    expense = {
        "amount": money_ammount,
        "category": category ,
        "description": description,
        "date": str(date.today()),
    }

    expenses.append(expense)
    saving_expenses(expenses)
    print("Your Expense has been added!")


def showing_expenses(expenses):
    if len(expenses) == 0:
        print("There is no expenses yet!")
        return
    for expense in expenses:
        print(expense["date"] + " | " + expense["category"] + " | " + str(expense["amount"]) + " | " + expense["description"])








def main():
    expenses = loading_expenses()
    while True:
        print("\n1. Add your expense   2. List your expenses    3. Quit")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            adding_expense(expenses)
        elif user_choice == "2":
            showing_expenses(expenses)
        elif user_choice == "3":
            break

        else:
            print("Invalid choice")



if __name__ == "__main__":
    main()

