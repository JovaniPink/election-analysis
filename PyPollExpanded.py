# -*- coding: utf-8 -*-

# Added dependencies
import csv
import os

# Assign a variable for the file to load and the path.
# The return type is of string
file_to_load = os.path.join("resources", "election_results.csv")

print(type(file_to_load))
# # Initialize a total vote counter.
# total_votes = 0

# # Candidate Options and candidate votes
# candidate_options = []
# county_options = []
# candidate_votes = {}
# county_count = {}

# # Track the winning candidate, vote count, and percentage.
# winning_candidate = ""
# winning_count = 0
# winning_percentage = 0

# # county_counts_done = {
# #     "Denver": {"Jane": 5000, "Joe": 2000, "John": 3000},
# #     "Jefferson": {"Jane": 6000, "Joe": 7000, "John": 4000},
# #     "Washington": {"Jane": "4000", "Joe": "2000", "John": "3000"},
# # }

# # for x in county_counts:
# #     print(county_counts[x])

# #     for y in county_counts[x]:
# #         print(county_counts[x][y])

# # Open the election results and read the file
# with open(file_to_load) as election_data:
#     # Read and analyze the data here.
#     # Read the file object with the reader function.
#     file_reader = csv.reader(election_data)

#     # Read the headers row.
#     headers = next(file_reader)

#     # Print each row in the CSV file.
#     for row in file_reader:
#         # 2. Add to the total vote count.
#         total_votes += 1
#         # Print out county
#         county_name = row[1]
#         # Print the candidate name from each row.
#         candidate_name = row[2]

#         if county_name not in county_count:
#             # Start to build the dictionary
#             county_count[county_name] = county_name
#             # If the candidate does not match any existing candidate...
#             if candidate_name not in county_count[county_name]:
#                 # Add it to the list of candidates.
#                 candidate_options.append(candidate_name)
#                 # Begin tracking that candidate's vote count.
#                 candidate_votes[candidate_name] = 0
#                 # Start to build the dictionary's candidate count
#                 county_count[county_name] = candidate_name

#         # Add a vote to that candidates's count
#         candidate_votes[candidate_name] += total_votes
