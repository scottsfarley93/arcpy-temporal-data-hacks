import csv
import pandas
f = open("F://Refugee_Analysis/timeseries/Tumblr_Cities_TS.csv", 'r')
lines = []
csvreader = csv.reader(f)
cursor = 0
for i in csvreader:
	if cursor ==0 :
		header = i
	else:
		lines.append(i)
	cursor += 1
data = []
i = 0
print "Number of columns is: ", len(header)
while i < len(header):
	j = 0
	while j < len(lines):
		thisdate = lines[j]
		if len(thisdate) != len(header):
			print "Line lengths not equal. Aborting. "
			print "Expected ", len(header), "but got", len(thisdate)
			exit()
		date = thisdate[0]
		gpe = header[i]
		value = thisdate[i]
		newrow = [gpe, date, value]
		data.append(newrow)
		j +=1
	print "Iteration: ", i
	i +=1
	
data= pandas.DataFrame(data, columns=["Entity", "Date", "Value"])
data.to_csv("F://Refugee_Analysis/Temporalized_Timeseries/Tumblr_new_Cities.csv")
print "Job Complete"