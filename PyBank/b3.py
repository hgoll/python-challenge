import os
import csv

#csvpath = os.path.join('PyBank1.csv')
##STEP ONE:

csvpath = os.path.join('PyBank1.csv')


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    count = 1
    total_amount = 0
    average_change = 0
    total_profits = 0 
    total_losses = 0
    csv_firstrow = next(csvreader)
    pre_amount = int(csv_firstrow[1])
    change_amounts = []

    #num_rows = 1

        
    for row in csvreader:
        #num_rows += 1
        count = (count +1)
        total_amount = (total_amount + int(row[1]))
        #average_change = total_amount/count
        change_amounts.append(int(row[1]) - pre_amount)
        pre_amount = int(row[1])
        average_change = sum(change_amounts)/count
        #greatest_increase = max(change_amounts)
        #greatest_increase_day =
        #greatest_decrease = min(change_amounts)

        if int(row[1]) > 0:
            total_profits = total_profits + int(row[1])
        if int(row[1]) < 0:
            total_losses = total_losses + int(row[1])
        #greatest_increase =
        #greatest_decrease =
    #print(num_rows)
    print('Financial Analysis')
    print('------------------------------------------')    
    print (f'Total Months: {count}')
    print (f'Total: {total_amount}')
    print (f'Average Change: {average_change}')
    print (f'Greatest Increase in Profits: {total_profits}')
    print (f'Greatest Decrease in Profits: {total_losses}')

#Step Two
indexes = [1,2,3,4,5]
titles = ["Total Months", "Total", "Average Change",
"Greatest Increase in Profits", "Greatest Decrease in Profits"]
values = ["86", "$37514694", "$-2288.19", "$4482120", "$-7327426"]
roster = zip(indexes, titles, values) 
output_file = os.path.join('Bank Data2.csv')
with open(output_file, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Index", "Title", "Value"])
    writer.writerows(roster)





#type(row)





   
    

#Initialize array     
    #arr = [[1,2]];     
    #sum = 0;    
     
#Loop through the array to calculate sum of elements  
#for i in range(2, len(arr)):    
   #sum = sum + arr[i];    
     
#print("Total: " + str(sum));
    
    
    #for row in csvreader:
     #   profits.append(row[1])
      #  dates.append(row[0])
    
   # print(profits)
    #print(dates)

