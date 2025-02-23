# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_input = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")  # Input file path 
file_to_output = os.path.join(os.path.dirname(__file__), "analysis", "budget_analysis.txt")  # Output file path

# Ensure the output directory exists
os.makedirs(os.path.dirname(file_to_output), exist_ok=True)

# Define variables to track the financial data
total_months = 0
total_net = 0
net_changes = []
dates = []

# Open and read the csv
with open(file_to_input, "r", encoding="utf-8") as budget_data:
    reader = csv.reader(budget_data)
    
    # Skip the header row
    header = next(reader)
    
    # Extract first row to initialize tracking
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_net = int(first_row[1])
    
    # Process each row of data
    for row in reader:
        # Track the total months and net amount
        total_months += 1
        total_net += int(row[1])
        
        # Calculate net change and store it
        net_change = int(row[1]) - previous_net
        net_changes.append(net_change)
        dates.append(row[0])
        previous_net = int(row[1])
    
# Calculate the average net change
average_change = sum(net_changes) / len(net_changes) if net_changes else 0

# Find greatest increase and decrease
if net_changes:
    greatest_increase = max(net_changes)
    greatest_decrease = min(net_changes)
    greatest_increase_date = dates[net_changes.index(greatest_increase)]
    greatest_decrease_date = dates[net_changes.index(greatest_decrease)]
else:
    greatest_increase = greatest_decrease = 0
    greatest_increase_date = greatest_decrease_date = "N/A"

# Generate the output summary
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})
"""

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
