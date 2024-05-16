'''PyBank challenge
- Need to find total number of months in data set
- Net total amount of Profit/Losses over the entire period
- Changes in Profit/Losses over the entire period and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greates decrease in profits (date and amount) over the entire period'''

import csv

# Define the path to your CSV file
csv_file_path = os.path.join('Resources', 'budget_data.csv')

# Initialize counters and lists
total_months = 0
total_profit_losses = 0
previous_profit_losses = None
monthly_changes = []
months = []

# Open and read the CSV file
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file, delimiter=',')
    
    # Skip the header row
    next(csv_reader)
    
    # Iterate over the rows in the CSV file
    for row in csv_reader:
        # Extract current month's date and profit/losses
        current_date = row[0]
        current_profit_losses = int(row[1])
        
        # Increment total months counter
        total_months += 1
        
        # Sum the Profit/Losses values
        total_profit_losses += current_profit_losses
        
        # Calculate the monthly change if not the first row
        if previous_profit_losses is not None:
            monthly_change = current_profit_losses - previous_profit_losses
            monthly_changes.append(monthly_change)
            months.append(current_date)
        
        # Update previous profit/losses for next iteration
        previous_profit_losses = current_profit_losses

# Calculate the average change in Profit/Losses
average_change = sum(monthly_changes) / len(monthly_changes)

# Find the maximum and minimum changes
max_change = max(monthly_changes)
min_change = min(monthly_changes)

# Find the corresponding months for max and min changes
max_change_month = months[monthly_changes.index(max_change)]
min_change_month = months[monthly_changes.index(min_change)]

print(f"Total number of months: {total_months}")
print(f"Total Profit/Losses: {total_profit_losses}")
print(f"Average Change in Profit/Losses: {average_change:.2f}")
print(f"Greatest Increase in Profits: {max_change_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_change_month} (${min_change})")

