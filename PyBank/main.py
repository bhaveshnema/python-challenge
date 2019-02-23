# Import OS, CSV, and locale module
import os
import csv
import locale

# Define Lists
total_months = []
total_dollars = []
monthly_profit_change = []

# Set the locale module for Total Profit to get number in dollars
locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8' )

# Set the CSV Path
pybank_csv = os.path.join("../" "Resources", "budget_data.csv")

# Open the CSV with comma as a delimiter
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)

    # Read through the CSV
    for row in csv_reader:
        # Append the total months and total profit in the lists
        total_months.append(row[0])
        total_dollars.append(int(row[1]))

    # Iterate through the profitsto get the monthly change in profits
    for i in range(len(total_dollars) - 1):

    # Take the difference between two months and append to monthly profit change
         monthly_profit_change.append(total_dollars[i + 1] - total_dollars[i])

# Calculate the max and min of the the monthly profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Correlate max and min to the proper month using month list and index from max and min
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1



#Print Statements

print("Financial Analysis\n" "------------------------")
print(f"Total Months: {len(total_months)}")
print("Total: " + locale.currency(sum(total_dollars)))
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")


# Output files
with open('financial_analysis.txt', 'w') as text:

    # Write methods to print to Financial Analysis
    text.write("Financial Analysis\n" "------------------------")
    text.write("\n")
    text.write(f"Total Months: {len(total_months)}")
    text.write("\n")
    text.write(f"Total: ${sum(total_dollars)}")
    text.write("\n")
    text.write(f"Average Change: {round(sum(monthly_profit_change) / len(monthly_profit_change), 2)}")
    text.write("\n")
    text.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    text.write("\n")
    text.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

