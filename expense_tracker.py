expenses = []

def menu():
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Filter Expenses")
    print("4. Calculate Total")
    print("5. Exit")
    

def add_expence():
    date = input("Enter the date DD-MM-YYYY: ")
    description = input("Descirbe the expense (description): ")
    category = input("What category was it(Food, Transpoir, Electronics etc.):")
    amount  = float (input("Enter the amount: "))
    expenses.append()