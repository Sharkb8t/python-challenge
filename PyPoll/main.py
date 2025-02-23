# Import dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_input = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join(os.path.dirname(__file__), "analysis", "election_results.txt")  # Output file path

# Ensure the output directory exists
os.makedirs(os.path.dirname(file_to_output), exist_ok=True)

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidates = {}  # Dictionary to track candidate names and vote counts

# Open the CSV file and process it
with open(file_to_input) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        # Increment the total vote count
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates[candidate_name] = 0

        # Add a vote to the candidate's count
        candidates[candidate_name] += 1

# Determine the winner based on vote count
winning_candidate = max(candidates, key=candidates.get)

# Generate output summary
output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"
output += f"-------------------------\nWinner: {winning_candidate}\n-------------------------\n"

# Print the output to the terminal
print(output)

# Save the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
