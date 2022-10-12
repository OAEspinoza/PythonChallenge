# Import modules
import os
import csv             

# Specifies the file to write to
csvpath=os.path.join("Resources","election_data.csv")

names=[] # Creates list with candidates' names of all ballots
votes=[] # Creates list with number of votes each candidate gets

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

# Find unique names
unique_list=[]
for x in names:
    if x not in unique_list:
        unique_list.append(x)

# Initializes values in the list containing the candidates' votes
for y in range(0,len(unique_list)):
    votes.append(0)

# Count votes per candidate
for i in range(0,len(unique_list)):
    for j in range(0,total_votes_counter):
        if names[j]==unique_list[i]:
            votes[i]+=1

# Determines who is the winner
winner=unique_list[0]
winner_votes=votes[0]
for i in range(1,len(unique_list)):
    if votes[i]>winner_votes:
        winner=unique_list[i]
        winner_votes=votes[i]

# Print to terminal
print("Election Results")
print("-------------------")
print("Total votes cast: "+f'{total_votes_counter:,}') # formats output with thousands separator, and no decimals
print("-------------------")
for i in range(0,len(unique_list)):
        print(unique_list[i]+": "+f'{votes[i]:,}'+" votes"+", "+f'{(votes[i]/total_votes_counter)*100:,.2f}'+"%")   # str(votes[i]/total_votes_counter)+"% of total votes cast")
print("-------------------")
print("The election winner is: "+winner+" with "+f'{winner_votes:,}'+" votes")

# Exports results to a txt file
f=open('PyPollResults.txt','w')
f.write("Election Results")
f.write("\n")
f.write("-------------------")
f.write("\n")
f.write("Total votes cast: "+f'{total_votes_counter:,}') # formats output with thousands separator, and no decimals
f.write("\n")
f.write("-------------------")
f.write("\n")
for i in range(0,len(unique_list)):
        f.write(unique_list[i]+": "+f'{votes[i]:,}'+" votes"+", "+f'{(votes[i]/total_votes_counter)*100:,.2f}'+"%")   # str(votes[i]/total_votes_counter)+"% of total votes cast")
        f.write("\n")
f.write("-------------------")
f.write("\n")
f.write("The election winner is: "+winner+" with "+f'{winner_votes:,}'+" votes")