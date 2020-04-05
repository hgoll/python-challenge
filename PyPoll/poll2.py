import os
import csv
from collections import Counter

csvpath = os.path.join('pypoll.csv')

voter = []
county = []
candidate = []
words= []
    
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    num_rows = -1
    for row in open("pypoll.csv"):
        num_rows += 1
    print("Election Results")
    print("********************")
    print("Total Votes: " + str(num_rows))
    print("********************")

    count = 0
    count_of_cand = 0
    candi = [rec[2] for rec in csvreader]
    result = candi.count('Khan')
    result2 = candi.count('Correy')
    result3 = candi.count('Li')
    result4 = candi.count("O'Tooley")
    resPercent = result/num_rows
    resPercent2 = result2/num_rows
    resPercent3 = result3/num_rows
    resPercent4 = result4/num_rows
    for row in csvreader:
        voter.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
        count = count +1   
    #print(voter)
    #print(county)
    #print(candidate)
    #print(count) 

    print("Khan: " + str(result))
    print(str(resPercent*100) + "%")
    print("--------------------")
    print ("Correy: " + str(result2))
    print(str(resPercent2*100) + "%")
    print("--------------------")
    print("Li: " + str(result3))
    print(str(resPercent3*100) + "%")
    print("--------------------")
    print("O'Tooley: " + str(result4))
    print(str(resPercent4*100) + "%")
    print("********************")
    print("Winner: Khan")
        
#outpath = os.path.join('write_pypollcsv.csv')

#with open(outpath, 'w') as csvfile:
    #writer = csv.writer(csvfile)
    #writer.writerow("Candidate", "Votes", "Percent")


indexes =[1, 2, 3, 4]
titles = ["Khan", "Correy", "Li", "O'Tooley"]
values = ["63.09%", "19.94%", "13.96%", "3.01"]
roster = zip(indexes, titles, values)

output_file = os.path.join('Poll_Write.csv')
with open(output_file, "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Index", "Title", "Value"])
    writer.writerows(roster)


