import os
import csv
budget_csv = os.path.join("Resources","budget_data.csv")
months=1
profitlist=[]
monthlist=[]
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csvheader=next(csvfile)
    firstrow=next(csvreader)
    total=int(firstrow[1])
    for row in csvreader:
        months += 1
        total += int(row[1])
        profitlist.append(int(row[1]))
        monthlist.append(str(row[0]))
    v = [profitlist[i+1]-profitlist[i] for i in range(len(profitlist)-1)]
    increase=max(v)
    decrease=min(v)
    average_change = 0
x=v.index(min(v))
y=v.index(max(v))
g=monthlist[x+1]
h=monthlist[y+1]

print(f"Financial Analysis \n Total Months: {months} \n Total: ${total} \n Average Change: {average_change} \n Greatest Increase in Profits: {g} ({increase}) \n Greatest Decrease in Profits: {h} ({decrease}) ")

    
        

    

       
            


