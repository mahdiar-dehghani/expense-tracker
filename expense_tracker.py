import json
import os

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



def main():
    expenses = loading_expenses()
    print("Loaded " + str(len(expenses)) + " expenses.")

if __name__ == "__main__":
    main()

