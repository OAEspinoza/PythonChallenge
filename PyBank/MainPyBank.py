# Import modules
import os
import csv

# Specifies the file to write to
csvpath=os.path.join("Resources","budget_data.csv")

# initalize counters
month_counter=0
net_total=0
total_changes=0
values=[] #creates list to store profit and loss values
dates=[] #creates list to store dates in a list
max_increase=0
max_decrease=0

# Open the CSV
with open(csvpath,newline="") as csvfile:
    # Set path for file
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader)
    for line in csvreader:
        month_counter+=1
        net_total+=int(line[1])
        values.append(line[1]) #adds profit/loss to "values" list
        dates.append(line[0]) #adds date to "dates" list
for i in range(1,month_counter):
    change=float(values[i])-float(values[i-1])
    total_changes=total_changes+(change)
    if change <0:
        if change<max_decrease:
            max_decrease=change
            max_decrease_date=i
    if change>0:
        if change>max_increase:
            max_increase=change
            max_increase_date=i
        
# Format results
net_total=f'{net_total:,.2f}'
average_changes=f'{total_changes/(month_counter-1):,.2f}'
max_increase=f'{max_increase:,.2f}'
max_decrease=f'{max_decrease:,.2f}'

# Print results to terminal
print("Total months: "+str(month_counter))
print("Notal net profit/loss: $"+str(net_total))
print("Average change: $"+str(average_changes))
print("Greatest increase in profits: "+str(dates[max_increase_date])+" $"+str(max_increase))
print("Greatest decrease in profits: "+str(dates[max_decrease_date])+" $"+str(max_decrease))

# Exports results to a txt file
f=open('PyBankResults.txt','w')
f.write("Total months: "+str(month_counter))
f.write("\n")
f.write("Notal net profit/loss: $"+str(net_total))
f.write("\n")
f.write("Average change: $"+str(average_changes))
f.write("\n")
f.write("Greatest increase in profits: "+str(dates[max_increase_date])+" $"+str(max_increase))       
f.write("\n")
f.write("Greatest decrease in profits: "+str(dates[max_decrease_date])+" $"+str(max_decrease))
f.close()
