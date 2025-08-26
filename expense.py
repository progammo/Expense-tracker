import csv
import os
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))  # folder of the script
file_path = os.path.join(script_dir, "expenses.csv")

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

fieldrows = [expense_category, expense_date, expense_amount]

if os.path.exists(file_path):
    with open(file_path, "a", newline="") as csvfile:     
        writer = csv.writer(csvfile)
        writer.writerow(fieldrows)

else:
    with open(file_path, "w") as csvfile:
        fieldnames = ["Category", "Date", "Amount"]
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fieldnames)
    with open(file_path, "a", newline="") as csvfile:     
        writer = csv.writer(csvfile)
        writer.writerow(fieldrows)
