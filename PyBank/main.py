import os
import csv
budget_csv = os.path.join("Resources","budget_data.csv")
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csvheader=next(csvfile)
    months = len(next(zip(*csvreader)))
    net = 0
    for row in csvreader:
        net += float(row[1])
    average_change = 0
    increase = 0
    decrease = 0
    print(f"Financial Analysis \n Total Months: {months} \n Total: ${net} \n Average Change: {average_change} \n Greatest Increase in Profits: {increase} \n Greatest Decrease in Profits: {decrease} ")

    
        

    

       
            


