import csv
import os
import pandas as pd

# Load the dataset
file_path = "PyBank\Resources\budget_data.csv"
df = pd.read_csv(file_path)

# Display the first few rows to understand the structure
df.head()

# Calculate the total number of months
total_months = df.shape[0]

# Calculate the net total amount of "Profit/Losses"
net_total = df["Profit/Losses"].sum()

# Calculate the changes in "Profit/Losses" over the entire period
df["Change"] = df["Profit/Losses"].diff()

# Calculate the average change (excluding the first NaN value)
average_change = df["Change"].mean()

# Find the greatest increase in profits (maximum change)
greatest_increase = df.loc[df["Change"].idxmax(), ["Date", "Change"]]

# Find the greatest decrease in profits (minimum change)
greatest_decrease = df.loc[df["Change"].idxmin(), ["Date", "Change"]]

# Prepare the results
financial_analysis = f"""\
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase['Date']} (${int(greatest_increase['Change'])})
Greatest Decrease in Profits: {greatest_decrease['Date']} (${int(greatest_decrease['Change'])})
"""

# Print the results
print(financial_analysis)

# Save the output to a text file
output_path = "PyBank\analysis\financial_analysis.txt"
with open(output_path, "w") as file:
    file.write(financial_analysis)
