# Import OS and CSV module
import os
import csv

# Set the CSV Path
pypoll_csv = os.path.join("../", "Resources", "election_data.csv")

# # Define Lists and variables
count = 0
candidate_list = []
unique_candidate = []
vote_count = []
vote_percent = []
final_str = ""

# Open the CSV using the set path pypoll csv

with open(pypoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Read through the CSV
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidate_list
        candidate_list.append(row[2])
        # Create a set from the candidate_list to get the unique candidate names
    for x in set(candidate_list):
        unique_candidate.append(x)

        # y is the total number of votes per candidate
        y = candidate_list.count(x)
        vote_count.append(y)

        # z is the percent of total votes per candidate
        z = (y / count) * 100
        vote_percent.append(z)


    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]


# Print to terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(count))
print("-------------------------")
for i in range(len(unique_candidate)):
    print(unique_candidate[i] + ": " + str(round(vote_percent[i])) + "% (" + str(vote_count[i]) + ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")



# Print to a text file: election_results.txt

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("-------------------------\n")
    for i in range(len(set(unique_candidate))):
        final_str = str(unique_candidate[i] + ": " + str(round(vote_percent[i])) + "% (" + str(vote_count[i]) + ")")
        text.write(final_str)
        text.write("\n")
    text.write("-------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("-------------------------")
