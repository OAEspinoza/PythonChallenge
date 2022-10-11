# Import modules
import os
import csv             

# Specifies the file to write to
csvpath=os.path.join("Resources","election_data.csv")

# Function to find unique values in a list
def uniquelist(list):
    unique_list=[]
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print(x)

names=[] # Creates list with candidates' names of all ballots

# initalize counters
total_votes_counter=0

# Open the CSV
with open(csvpath,newline="") as csvfile:
    # Set path for file
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader)
    for line in csvreader:
        total_votes_counter+=1
        names.append(line[2]) #adds candidates names to the list

# Print results
print("Total votes cast: "+str(total_votes_counter))
print("Candidates with votes: ")
uniquelist(names)