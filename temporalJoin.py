import arcpy 
import csv
import arcpy.da
print "Imports successful"

workingShapefile = "F://572_Final_Project/BaseData/temporal_country_base.shp"
csvfile = "F://CSVs/Guardian_countries.csv"

##read the csv file
##make a dictionary by country key
##values are lists
csvreader = csv.reader(open(csvfile, 'rU'))

csvdata = {}


print "Loading data from csv"
for row in csvreader:
	thisCountry = row[1]
	if thisCountry not in csvdata.keys():
		csvdata[thisCountry] = []
	insertRow = (row[2], row[3])
	csvdata[thisCountry].append(insertRow)

cursors = {}

print "Adding fields"

arcpy.AddField_management(workingShapefile, "Date", "DATE")
arcpy.AddField_management(workingShapefile, "Mentions", "FLOAT")

print "Added fields to shapefile."

print "Getting field names."
fields = []
for field in arcpy.ListFields(workingShapefile):
	fields.append(field.name)
numFields = len(fields)
print "Found", numFields, "fields."


limiter = 0
#print "Starting search cursor"
with arcpy.da.UpdateCursor(workingShapefile, "*") as cursor:#
	for row in cursor:
		if limiter < 10:
			country = row[-3]
			if country not in cursors:
				cursors[country] = 0
			csvRecordNumber = cursors[country]
			if csvRecordNumber > 59:
				##reset if something funky happened
				csvRecordNumber = 0
				cursors[country] = 0
			if country in csvdata.keys():
				csvRecord = csvdata[country][csvRecordNumber]
				recordDate = csvRecord[0]
				recordValue = csvRecord[1]
				row[4] = recordDate
				row[5] = recordValue
				cursors[country] += 1
				cursor.updateRow(row)
				print row
				print "Completed", country, "record #", csvRecordNumber
			else:
				pass
		else:
			break
print "Now copying..."
arcpy.Copy_management(workingShapefile, "F://Analysis/Data/TS_Countries/Guardian_Countries.shp")
print "Now deleting fields..."
arcpy.DeleteField_management(workingShapefile, "Date")
arcpy.DeleteField_management(workingShapefile, "Mentions")
print "Job Complete."


			
