import csv
import arcpy
print "Import successful."

def clearDir(folder):
	import os, shutil
	for the_file in os.listdir(folder):
		file_path = os.path.join(folder, the_file)
		try:
			if os.path.isfile(file_path):
				os.unlink(file_path)
			#elif os.path.isdir(file_path): shutil.rmtree(file_path)
		except Exception, e:
			print e


			
##make 60 copies of a shapefile --> one for each day
baseShapefile = "F://Analysis/Data/world_cities.shp"
shapeDump = "C://Users/student/documents"

##make sure we start with an empty directory
clearDir(shapeDump)
print "Deleted all existing files in shapedump"

outputShapefile = "F://572_Final_Project/BaseData/cities_base.shp"
copies = 60
dataType = ""

list_of_shapefiles = []
i = 0
while i < copies:
	outname = shapeDump + "/" + str(i) + ".shp"
	arcpy.Copy_management(baseShapefile, outname, dataType)
	list_of_shapefiles.append(outname)
	print "Iteration", i, "Complete."
	i += 1

##append all the shapefiles to the output shapefile
print "Now copying..."
arcpy.Copy_management(baseShapefile, outputShapefile)
print "Now appending..."
arcpy.Append_management(list_of_shapefiles, outputShapefile, "TEST", "", "")
print "Complete"