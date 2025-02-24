# python-challenge

## Overview

This project consists of two Python scripts that analyze financial and election data using CSV files. The scripts automate the process of reading the data, performing calculations, and generating summary reports.

## Project Structure
```
Project Repository
│── PyBank/
│   │── Resources/
│   │   ├── budget_data.csv
│   │── analysis/
│   │   ├── budget_analysis.txt
│   ├── main.py
│── PyPoll/
│   │── Resources/
│   │   ├── election_data.csv
│   │── analysis/
│   │   ├── election_results.txt
│   │── main.py
│── README.md
```

## PyBank - Financial Data Analysis
### Description
The `PyBank` script analyzes financial records stored in the corresponding `Resources` directory in a `csv` file format and provides key financial metrics. The `csv` file input should be is arranged into 2 columns: "Date" and "Profit/Losses", respectively.

### Functionality
- Calculates the total number of months recorded.
- Computes the net total of "Profit/Losses" across entire csv file.
- Determines the average change in "Profits/Losses" values.
- Identifies the greatest increase and decrease in "Profits/Losses" column along with their corresponding dates.

### Sample Output
```
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```

## PyPoll - Election Data Analysis
### Description
The `PyPoll` script processes election data stored in the corresponding `Resources` directory in a `csv` file and determines the election results. The `csv` file input should be formatted into 3 columns: "Voter ID", "County", and "Candidate", in that order.

### Functionality
- Counts the total number of votes cast.
- Identifies each candidate who received votes.
- Calculates the percentage and total votes for each candidate.
- Determines the winner based on the highest number of votes won by each candidate.

### Sample Output
```
Election Results
-------------------------
Total Votes: 369711
-------------------------
Jane Doe: 26.056% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
```

## Usage
1. Place a `csv` file inside the corresponding `Resources/` folder.
2. Run the Python scripts located in the `PyPoll` or `PyBank` directories using:
   ```sh
   python main.py
   ```
3. The analysis results will be saved inside the `analysis/` folder, within the `PyPoll` directory, as text files.

## Dependencies
- Python 3.0.0+
- CSV module
- OS module

## Author
This project was created for educational purposes to demonstrate basic Python data analysis techniques pertaining to `csv` files.

