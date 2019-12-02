
import os
import csv

csvpath=os.path.join("..","/Users/Grant/UCSD Bootcamp/python-challenge/PyPoll","election_data.csv")

votes=[]

with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csvheader=next(csvreader)
    
    for row in csvreader:
         votes.append(row[2])   
            
#iterate through list of canidates and find canidate names

canidates=[]

for vote in votes: 
    if vote not in canidates:
        canidates.append(vote)

#determine the winner
tally=0
for canidate in canidates:
    if votes.count(canidate) > tally:
        winner=canidate
        tally=votes.count(canidate)

#print output
print("Election Results\n")
print(f"Total Votes: {len(votes)}\n")

for vote in canidates:
    print(f"{vote}: {'{0:.3%}'.format(votes.count(vote)/len(votes))} ({votes.count(vote)})")

print(f"\nWinner: {winner}")

output_file=os.path.join("..","/Users/Grant/UCSD Bootcamp/python-challenge/PyPoll","election_summary.txt")

with open(output_file,"w") as file:
    file.write("Election Results\n\n")
    file.write(f"Total Votes: {len(votes)}\n\n")

    for vote in canidates:
        file.write(f"{vote}: {'{0:.3%}'.format(votes.count(vote)/len(votes))} ({votes.count(vote)})\n")

    file.write(f"\nWinner: {winner}")

