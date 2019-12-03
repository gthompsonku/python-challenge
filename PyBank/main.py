import os
import csv
from statistics import mean

csvpath = os.path.join("..", "/Users/Grant/UCSD Bootcamp/python-challenge/PyBank", "budget_data.csv")

months=[]
profits=[]
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))

#determine the change in profit month over month and store in list
monthly_change=[]

#starting at month 2 and comapre it to previous month 
i=1  
while i < (len(profits)):
    monthly_change.append(profits[i]-profits[i-1])
    i=i+1

# determine best and worst month over month change
best_month_index=monthly_change.index(max(monthly_change))
worst_month_index=monthly_change.index(min(monthly_change))

#print out results to terminal (as well as determine average monthly change)
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: {'${:,.2f}'.format(sum(profits))}")  
print(f"Average Change: {'${:,.2f}'.format(mean(monthly_change))}")
print(f"Greatest Increase in Profits: {months[best_month_index+1]} {'${:,.2f}'.format(monthly_change[best_month_index])}")
print(f"Greatest Decrease in Profits: {months[worst_month_index+1]} {'${:,.2f}'.format(monthly_change[worst_month_index])}")

#create new txt file with the results
output_file=os.path.join("..","/Users/Grant/UCSD Bootcamp/python-challenge/PyBank","budget_summary.txt")

with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------------\n")
    file.write(f"Total Months: {len(months)}\n")
    file.write(f"Total: {'${:,.2f}'.format(sum(profits))}\n")  
    file.write(f"Average Change: {'${:,.2f}'.format(mean(monthly_change))}\n")
    file.write(f"Greatest Increase in Profits: {months[best_month_index+1]} {'${:,.2f}'.format(monthly_change[best_month_index])}\n")
    file.write(f"Greatest Decrease in Profits: {months[worst_month_index+1]} {'${:,.2f}'.format(monthly_change[worst_month_index])}\n")

