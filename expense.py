import csv
import matplotlib.pyplot as plt
import os
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__)) 
file_path = os.path.join(script_dir, "expenses.csv")

choice = input("Do you want to add an expense Y/N: ")

if choice.lower() == "y":
    while True:
        print("TRACK YOUR EXPENSES")

        expense_category = input("Enter category: ")
        expense_information = input("Add other information: ")

        while True:
            try:
                expense_date = input("Enter the date (dd-mm-yyyy): ")
                date_str = datetime.strptime(expense_date, "%d-%m-%Y")
                break
            except:
                print("Not a valid entry for date")
        expense_amount = float(input("Enter amount: "))

        fieldrows = [expense_category.capitalize(), expense_date, expense_amount, expense_information]

        if os.path.exists(file_path):
            with open(file_path, "a", newline="") as csvfile:     
                writer = csv.writer(csvfile)
                writer.writerow(fieldrows)

        else:
            with open(file_path, "w") as csvfile:
                fieldnames = ["Category", "Date", "Amount", "Other info"]
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow(fieldnames)
            with open(file_path, "a", newline="") as csvfile:     
                writer = csv.writer(csvfile)
                writer.writerow(fieldrows)

        repeat_choice = input("Do you want to add another item Y/N: ")
        if repeat_choice.lower() == "n":
            break

elif choice.lower() == "n":
    print("No expense added")

with open(file_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    categories = list()
    amounts = list()
    for line in csv_reader:
        if len(line) > 3:
            categories.append(line[0])
            amounts.append(float(line[2]))
    
    category_sums = {}
    for cat, amt in zip(categories, amounts):
        category_sums[cat] = category_sums.get(cat, 0) + amt

    print(category_sums.keys())

    plt.pie(category_sums.values(), labels = category_sums.keys(), autopct = lambda pct: f"{int(round(pct/100.*sum(category_sums.values())))}PKR")
    plt.title("Expenses")
    plt.show()
    

