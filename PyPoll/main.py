import os
import csv
election_csv = os.path.join("Resources","election_data.csv")
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csvheader=next(csvfile)
    votes = len(next(zip(*csvreader)))
    

    print(f"Election Results \n Total Votes: {votes} \n Khan:   \n Correy:    \n Li:   \n O'Tooley:    \n Winner:    ")

