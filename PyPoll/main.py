'''Your task is to create a Python script that analyzes the votes and calculates each of the following values:
The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote'''

import csv
import os

# Define the path to your CSV file
csv_file_path = 'PyPoll/Resources/election_data.csv'
output_data_path = 'PyPoll/analysis/election_results.txt'

# Check if the output file already exists and delete it if it does
if os.path.exists(output_data_path):
    os.remove(output_data_path)
    
# Initialize counters and lists
total_votes = 0
candidate_votes = {}


# Open and read the CSV file
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file, delimiter=',')
    
     # Skip the header row
    next(csv_reader)
    
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
            

# Calculate percentages and find the winner
winner = None
max_votes = 0

results = []
results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")

for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {vote_percentage:.3f}% ({votes})")
    if votes > max_votes:
        max_votes = votes
        winner = candidate

results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")

# Print results to the screen
for line in results:
    print(line)

# Write results to a text file
with open(output_data_path, mode='w') as file:
    for line in results:
        file.write(line + '\n')

print(f"Election results have been written to {output_data_path}")