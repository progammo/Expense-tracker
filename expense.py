from datetime import datetime

print("TRACK YOUR EXPENSES")

expense_category = input("Enter category: ")
while True:
    try:
        expense_date = input("Enter the date (dd-mm-yyyy): ")
        date_str = datetime.strptime(expense_date, "%d-%m-%Y")
        break
    except:
        print("Not a valid entry for date")

expense_amount = float(input("Enter amount: "))