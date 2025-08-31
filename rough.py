import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__)) 
file_path = os.path.join(script_dir, "expenses.csv")

with open(file_path, "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    categories = [] 
    amounts = []
    for line in csv_reader:
        if len(line) > 3:
            categories.append(line[0])
            amounts.append(line[2])
    
    print(categories, amounts)

    # unique_categories = list(dict.fromkeys(categories))
    # other_list = []
    # other_list2 = set()
    # new_amounts_list = []
    
    # for index1, i in enumerate(categories):
    #     for index2, j in enumerate(categories):
    #         if i == j and index2 not in other_list:
    #             print(f"i = {index1} , j = {index2} , {i}")
    #             other_list.append(index2)
    #             other_list2.add(index1)
    #             if index1 not in other_list2:
    #                 new_amounts_list.append(amounts[index2])
    #             elif index1 in other_list2:
    #                 new_amounts_list[index1] += amounts[index2] 
    #         else:
    #             continue
    # print(other_list)
    # print(unique_categories)
    # print(new_amounts_list)
    category_sums = {}
    categories2 = zip(categories,amounts)
    print(categories2)

    for cat, amt in zip(categories, amounts):
        amt = float(amt)  # convert to number if needed
        if cat in category_sums:
            category_sums[cat] += amt
        else:
            category_sums[cat] = amt

    print(category_sums)
