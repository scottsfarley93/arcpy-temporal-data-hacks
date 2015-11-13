import csv
import pandas 
print "Imports Successful."
csvFiles = ["C://Users/student/documents/all_tweets.csv", "C://Users/student/downloads/tweetsOut1/tweetsOut1.csv"]
outputCSV = "C://Users/student/documents/all_tweets1.csv"

bigMatrix = []
fields = ""


for filename in csvFiles:
    f = open(filename, 'rU')
    csvreader = csv.reader(f)
    numHeaders = 2
    headerCounter = 0
    try:
        for row in csvreader:
            if headerCounter < numHeaders:
                headerCounter += 1
            else:
                bigMatrix.append(row)
        print "Completed: ", filename
    except Exception as e:
        print "Skipped file", filename, "because", str(e)
print "Now Saving..."
bigDataframe = pandas.DataFrame(bigMatrix)
bigDataframe.to_csv(outputCSV)
