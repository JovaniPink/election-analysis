# -*- coding: utf-8 -*-

# TODO:
# The data we need to retrive.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("resources", "election_results.csv")
# Create a filename variable to a direct or indirect of indirect path to the file.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#Open the election results and read the file
with open(file_to_load) as election_data:
    # TODO:
    # Read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    print(type(file_reader))
    # for row in file_reader:
    #     print(row)
    headers = next(file_reader)
    print(headers)

# # Using the with statement open the file as a text file.
# with open(file_to_save, 'w') as txt_file:
#     # Write three countines to the file.
#     txt_file.write("Arapahoe", "Denver","Jefferson")

# # Import the datetime class from the datetime module.
# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print out the type of now
# print(type(now))
# # Print out the present time.
# print("The time right now is ", now)
