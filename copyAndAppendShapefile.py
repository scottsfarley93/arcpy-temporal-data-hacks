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
baseShapefile = "F://Analysis/Data/world_countries_3.shp"
shapeDump = "C://Users/student/documents/shapefileDump"

##make sure we start with an empty directory
clearDir(shapeDump)
print "Deleted all existing files in shapedump"

outputShapefile = "C://Users/student/documents/country_base.shp"
dataType = ""

list_of_shapefiles = []
i = 0
while i < 60:
	outname = shapeDump + "/" + str(i) + ".shp"
	arcpy.Copy_management(baseShapefile, outname, dataType)
	list_of_shapefiles.append(outname)
	print "Iteration", i, "Complete."
	i += 1

##append all the shapefiles to the output shapefile
print "Now appending..."
arcpy.Append_management(list_of_shapefiles, outputShapefile, "TEST", "", "")
print "Complete"